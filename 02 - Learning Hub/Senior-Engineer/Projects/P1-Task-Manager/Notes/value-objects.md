---
tags:
  - ddd
  - domain
  - value-object
  - from/senior-p1-week-01
  - status/learning
aliases:
  - VO
  - Value Type
created: 2026-03-03
source: "Sessione Senior P1 Week 1 - Recap Exercise"
---

# Value Objects

> **One-liner:** Oggetti definiti dal loro VALORE, non da un'identità. Due VO con gli stessi attributi sono intercambiabili.

## Cos'è

Un **Value Object** è un oggetto del dominio che:
- **Non ha identità propria** (non ha ID)
- **È definito dai suoi attributi** (equality by value)
- **È immutabile** (non si modifica, si sostituisce)
- **Può avere comportamento** (metodi che ritornano nuovi VO)

### La differenza chiave: Identity vs Value

```
Entity:
  User(id: 1, name: "Dan") ≠ User(id: 2, name: "Dan")
  → Anche con stesso nome, sono DUE utenti diversi (ID diverso)

Value Object:
  Money(100, "EUR") == Money(100, "EUR")
  → Stesso valore = stessa cosa, intercambiabili
```

## Quando usarlo

| Situazione | Usa Value Object |
|------------|------------------|
| L'oggetto è definito dai suoi attributi | ✅ |
| Due oggetti con stessi valori sono "la stessa cosa" | ✅ |
| Vuoi garantire validazione sempre | ✅ |
| Vuoi incapsulare comportamento | ✅ |
| Non serve tracciare "quale" oggetto è | ✅ |

### Esempi classici

- `Money(100, "EUR")` - importo + valuta
- `Email("dan@test.com")` - validazione formato
- `DateRange(start, end)` - periodo temporale
- `Coordinate(lat, long)` - posizione geografica
- `Address(via, città, cap)` - indirizzo completo

## Quando NON usarlo

| Situazione | Usa invece |
|------------|------------|
| Serve tracciare l'identità | Entity |
| I valori cambiano frequentemente | Entity (mutabile) |
| Over-engineering per validazione semplice | Validazione nel costruttore Entity |

## Esempio Completo: Money (Recap Dan)

```csharp
public class Money
{
    public decimal Amount { get; }
    public string Currency { get; }

    // Costruttore PRIVATO
    private Money(decimal amount, string currency)
    {
        this.Amount = amount;
        this.Currency = currency;
    }

    // Factory method
    public static Money Create(decimal amount, string currency)
    {
        if (string.IsNullOrWhiteSpace(currency))
            throw new ArgumentNullException(nameof(currency));
        return new Money(amount, currency);
    }

    // Comportamento - ritorna NUOVO Money (immutabilità!)
    public Money Add(Money other)
    {
        if (other.Currency != this.Currency)
            throw new ArgumentException("Currency mismatch");
        return new Money(this.Amount + other.Amount, this.Currency);
    }

    public Money Subtract(Money other)
    {
        if (other.Currency != this.Currency)
            throw new ArgumentException("Currency mismatch");
        return new Money(this.Amount - other.Amount, this.Currency);
    }

    // EQUALITY BY VALUE - obbligatorio per VO!
    public override bool Equals(object? obj)
    {
        if (obj is not Money other) return false;
        return Amount == other.Amount && Currency == other.Currency;
    }

    public static bool operator ==(Money? a, Money? b)
        => a?.Equals(b) ?? b is null;

    public static bool operator !=(Money? a, Money? b)
        => !(a == b);

    // OBBLIGATORIO se fai override di Equals
    public override int GetHashCode()
        => HashCode.Combine(Amount, Currency);
}
```

### Test

```csharp
public class MoneyTest
{
    [Fact]
    public void Create_Money_ReturnMoney()
    {
        Money m = Money.Create(100, "EUR");
        m.Amount.Should().Be(100);
        m.Currency.Should().Be("EUR");
    }

    [Fact]
    public void TwoEqualMoney_AreEqual()
    {
        Money m1 = Money.Create(100, "EUR");
        Money m2 = Money.Create(100, "EUR");
        (m1 == m2).Should().BeTrue();
    }

    [Fact]
    public void Add_SameCurrency_ReturnsNewMoney()
    {
        Money m1 = Money.Create(100, "EUR");
        Money m2 = m1.Add(Money.Create(100, "EUR"));
        m2.Amount.Should().Be(200);
    }

    [Fact]
    public void Add_DifferentCurrency_ThrowsException()
    {
        Money m1 = Money.Create(100, "EUR");
        Action act = () => m1.Add(Money.Create(100, "CHF"));
        act.Should().Throw<ArgumentException>();
    }
}
```

## Checklist Implementazione VO

- [ ] Costruttore **privato**
- [ ] Factory method per creazione
- [ ] Proprietà **readonly** (immutabilità)
- [ ] Metodi ritornano **nuovo oggetto** (non mutano)
- [ ] Override `Equals()` (equality by value)
- [ ] Override `GetHashCode()` (obbligatorio con Equals)
- [ ] Operatori `==` e `!=` (opzionale ma utile)

## Smart Enum vs Value Object

| Tipo | Caratteristica | Esempio |
|------|----------------|---------|
| Smart Enum | Set FISSO di istanze predefinite | `Priority.High`, `Priority.Low` |
| Value Object | Qualsiasi valore valido | `Money(100, "EUR")`, `Money(50, "USD")` |

Vedi [[smart-enum]] per dettagli su Smart Enum.

## Collegamenti

- [[smart-enum]] - Tipo specifico di VO con set fisso
- [[ddd-building-blocks]] - Fa parte dei building blocks DDD
- [[entity]] - Contrasto: oggetti con identità

## Quiz

### Q1: Entity o Value Object?
`Email("dan@test.com")` è un Entity o Value Object? Perché?

<details>
<summary>Risposta</summary>

**Value Object.** Due oggetti Email con lo stesso indirizzo sono la stessa cosa - non ci interessa "quale" oggetto email sia, solo il valore. Non ha identità propria.

</details>

### Q2: Perché Equals e GetHashCode?
Perché è obbligatorio fare override di GetHashCode quando fai override di Equals?

<details>
<summary>Risposta</summary>

Perché Dictionary, HashSet e altre strutture dati usano GetHashCode per organizzare gli oggetti. Se due oggetti sono Equals, **devono** avere lo stesso HashCode, altrimenti queste strutture non funzionano correttamente.

</details>

### Q3: Immutabilità
Perché `Add()` ritorna un nuovo Money invece di modificare `this.Amount`?

<details>
<summary>Risposta</summary>

Perché i Value Objects sono **immutabili**. Non si modificano mai - si sostituiscono con nuovi oggetti. Questo garantisce:
- Thread safety
- Nessun side effect nascosto
- Predicibilità del comportamento

</details>

---

## Risorse per Approfondire

- **[Martin Fowler - Value Object](https://martinfowler.com/bliki/ValueObject.html)** - Definizione originale
- **[Implementing Value Objects](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/implement-value-objects)** - Microsoft Docs
- **[DDD Quickly - Value Objects](https://www.infoq.com/minibooks/domain-driven-design-quickly/)** - Capitolo specifico

---

*Creato durante: Senior P1 Week 1 - Task Manager (Recap Exercise Money)*
