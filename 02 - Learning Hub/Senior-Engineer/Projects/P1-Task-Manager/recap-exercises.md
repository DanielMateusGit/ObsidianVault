---
tags: [senior-engineer, exercises, p1]
created: 2026-03-03
---

# 🎯 Esercizi Recap - P1 Task Manager

> Dopo ogni argomento TDD, Dan fa un esercizio simile **da solo** (compartimento stagno).

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| **Esercizi completati** | 1 |
| **XP totali esercizi** | 105 |
| **Primo tentativo** | 1 |
| **Media tentativi** | 1.0 |

---

## 📋 Esercizi

### Esercizio 1: Project Entity

**Argomento:** Entity Pattern (dopo TaskItem)

**Specifica:**
Crea un'entity `Project` con:
- `Id` (Guid, generato automaticamente)
- `Name` (string, obbligatorio, non vuoto)
- `Description` (string?, opzionale)
- `CreatedAt` (DateTime, impostato alla creazione)
- Metodo `Rename(string newName)` con validazione

**Test richiesti:**
1. `Constructor_WithValidName_SetsName`
2. `Constructor_WhenCalled_GeneratesUniqueId`
3. `Constructor_WithEmptyName_ThrowsArgumentException`
4. `Rename_WithValidName_UpdatesName`
5. `Rename_WithEmptyName_ThrowsArgumentException`

| Campo | Valore |
|-------|--------|
| **Status** | ✅ Completato |
| **Tentativi** | 1 |
| **XP** | +75 (+50 base, +25 primo tentativo) |
| **Data completamento** | 2026-03-03 |

---

### Esercizio 2: DueDate Value Object

**Argomento:** Value Object (dopo Priority)

**Specifica:**
Crea un Value Object `DueDate` con:
- `Value` (DateTime)
- Factory method `FromDateTime(DateTime date)` che valida che la data sia futura
- Metodo `IsOverdue()` che ritorna true se la data è passata
- Metodo `DaysRemaining()` che ritorna i giorni mancanti

**Test richiesti:**
1. `FromDateTime_WithFutureDate_CreatesDueDate`
2. `FromDateTime_WithPastDate_ThrowsArgumentException`
3. `IsOverdue_WhenDatePassed_ReturnsTrue`
4. `IsOverdue_WhenDateFuture_ReturnsFalse`
5. `DaysRemaining_ReturnsCorrectDays`

| Campo | Valore |
|-------|--------|
| **Status** | ⬜ Non iniziato |
| **Tentativi** | 0 |
| **XP** | - |
| **Data completamento** | - |

---

### Esercizio 3: TaskCompletedEvent

**Argomento:** Domain Events (dopo Complete())

**Specifica:**
Crea un Domain Event `TaskCompletedEvent` con:
- `TaskId` (Guid)
- `CompletedAt` (DateTime)
- `OccurredOn` (DateTime, impostato automaticamente)

Modifica `TaskItem.Complete()` per creare l'evento.

**Test richiesti:**
1. `TaskCompletedEvent_HasCorrectTaskId`
2. `TaskCompletedEvent_HasCorrectCompletedAt`
3. `TaskItem_WhenCompleted_RaisesTaskCompletedEvent`

| Campo | Valore |
|-------|--------|
| **Status** | ⬜ Non iniziato |
| **Tentativi** | 0 |
| **XP** | - |
| **Data completamento** | - |

---

### Esercizio 4: IProjectRepository

**Argomento:** Repository Pattern

**Specifica:**
Crea l'interfaccia `IProjectRepository` con:
- `GetByIdAsync(Guid id)`
- `GetAllAsync()`
- `AddAsync(Project project)`
- `UpdateAsync(Project project)`
- `DeleteAsync(Guid id)`

Crea un'implementazione in-memory `InMemoryProjectRepository` per i test.

**Test richiesti:**
1. `AddAsync_AddsProjectToRepository`
2. `GetByIdAsync_ReturnsCorrectProject`
3. `GetByIdAsync_WithInvalidId_ReturnsNull`
4. `GetAllAsync_ReturnsAllProjects`
5. `DeleteAsync_RemovesProject`

| Campo | Valore |
|-------|--------|
| **Status** | ⬜ Non iniziato |
| **Tentativi** | 0 |
| **XP** | - |
| **Data completamento** | - |

---

## 🏆 Achievement Progress

| Achievement | Requisito | Status |
|-------------|-----------|--------|
| 🏋️ First Solo | 1 esercizio completato | ✅ +30 XP |
| 💪 Solo Streak | 5 corretti consecutivi | ⬜ (1/5) |
| 🎯 Perfect Form | 10 al primo tentativo | ⬜ (1/10) |
| 🏆 Independent Dev | Tutti gli esercizi P1 | ⬜ (1/4) |

---

## 📝 Regole

1. **Zero aiuto** - Claude non risponde durante l'esercizio
2. **Tempo libero** - Nessun limite, ma traccia quanto ci metti
3. **Valutazione finale** - Claude corregge solo quando dici "ho finito"
4. **Retry** - Puoi riprovare, ma conta come tentativo aggiuntivo

---

*Creato: 2026-03-03*
