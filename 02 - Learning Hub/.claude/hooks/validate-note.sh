#!/bin/bash
# Hook: PostToolUse - Valida note in Knowledge/
# Verifica che le note abbiano la struttura obbligatoria

# Leggi lo stdin (JSON dal hook system)
INPUT=$(cat)

# Estrai il path del file scritto
FILE_PATH=$(echo "$INPUT" | python3 -c "
import json, sys
data = json.load(sys.stdin)
# Il path è nel tool_input dell'evento Write
tool_input = data.get('tool_input', {})
print(tool_input.get('file_path', tool_input.get('filePath', '')))
" 2>/dev/null)

# Se non è un file in Knowledge/, esci con successo (non bloccare)
if [[ ! "$FILE_PATH" =~ Knowledge/.*\.md$ ]]; then
    exit 0
fi

# Se è Knowledge/CLAUDE.md (l'indice), non validare
if [[ "$FILE_PATH" =~ Knowledge/CLAUDE\.md$ ]]; then
    exit 0
fi

# Verifica che il file esista
if [[ ! -f "$FILE_PATH" ]]; then
    exit 0
fi

CONTENT=$(cat "$FILE_PATH")
ERRORS=""

# 1. Verifica frontmatter con tags
if ! echo "$CONTENT" | head -20 | grep -q "^tags:"; then
    ERRORS="${ERRORS}\n- Manca frontmatter 'tags:'"
fi

# 2. Verifica frontmatter con created
if ! echo "$CONTENT" | head -20 | grep -q "^created:"; then
    ERRORS="${ERRORS}\n- Manca frontmatter 'created:'"
fi

# 3. Verifica frontmatter con source
if ! echo "$CONTENT" | head -20 | grep -q "^source:"; then
    ERRORS="${ERRORS}\n- Manca frontmatter 'source:'"
fi

# 4. Verifica sezione Cos'è o Cos'e
if ! echo "$CONTENT" | grep -qE "^## Cos'[eè]|^## Cos'è"; then
    ERRORS="${ERRORS}\n- Manca sezione '## Cos'è'"
fi

# 5. Verifica sezione Quando usarlo
if ! echo "$CONTENT" | grep -q "^## Quando usarlo"; then
    ERRORS="${ERRORS}\n- Manca sezione '## Quando usarlo'"
fi

# 6. Verifica sezione Quiz
if ! echo "$CONTENT" | grep -q "^## Quiz"; then
    ERRORS="${ERRORS}\n- Manca sezione '## Quiz'"
fi

# 7. Verifica almeno 3 quiz (### Q)
QUIZ_COUNT=$(echo "$CONTENT" | grep -c "^### Q[0-9]")
if [[ $QUIZ_COUNT -lt 3 ]]; then
    ERRORS="${ERRORS}\n- Servono almeno 3 quiz (### Q), trovati: $QUIZ_COUNT"
fi

# Se ci sono errori, blocca
if [[ -n "$ERRORS" ]]; then
    echo "{
  \"decision\": \"block\",
  \"reason\": \"La nota in Knowledge/ non rispetta il template obbligatorio:$(echo -e "$ERRORS" | sed 's/"/\\"/g' | tr '\n' ' ')\"
}"
    exit 0
fi

# Tutto ok
exit 0
