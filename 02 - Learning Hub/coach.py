#!/usr/bin/env python3
"""
🤖 Learning Coach Agent
Un agente locale che legge il tuo vault Obsidian e ti aiuta a studiare.

Setup:
1. brew install ollama
2. ollama pull llama3.1:8b
3. pip install pyyaml rich ollama
4. chmod +x coach.py
5. ./coach.py briefing
"""

import os
import re
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional
import random

# === CONFIGURAZIONE ===
VAULT_PATH = Path("/Users/Dan/Documents/Obsidian Vault/02 - Learning Hub")
MODEL = "llama3.1:8b"  # Oppure: qwen2.5:32b, mistral, etc.
# ======================

try:
    import ollama
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.markdown import Markdown
except ImportError:
    print("Installa le dipendenze: pip install ollama rich pyyaml")
    sys.exit(1)

console = Console()

# ============================================================
# PARSING OBSIDIAN
# ============================================================

def parse_frontmatter(content: str) -> dict:
    """Estrae frontmatter YAML da un file markdown."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)) or {}
        except:
            return {}
    return {}

def update_frontmatter(filepath: Path, updates: dict):
    """Aggiorna campi nel frontmatter di un file."""
    content = filepath.read_text()
    fm = parse_frontmatter(content)
    fm.update(updates)
    
    # Ricostruisci il file
    fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    
    if content.startswith('---'):
        # Sostituisci frontmatter esistente
        rest = re.sub(r'^---\n.*?\n---\n?', '', content, flags=re.DOTALL)
        new_content = f"---\n{fm_str}---\n{rest}"
    else:
        new_content = f"---\n{fm_str}---\n\n{content}"
    
    filepath.write_text(new_content)

def get_progress() -> dict:
    """Legge lo stato di progressione."""
    progress_file = VAULT_PATH / "Progress.md"
    if not progress_file.exists():
        return {"xp": 0, "level": 1, "title": "Apprentice", "streak": 0}
    
    content = progress_file.read_text()
    return parse_frontmatter(content)

def get_daily_logs(days: int = 7) -> list:
    """Legge gli ultimi N daily logs."""
    daily_path = VAULT_PATH / "Daily"
    if not daily_path.exists():
        return []
    
    logs = []
    for file in sorted(daily_path.glob("*.md"), reverse=True)[:days]:
        content = file.read_text()
        fm = parse_frontmatter(content)
        logs.append({
            "date": file.stem,
            "completed": fm.get("completed", False),
            "hours": fm.get("hours", 0),
            "minutes": fm.get("minutes", 0),
            "xp_earned": fm.get("xp_earned", 0),
            "focus": fm.get("focus", ""),
            "content": content
        })
    return logs

def calculate_streak(logs: list) -> int:
    """Calcola lo streak corrente."""
    if not logs:
        return 0
    
    streak = 0
    today = datetime.now().date()
    
    for i, log in enumerate(logs):
        try:
            log_date = datetime.strptime(log["date"], "%Y-%m-%d").date()
        except:
            continue
        
        expected = today - timedelta(days=i)
        if log_date == expected and log.get("completed"):
            streak += 1
        else:
            break
    
    return streak

def get_recent_concepts() -> list:
    """Trova concetti studiati di recente."""
    concepts = []
    
    for project in ["Architect-Quest", "Senior-Engineer"]:
        concepts_path = VAULT_PATH / project / "Concepts"
        if concepts_path.exists():
            for file in concepts_path.rglob("*.md"):
                content = file.read_text()
                fm = parse_frontmatter(content)
                if fm.get("status") in ["in-progress", "completed"]:
                    concepts.append({
                        "name": file.stem,
                        "path": str(file.relative_to(VAULT_PATH)),
                        "project": project,
                        "content": content[:1000]
                    })
    
    return concepts[-10:]

def get_current_tasks() -> list:
    """Trova i task correnti."""
    tasks = []
    
    for project in ["Architect-Quest", "Senior-Engineer"]:
        project_path = VAULT_PATH / project / "Projects"
        if project_path.exists():
            for file in project_path.rglob("*.md"):
                content = file.read_text()
                uncompleted = re.findall(r'- \[ \] (.+)', content)
                for task in uncompleted[:5]:
                    tasks.append({
                        "task": task,
                        "file": file.stem,
                        "project": project
                    })
    
    return tasks[:15]

# ============================================================
# INTERAZIONE CON OLLAMA
# ============================================================

SYSTEM_PROMPT = """Sei un coach per l'apprendimento di software engineering e architettura.
Il tuo studente Dan sta seguendo due percorsi paralleli:
1. Architect Quest - system design, cloud, progettare per AI
2. Senior Engineer Path - coding hands-on, patterns, TDD, Redis

Il tuo ruolo:
- Motivare e celebrare i progressi
- Suggerire cosa studiare basandoti sul contesto
- Fare domande per verificare comprensione (spaced repetition)
- Avvisare se lo streak è a rischio
- Essere conciso ma supportivo

IMPORTANTE:
- Parla in italiano
- Usa emoji per engagement
- Sii pratico e actionable
- Ricorda: Dan lavora full-time, studia la sera (1-2h weekdays, 3-4h weekend)
"""

def ask_ollama(prompt: str, context: str = "") -> str:
    """Chiede qualcosa a Ollama."""
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{context}\n\n{prompt}" if context else prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"❌ Errore Ollama: {e}\n\nAssicurati che Ollama sia avviato: `ollama serve`"

# ============================================================
# COMANDI
# ============================================================

def cmd_status():
    """Mostra lo status completo."""
    progress = get_progress()
    logs = get_daily_logs(7)
    streak = calculate_streak(logs)
    
    # Aggiorna streak nel file
    if progress.get("streak") != streak:
        progress_file = VAULT_PATH / "Progress.md"
        if progress_file.exists():
            update_frontmatter(progress_file, {"streak": streak})
    
    table = Table(title="📊 Status")
    table.add_column("Stat", style="cyan")
    table.add_column("Valore", style="green")
    
    table.add_row("Level", f"{progress.get('level', 1)}")
    table.add_row("Title", progress.get('title', 'Apprentice'))
    table.add_row("XP", f"{progress.get('xp', 0)}")
    table.add_row("Streak", f"{streak} giorni 🔥" if streak > 0 else "0 giorni")
    table.add_row("Best Streak", f"{progress.get('longest_streak', 0)} giorni")
    
    console.print(table)
    
    # XP settimana
    week_xp = sum(log.get("xp_earned", 0) for log in logs)
    week_time = sum(log.get("hours", 0) * 60 + log.get("minutes", 0) for log in logs)
    
    console.print(f"\n📅 **Ultimi 7 giorni:** +{week_xp} XP, {week_time//60}h {week_time%60}m di studio")

def cmd_motivation():
    """Frase motivazionale giornaliera basata sul PERCHÉ."""
    console.print(Panel("💪 IL TUO PERCHÉ", style="bold magenta"))

    # Leggi WHY.md
    why_file = VAULT_PATH / "claude" / "WHY.md"
    if not why_file.exists():
        console.print("❌ File WHY.md non trovato!")
        return

    why_content = why_file.read_text()
    progress = get_progress()

    # Scegli un tema random per varietà
    themes = [
        "casa_federica",
        "famiglia_supporto",
        "figli_futuro",
        "liberta_finanziaria",
        "numeri_concreti",
        "roi_impegno"
    ]
    today_theme = random.choice(themes)

    context = f"""
## Il PERCHÉ di Dan (dal file WHY.md):
{why_content[:2000]}

## Progresso attuale:
- Level: {progress.get('level', 1)} - {progress.get('title', 'Apprentice')}
- XP: {progress.get('xp', 0)}

## Tema oggi: {today_theme}
"""

    prompt = f"""Basandoti sul file WHY.md, dammi UNA frase motivazionale potente (massimo 2-3 righe) che:

1. Si concentri sul tema: {today_theme}
2. Includa un numero concreto quando possibile (€2k in più al mese, casa in 2-3 anni, etc.)
3. Connetta lo studio di OGGI a un obiettivo concreto
4. Sia emotiva ma non sdolcinata
5. Usi emoji pertinenti

Esempi di tono:
- "Ogni ora di studio oggi = €100 in più al mese tra 18 mesi. Quella casa per te e Federica è più vicina di quanto pensi. 🏡"
- "Oggi non stai solo imparando Redis. Stai costruendo la tranquillità per mamma e papà quando avranno bisogno di te. ❤️"
- "€2000 in più al mese = €800 risparmi casa + €500 famiglia. Questo progetto ti porta lì. 💪"

La frase:"""

    response = ask_ollama(prompt, context)
    console.print(Panel(Markdown(response), style="bold magenta"))

    # Aggiungi reminder dei numeri chiave
    console.print("\n[dim]📊 Numeri chiave:[/dim]")
    console.print("[dim]   • Target: €100-120k/anno (da €50-60k ora)[/dim]")
    console.print("[dim]   • +€2-2.3k/mese netto[/dim]")
    console.print("[dim]   • Casa: fattibile in 2-3 anni[/dim]")
    console.print("[dim]   • 18 mesi = 40 anni di tranquillità ❤️[/dim]")

def cmd_briefing():
    """Briefing giornaliero motivante."""
    console.print(Panel("🤖 Daily Briefing", style="bold blue"))

    progress = get_progress()
    logs = get_daily_logs(7)
    streak = calculate_streak(logs)
    tasks = get_current_tasks()

    context = f"""
## Status Dan
- Level: {progress.get('level', 1)} - {progress.get('title', 'Apprentice')}
- XP: {progress.get('xp', 0)}
- Streak: {streak} giorni
- Settimana Architect Quest: {progress.get('architect_quest_week', 'P1-W1')}
- Settimana Senior Engineer: {progress.get('senior_engineer_week', 'P1-W1')}

## Attività recenti (ultimi 5 giorni)
{chr(10).join([f"- {log['date']}: {'✅' if log['completed'] else '❌'} {log['hours']}h{log['minutes']}m, +{log['xp_earned']} XP" for log in logs[:5]])}

## Task aperti
{chr(10).join([f"- [{t['project']}] {t['task']}" for t in tasks[:8]])}
"""

    prompt = """Dammi un briefing giornaliero:
1. Saluto personalizzato basato su streak e progressi
2. Cosa dovrei studiare oggi (scegli UN focus principale)
3. Tempo suggerito basato sul giorno (oggi è """ + datetime.now().strftime("%A") + """)
4. Un tip motivazionale breve

Sii conciso ma engaging!"""

    response = ask_ollama(prompt, context)
    console.print(Panel(Markdown(response), style="green"))

def cmd_quiz():
    """Quiz su concetti recenti."""
    console.print(Panel("🧠 Quiz Time!", style="bold yellow"))
    
    concepts = get_recent_concepts()
    if not concepts:
        console.print("Nessun concetto trovato. Inizia a studiare e documentare!")
        return
    
    concept = random.choice(concepts)
    
    prompt = f"""Basandoti su questo concetto che Dan ha studiato:

**{concept['name']}** (da {concept['project']})

Contenuto note:
{concept['content'][:800]}

Fai UNA domanda per verificare che Dan abbia capito davvero il concetto.
La domanda deve:
- Essere pratica, non teorica
- Richiedere di spiegare "quando" o "perché", non solo "cosa"
- Essere rispondibile in 2-3 frasi

Alla fine, dopo la domanda, aggiungi:
"💡 Prova a rispondere, poi dimmi 'verifica' per il feedback!"
"""
    
    response = ask_ollama(prompt)
    console.print(Panel(Markdown(response), style="yellow"))
    console.print("\n[dim]Rispondi e poi esegui: ./coach.py verify 'la tua risposta'[/dim]")

def cmd_suggest():
    """Suggerisce cosa studiare."""
    console.print(Panel("🎯 Cosa studiare oggi?", style="bold cyan"))
    
    progress = get_progress()
    logs = get_daily_logs(3)
    tasks = get_current_tasks()
    
    today = datetime.now().strftime("%A")
    is_weekend = today in ["Saturday", "Sunday"]
    suggested_time = "3-4 ore" if is_weekend else "1-2 ore"
    
    context = f"""
Oggi è {today}.
Tempo disponibile suggerito: {suggested_time}

Progress:
- Architect Quest: {progress.get('architect_quest_week', 'P1-W1')}
- Senior Engineer: {progress.get('senior_engineer_week', 'P1-W1')}

Task aperti:
{chr(10).join([f"- [{t['project']}] {t['task']}" for t in tasks[:10]])}

Ultimi 3 giorni:
{chr(10).join([f"- {log['date']}: focus su {log.get('focus', 'non specificato')}" for log in logs])}
"""
    
    prompt = """Basandoti sul contesto, suggerisci:

1. **Focus principale** - UN solo argomento/task su cui concentrarsi
2. **Perché questo** - Come si collega al percorso
3. **Deliverable concreto** - Cosa dovrebbe completare entro fine sessione
4. **Bonus** (se avanza tempo) - Cosa fare extra

Sii specifico e actionable!"""
    
    response = ask_ollama(prompt, context)
    console.print(Panel(Markdown(response), style="cyan"))

def cmd_add_xp(amount: int, reason: str):
    """Aggiunge XP manualmente."""
    progress_file = VAULT_PATH / "Progress.md"
    if not progress_file.exists():
        console.print("❌ File Progress.md non trovato")
        return
    
    progress = get_progress()
    new_xp = progress.get("xp", 0) + amount
    
    levels = [
        (0, 1, "Apprentice Developer"),
        (500, 2, "Code Crafter"),
        (1200, 3, "Pattern Seeker"),
        (2000, 4, "Module Builder"),
        (3000, 5, "Service Architect"),
        (4200, 6, "Domain Master"),
        (5600, 7, "System Designer"),
        (7200, 8, "Cloud Engineer"),
        (9000, 9, "Principal Developer"),
        (11000, 10, "Staff Engineer"),
        (15000, 11, "Senior Architect"),
        (20000, 12, "AI-Native Architect"),
    ]
    
    new_level = 1
    new_title = "Apprentice Developer"
    for xp_req, lvl, title in levels:
        if new_xp >= xp_req:
            new_level = lvl
            new_title = title
    
    old_level = progress.get("level", 1)
    
    update_frontmatter(progress_file, {
        "xp": new_xp,
        "level": new_level,
        "title": new_title
    })
    
    console.print(f"✅ +{amount} XP: {reason}")
    console.print(f"📊 Totale: {new_xp} XP")
    
    if new_level > old_level:
        console.print(Panel(f"🎉 LEVEL UP! Lv.{new_level} - {new_title}", style="bold green"))

def cmd_streak_check():
    """Controlla se lo streak è a rischio."""
    logs = get_daily_logs(2)
    today = datetime.now().date()
    
    today_log = None
    for log in logs:
        try:
            if datetime.strptime(log["date"], "%Y-%m-%d").date() == today:
                today_log = log
                break
        except:
            pass
    
    if today_log and today_log.get("completed"):
        streak = calculate_streak(logs)
        console.print(f"✅ Streak sicuro! {streak} giorni 🔥")
    else:
        console.print(Panel(
            "⚠️ **STREAK A RISCHIO!**\n\n"
            "Non hai ancora completato il daily di oggi.\n"
            "Serve: 30min studio OPPURE 1 commit OPPURE 1 task.\n\n"
            "Il tuo streak andrà perso a mezzanotte!",
            style="bold red"
        ))

def cmd_help():
    """Mostra aiuto."""
    help_text = """
# 🤖 Learning Coach - Comandi

## Comandi principali
- `briefing` - Briefing giornaliero motivante
- `motivation` - Frase motivazionale sul TUO perché (casa, Federica, famiglia) 💪
- `status` - Mostra XP, level, streak
- `suggest` - Cosa studiare oggi
- `quiz` - Quiz su concetti recenti
- `streak` - Controlla se streak è a rischio

## Gestione XP
- `add-xp <amount> <reason>` - Aggiungi XP manualmente
  Esempio: `./coach.py add-xp 50 "Completato task TDD"`

## Setup
- `check` - Verifica configurazione

## Esempi
```bash
./coach.py motivation        # Ricordati perché lo fai!
./coach.py briefing
./coach.py add-xp 100 "Deliverable completato"
./coach.py quiz
```
"""
    console.print(Markdown(help_text))

def cmd_check():
    """Verifica la configurazione."""
    console.print(Panel("🔧 Controllo configurazione", style="bold"))
    
    # Check vault
    if VAULT_PATH.exists():
        console.print(f"✅ Vault trovato: {VAULT_PATH}")
    else:
        console.print(f"❌ Vault NON trovato: {VAULT_PATH}")
        console.print("   Modifica VAULT_PATH nello script!")
        return
    
    # Check struttura
    required = ["Progress.md", "Daily"]
    for item in required:
        path = VAULT_PATH / item
        if path.exists():
            console.print(f"✅ {item}")
        else:
            console.print(f"❌ {item} mancante")
    
    # Check Ollama
    try:
        models_response = ollama.list()
        console.print(f"✅ Ollama connesso")

        # Check modello (supporta sia nuovo che vecchio formato API)
        models = models_response.get('models', []) if isinstance(models_response, dict) else getattr(models_response, 'models', [])
        model_names = [getattr(m, 'model', m.get('name', '')) if hasattr(m, 'model') else m.get('name', '') for m in models]
        if any(MODEL in m for m in model_names):
            console.print(f"✅ Modello {MODEL} disponibile")
        else:
            console.print(f"⚠️ Modello {MODEL} non trovato. Esegui: ollama pull {MODEL}")
    except Exception as e:
        console.print(f"❌ Ollama non raggiungibile: {e}")
        console.print("   Esegui: ollama serve")

# ============================================================
# MAIN
# ============================================================

def main():
    if len(sys.argv) < 2:
        cmd_help()
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        "briefing": cmd_briefing,
        "motivation": cmd_motivation,
        "status": cmd_status,
        "suggest": cmd_suggest,
        "quiz": cmd_quiz,
        "streak": cmd_streak_check,
        "check": cmd_check,
        "help": cmd_help,
    }
    
    if command == "add-xp" and len(sys.argv) >= 4:
        try:
            amount = int(sys.argv[2])
            reason = " ".join(sys.argv[3:])
            cmd_add_xp(amount, reason)
        except ValueError:
            console.print("❌ Uso: ./coach.py add-xp <numero> <motivo>")
    elif command in commands:
        commands[command]()
    else:
        console.print(f"❌ Comando sconosciuto: {command}")
        cmd_help()

if __name__ == "__main__":
    main()