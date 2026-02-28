---
tags:
  - architecture
  - ddd
  - validation
  - domain-model
  - from/article
  - status/learned
aliases:
  - Validation vs Invariants
  - Always-Valid Domain Model
  - Domain Validation
created: 2026-02-26
updated: 2026-02-28
source: "Vladimir Khorikov - Validation and DDD, Validations vs Invariants"
---
V
# Validation vs Invariants in DDD

> **One-liner:** Validation protegge il Domain da input esterni (Application Layer), Invariants proteggono il Domain da uso scorretto interno (Domain Layer).

---

## Cos'è

In Domain-Driven Design, c'è una distinzione critica tra:

- **Validation** = Controlli su input esterni (utente, API, file)
- **Invariants** = Regole che definiscono l'essenza del Domain

**Non sono la stessa cosa**, anche se possono controllare lo stesso dato (es. "email obbligatoria").

### Il Problema

```csharp
// ❌ Dove metto il controllo "email obbligatoria"?

// Opzione 1: Solo in Application?
public class CreateUserCommandValidator : AbstractValidator<CreateUserCommand>
{
    RuleFor(x => x.Email).NotEmpty();  // ← Cosa succede se un programmatore
}                                       //   crea User senza validator?

// Opzione 2: Solo in Domain?
public class User
{
    public User(string email)
    {
        if (string.IsNullOrEmpty(email))
            throw new DomainException("Email required");  // ← Eccezione anche per input utente?
    }
}

// Opzione 3: In entrambi? (✅ GIUSTO!)
```

---

## La Distinzione Chiave

### 📊 Confronto

| Aspetto | **Validation** | **Invariants** |
|---------|----------------|----------------|
| **Dove vive** | Application Layer | Domain Layer |
| **Cosa protegge** | Domain da input esterni | Domain da uso scorretto |
| **Chi può fallire** | Utente, API esterna | Programmatore (bug) |
| **Come fallisce** | `Result<T>` o `ValidationException` | `DomainException` |
| **Messaggio** | User-friendly ("Email obbligatoria") | Tecnico ("Email cannot be null") |
| **Quando controlla** | Prima di entrare nel Domain | Quando crei/modifichi Entity |
| **Esempi** | Formato email, lunghezza password | "Order ha almeno 1 item" |

### 🎯 Esempio: Il Triangolo (di Dan)

```csharp
// ═══════════════════════════════════════════════════════
//  DOMAIN LAYER - Invariant
// ═══════════════════════════════════════════════════════

public class Triangle : Entity
{
    private readonly List<Side> _sides = new();

    private Triangle() { }  // ← EF Core

    public static Triangle Create(Side side1, Side side2, Side side3)
    {
        // ═══════════════════════════════════════════════════════
        //  INVARIANT: Un triangolo HA 3 lati
        // ═══════════════════════════════════════════════════════
        // Se questa regola è violata, NON È UN TRIANGOLO!

        if (side1 == null || side2 == null || side3 == null)
            throw new DomainException("Triangle must have exactly 3 sides");

        // Altra invariant: Disuguaglianza triangolare
        if (!IsValidTriangle(side1, side2, side3))
            throw new DomainException("Invalid triangle: sides don't satisfy triangle inequality");

        return new Triangle { _sides = new List<Side> { side1, side2, side3 } };
    }

    // ═══════════════════════════════════════════════════════
    //  Questa è un'INVARIANT perché:
    //  - Definisce l'ESSENZA di Triangle
    //  - Se violata → l'oggetto non è valido
    //  - Deve essere SEMPRE vera (sempre valido)
    // ═══════════════════════════════════════════════════════
}


// ═══════════════════════════════════════════════════════
//  APPLICATION LAYER - Validation
// ═══════════════════════════════════════════════════════

public record CreateTriangleCommand(
    decimal Side1Length,
    decimal Side2Length,
    decimal Side3Length
) : IRequest<Result<Guid>>;

public class CreateTriangleCommandValidator : AbstractValidator<CreateTriangleCommand>
{
    public CreateTriangleCommandValidator()
    {
        // ═══════════════════════════════════════════════════════
        //  VALIDATION: Input utente deve avere 3 lati
        // ═══════════════════════════════════════════════════════

        RuleFor(x => x.Side1Length)
            .GreaterThan(0)
            .WithMessage("Side 1 length must be greater than 0");

        RuleFor(x => x.Side2Length)
            .GreaterThan(0)
            .WithMessage("Side 2 length must be greater than 0");

        RuleFor(x => x.Side3Length)
            .GreaterThan(0)
            .WithMessage("Side 3 length must be greater than 0");

        // ═══════════════════════════════════════════════════════
        //  Questa è VALIDATION perché:
        //  - Controlla INPUT ESTERNO (utente)
        //  - Se fallisce → messaggio user-friendly
        //  - Ritorna Result.Failure, non Exception
        // ═══════════════════════════════════════════════════════
    }
}

// Handler
public class CreateTriangleHandler : IRequestHandler<CreateTriangleCommand, Result<Guid>>
{
    public async Task<Result<Guid>> Handle(CreateTriangleCommand request, ...)
    {
        // Validation già passata (ValidationBehavior)
        // Ora crea l'entità

        var side1 = Side.Create(request.Side1Length);
        var side2 = Side.Create(request.Side2Length);
        var side3 = Side.Create(request.Side3Length);

        var triangle = Triangle.Create(side1, side2, side3);  // ← Invariant check

        await _repository.AddAsync(triangle);

        return Result<Guid>.Success(triangle.Id);
    }
}
```

**La stessa regola ("3 lati") è controllata DUE VOLTE:**
1. **Application** (Validation): Protegge da input utente sbagliato → Result
2. **Domain** (Invariant): Protegge da programmatore che usa male Triangle → Exception

---

## Doppia Protezione: Esempio Email (di Dan)

```csharp
// ═══════════════════════════════════════════════════════
//  SCENARIO: Email obbligatoria per Notification
// ═══════════════════════════════════════════════════════


// ═══════════════════════════════════════════════════════
//  1. APPLICATION LAYER - Validation (input utente)
// ═══════════════════════════════════════════════════════

public record ScheduleNotificationCommand(
    string RecipientEmail,
    string Message,
    DateTime ScheduledAt
) : IRequest<Result<Guid>>;

public class ScheduleNotificationCommandValidator : AbstractValidator<ScheduleNotificationCommand>
{
    public ScheduleNotificationCommandValidator()
    {
        RuleFor(x => x.RecipientEmail)
            .NotEmpty()
            .WithMessage("Email is required")           // ← User-friendly
            .EmailAddress()
            .WithMessage("Invalid email format");       // ← User-friendly
    }
}

// ═══════════════════════════════════════════════════════
//  2. DOMAIN LAYER - Invariant (protezione interna)
// ═══════════════════════════════════════════════════════

public class Email : ValueObject
{
    public string Value { get; }

    private Email(string value)
    {
        Value = value;
    }

    public static Email Create(string value)
    {
        // ═══════════════════════════════════════════════════════
        //  INVARIANT: Email non può essere vuota
        // ═══════════════════════════════════════════════════════

        if (string.IsNullOrWhiteSpace(value))
            throw new DomainException("Email cannot be empty");  // ← Fail-fast

        if (!IsValidFormat(value))
            throw new DomainException("Invalid email format");   // ← Fail-fast

        return new Email(value.ToLower().Trim());
    }

    private static bool IsValidFormat(string email)
    {
        return Regex.IsMatch(email, @"^[^@\s]+@[^@\s]+\.[^@\s]+$");
    }

    protected override IEnumerable<object> GetEqualityComponents()
    {
        yield return Value;
    }
}

public class Notification : Entity
{
    public Email RecipientEmail { get; private set; }  // ← Sempre valido!

    private Notification() { }  // EF Core

    public static Notification Create(Email recipientEmail, string message, ...)
    {
        // ═══════════════════════════════════════════════════════
        //  INVARIANT: Notification richiede email valida
        // ═══════════════════════════════════════════════════════

        if (recipientEmail == null)
            throw new DomainException("RecipientEmail is required");  // ← Invariant

        return new Notification
        {
            Id = Guid.NewGuid(),
            RecipientEmail = recipientEmail,  // ← Già validato nel Value Object
            Message = message,
            Status = NotificationStatus.Pending
        };
    }
}


// ═══════════════════════════════════════════════════════
//  COSA SUCCEDE IN PRATICA
// ═══════════════════════════════════════════════════════

// Scenario 1: Utente manda form con email vuota
// ────────────────────────────────────────────────────────
var command = new ScheduleNotificationCommand("", "Hello", DateTime.Now);

// 1. ValidationBehavior esegue ScheduleNotificationCommandValidator
// 2. Validation fallisce: "Email is required"
// 3. Ritorna Result<Guid>.Failure("Email is required")
// 4. API ritorna 400 Bad Request con messaggio user-friendly
// 5. ✅ Domain NON viene toccato (protetto!)


// Scenario 2: Programmatore usa male il Domain
// ────────────────────────────────────────────────────────
// Mettiamo che un programmatore nuovo fa:
var notification = new Notification();  // ← Costruttore privato, non compila!

// Ma anche se aggirasse il costruttore:
var email = Email.Create("");  // ← BOOM! DomainException
// 💥 "Email cannot be empty"
// ✅ Domain si protegge da uso scorretto


// Scenario 3: Factory Pattern (uso legittimo)
// ────────────────────────────────────────────────────────
public class NotificationFactory
{
    public Notification CreateWelcomeNotification(User user)
    {
        // Se user.Email è null (BUG del programmatore):
        var email = Email.Create(user.Email);  // ← BOOM! DomainException
        // ✅ Fail-fast: meglio crashare qui che avere dati inconsistenti
    }
}
```

---

## Pattern Execute/CanExecute (Preferito da Khorikov)

> **Questo pattern ti ha colpito!** È quello che userai nel Notification Service.

### Il Problema

Come validare un'operazione nel Domain mantenendo:
1. **Always-valid state** (l'Entity non entra mai in stato invalido)
2. **CQS** (Command-Query Separation)
3. **Logica nel Domain** (non dispersa nell'Application)

### Le 4 Soluzioni di Khorikov

| # | Soluzione | Pro | Contro | Verdetto |
|---|-----------|-----|--------|----------|
| 1 | `IsValid()` dopo assegnazione | Logica nel Domain | Entity entra in stato invalido | ❌ Inaccettabile |
| 2 | Validazione in Application Service | Semplice, FluentValidation | Logica fuori dal Domain | ⚠️ OK per input validation |
| 3 | `TryExecute()` (valida + muta) | Always-valid | Viola CQS (muta E ritorna) | ⚠️ Accettabile |
| 4 | `CanExecute()` + `Execute()` | Always-valid + CQS | Due chiamate | ✅ **Preferito** |

### Esempio: Order.Deliver()

```csharp
public class Order : Entity
{
    public Address DeliveryAddress { get; private set; }
    public DayOfWeek DeliveryDay { get; private set; }
    public OrderStatus Status { get; private set; }

    // ═══════════════════════════════════════════════════════
    //  CanDeliver() - QUERY: ritorna errori, non muta stato
    // ═══════════════════════════════════════════════════════
    public IReadOnlyList<string> CanDeliver(Address address, DayOfWeek day)
    {
        var errors = new List<string>();

        if (address == null || address.IsEmpty)
            errors.Add("Delivery address cannot be empty");

        if (day == DayOfWeek.Sunday)
            errors.Add("Cannot deliver on Sunday");

        if (Status != OrderStatus.Confirmed)
            errors.Add("Order must be confirmed before delivery");

        return errors;
    }

    // ═══════════════════════════════════════════════════════
    //  Deliver() - COMMAND: muta stato, lancia se precondizioni falliscono
    // ═══════════════════════════════════════════════════════
    public void Deliver(Address address, DayOfWeek day)
    {
        var errors = CanDeliver(address, day);

        if (errors.Any())
            throw new DomainException($"Cannot deliver: {string.Join(", ", errors)}");

        DeliveryAddress = address;
        DeliveryDay = day;
        Status = OrderStatus.OutForDelivery;

        AddDomainEvent(new OrderDispatchedEvent(Id, address));
    }
}
```

### Come Usarlo nell'Application Layer

```csharp
public class DispatchOrderHandler : IRequestHandler<DispatchOrderCommand, Result<Unit>>
{
    public async Task<Result<Unit>> Handle(DispatchOrderCommand request, ...)
    {
        var order = await _repository.GetByIdAsync(request.OrderId);

        if (order == null)
            return Result<Unit>.Failure("Order not found");

        var address = Address.Create(request.Street, request.City);
        var day = request.DeliveryDay;

        // ═══════════════════════════════════════════════════════
        //  1. Chiama CanDeliver() per ottenere errori user-friendly
        // ═══════════════════════════════════════════════════════
        var errors = order.CanDeliver(address, day);

        if (errors.Any())
            return Result<Unit>.Failure(errors);  // ← User-friendly

        // ═══════════════════════════════════════════════════════
        //  2. Chiama Deliver() - sappiamo che passerà
        // ═══════════════════════════════════════════════════════
        order.Deliver(address, day);

        await _unitOfWork.SaveChangesAsync();

        return Result<Unit>.Success(Unit.Value);
    }
}
```

### Quando CRUD Complica le Cose

Per scenari **task-based** (operazioni specifiche come "Deliver", "Cancel", "Send"):
- ✅ Execute/CanExecute funziona perfettamente
- Gli errori sono chiari: "Cannot deliver on Sunday"

Per scenari **CRUD** (form con molti campi, upload Excel):
- ⚠️ Serve mappare errori ai campi specifici
- Devi arricchire `CanDeliver` con oggetti `Error` che indicano la fonte

```csharp
// Per CRUD: Errori con campo specifico
public record ValidationError(string Field, string Message);

public IReadOnlyList<ValidationError> CanUpdate(UpdateOrderDto dto)
{
    var errors = new List<ValidationError>();

    if (string.IsNullOrEmpty(dto.CustomerName))
        errors.Add(new ValidationError("CustomerName", "Name is required"));

    if (dto.Quantity <= 0)
        errors.Add(new ValidationError("Quantity", "Must be greater than 0"));

    return errors;
}
```

### Nel Nostro Notification Service

```csharp
public class Notification : Entity
{
    // CanSend() - per scenari task-based
    public IReadOnlyList<string> CanSend()
    {
        var errors = new List<string>();

        if (Status != NotificationStatus.Pending)
            errors.Add("Notification already processed");

        if (ScheduledAt < DateTime.UtcNow)
            errors.Add("Scheduled time is in the past");

        return errors;
    }

    public void Send()
    {
        var errors = CanSend();
        if (errors.Any())
            throw new DomainException($"Cannot send: {string.Join(", ", errors)}");

        Status = NotificationStatus.Sent;
        SentAt = DateTime.UtcNow;
        AddDomainEvent(new NotificationSentEvent(Id));
    }
}
```

---

## Always-Valid Domain Model

**Principio:** Le Entity del Domain devono essere **SEMPRE valide**.

### ✅ Giusto

```csharp
public class Order : Entity
{
    private readonly List<OrderItem> _items = new();

    private Order() { }

    public static Order Create(Customer customer, List<OrderItem> items)
    {
        // ═══════════════════════════════════════════════════════
        //  INVARIANT: Order deve avere almeno 1 item
        // ═══════════════════════════════════════════════════════

        if (customer == null)
            throw new DomainException("Customer is required");

        if (items == null || !items.Any())
            throw new DomainException("Order must have at least one item");

        return new Order
        {
            Id = Guid.NewGuid(),
            Customer = customer,
            _items = items,
            Status = OrderStatus.Pending
        };
    }

    // ✅ Impossibile avere Order senza items
    // ✅ Se Order esiste, è valido
}
```

### ❌ Sbagliato

```csharp
public class Order : Entity
{
    public Guid CustomerId { get; set; }
    public List<OrderItem> Items { get; set; }  // ← Può essere null!

    // ❌ Posso creare Order invalido:
    // var order = new Order();  // ← No customer, no items, ma compila!
}
```

---

## Quando Usare Cosa

### ✅ Usa **VALIDATION** (Application) quando:

- Input arriva da **fonte esterna** (utente, API, file, queue)
- Fallimento è **scenario normale** (utente sbaglia)
- Vuoi messaggio **user-friendly** ("La password deve avere almeno 8 caratteri")
- Vuoi ritornare **Result<T>** o **ValidationException**
- Controlli **sintattici** (formato, lunghezza, pattern)

**Esempi:**
- Formato email
- Lunghezza password (8-100 caratteri)
- Data nel futuro (per scheduling)
- File size < 10MB
- Phone number formato italiano

### ✅ Usa **INVARIANT** (Domain) quando:

- Regola definisce l'**essenza** dell'Entity (senza questa, l'Entity non è valida)
- Fallimento è **bug del programmatore**
- Vuoi **fail-fast** con Exception
- Controlli **semantici** (regole di business core)
- La regola deve essere **sempre vera** (invariante = non cambia mai)

**Esempi:**
- Triangle ha 3 lati
- Order ha almeno 1 item
- BankAccount balance >= 0 (se non consente overdraft)
- Email non può essere null (se è required)
- Event SourcedAt <= OccurredAt

---

## Doppia Protezione: Quando Serve?

```
┌─────────────────────────────────────────────────────────────┐
│  Usa ENTRAMBI (Validation + Invariant) quando:              │
├─────────────────────────────────────────────────────────────┤
│  ✅ Regola è CRITICA per il Domain                          │
│  ✅ Input viene da fonte esterna                            │
│  ✅ Vuoi protezione sia da user che da programmer bug       │
│  ✅ Esempio: email obbligatoria, order con items            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Usa SOLO Validation quando:                                │
├─────────────────────────────────────────────────────────────┤
│  ✅ Regola è specifica del caso d'uso (non Domain core)     │
│  ✅ Esempio: "Nome utente deve essere unico" (DB check)     │
│  ✅ Esempio: "Puoi schedulare max 100 notifiche"            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Usa SOLO Invariant quando:                                 │
├─────────────────────────────────────────────────────────────┤
│  ✅ Regola è interna al Domain (nessun input esterno)       │
│  ✅ Esempio: Domain Event SourcedAt viene settato a UtcNow  │
│  ✅ Esempio: Order.Complete() richiede Status == Pending    │
└─────────────────────────────────────────────────────────────┘
```

---

## Casi Complessi

### 🤔 Caso 1: Username Univoco

**Domanda:** È Validation o Invariant?

```csharp
// User con username "john_doe" esiste già.
// Nuovo user vuole username "john_doe".
// Come gestisco?
```

**Risposta:** Dipende!

**Opzione A: Validation (Application)**
```csharp
public class RegisterUserCommandValidator : AbstractValidator<RegisterUserCommand>
{
    private readonly IUserRepository _userRepository;

    public RegisterUserCommandValidator(IUserRepository repository)
    {
        _userRepository = repository;

        RuleFor(x => x.Username)
            .MustAsync(async (username, cancellation) =>
            {
                var exists = await _userRepository.ExistsByUsernameAsync(username);
                return !exists;
            })
            .WithMessage("Username already taken");  // ← User-friendly
    }
}

// ✅ Giusto perché:
// - È input esterno (user sceglie username)
// - Richiede DB check (dipendenza esterna)
// - Messaggio user-friendly
```

**Opzione B: Domain Event + Eventual Consistency**
```csharp
public class User : Entity
{
    public Username Username { get; private set; }

    public static User Create(Username username, ...)
    {
        if (username == null)
            throw new DomainException("Username is required");  // ← Invariant

        // NON controllo unicità qui (DB check)
        // Invece, lancia evento

        var user = new User { Username = username, ... };
        user.AddDomainEvent(new UserCreatedEvent(user.Id, username));

        return user;
    }
}

// Event Handler verifica unicità in modo asincrono
// Se username duplicato → rollback o chiedi altro username
```

**Consiglio:** Per username univoco → **Validation** (più semplice).

---

### 🤔 Caso 2: Race Condition

**Scenario:** Due richieste concorrenti creano User con stesso username.

```
Request 1: RegisterUser("john_doe") → Validation passa → Crea User
Request 2: RegisterUser("john_doe") → Validation passa → Crea User
                                      ↑
                            Entrambi passano validation!
```

**Soluzione:** Unique Index nel DB + retry logic.

```csharp
// Application Layer
public class RegisterUserHandler : IRequestHandler<RegisterUserCommand, Result<Guid>>
{
    public async Task<Result<Guid>> Handle(...)
    {
        // 1. Validation passa (async check)
        var username = Username.Create(command.Username);
        var user = User.Create(username, ...);

        try
        {
            await _repository.AddAsync(user);
            await _unitOfWork.SaveChangesAsync();  // ← Può fallire per unique constraint
        }
        catch (DbUpdateException ex) when (ex.IsUniqueConstraintViolation())
        {
            // 2. Race condition catturata dal DB
            return Result<Guid>.Failure("Username already taken");
        }

        return Result<Guid>.Success(user.Id);
    }
}
```

**Lezione:** Validation può fallire per race condition. DB è source of truth.

---

## Collegamenti

- [[always-valid-domain-model]] - Principio fondamentale DDD
- [[value-objects]] - Invariants nei Value Objects
- [[result-pattern]] - Come ritornare validation errors
- [[domain-exceptions]] - Quando lanciare eccezioni nel Domain
- [[mediatr-pipeline-behaviors]] - Validation con FluentValidation
- [[clean-architecture-principles]] - Separation of concerns

---

## Quiz

### Q1: Email Obbligatoria - Dove Mettere il Controllo?

Hai una `Notification` entity che richiede email obbligatoria. Dove metti il controllo?

A) Solo Application Layer (FluentValidation)
B) Solo Domain Layer (costruttore privato)
C) Entrambi (doppia protezione)
D) Dipende dal caso d'uso

<details>
<summary>Risposta</summary>

**C) Entrambi (doppia protezione)**

**Application Layer (Validation):**
```csharp
RuleFor(x => x.RecipientEmail)
    .NotEmpty()
    .WithMessage("Email is required");  // User-friendly
```
→ Protegge da input utente sbagliato (form, API)

**Domain Layer (Invariant):**
```csharp
public class Email : ValueObject
{
    public static Email Create(string value)
    {
        if (string.IsNullOrWhiteSpace(value))
            throw new DomainException("Email cannot be empty");  // Fail-fast
    }
}
```
→ Protegge da programmatore che usa male il Domain

**Perché entrambi?**
- Application → Scenario normale (user sbaglia)
- Domain → Protezione interna (programmatore sbaglia)

</details>

---

### Q2: Invariant o Validation?

Per ognuno di questi, decidi se è **Invariant** (Domain) o **Validation** (Application):

1. "Triangle deve avere 3 lati"
2. "Password deve avere almeno 8 caratteri"
3. "Order deve avere almeno 1 item"
4. "Username deve essere univoco"
5. "BankAccount balance >= 0" (no overdraft)

<details>
<summary>Risposta</summary>

1. **Invariant** - Definisce l'essenza di Triangle (senza 3 lati, non è un triangolo)
2. **Validation** - Controllo sintattico su input utente (può essere 7 o 9, ma policy dice 8)
3. **Invariant** - Order senza items non ha senso nel Domain
4. **Validation** - Richiede DB check, input esterno, scenario normale che fallisce
5. **Invariant** - Regola di business core che definisce BankAccount (se no overdraft)

**Nota:** Alcuni sono borderline. Username univoco potrebbe essere anche Invariant se il Domain lo richiede assolutamente.

</details>

---

### Q3: Cosa C'è di Sbagliato?

```csharp
public class User : Entity
{
    public string Email { get; set; }
    public string Password { get; set; }

    public User() { }  // Costruttore pubblico senza parametri

    public void SetEmail(string email)
    {
        Email = email;  // Nessun controllo
    }
}
```

Identifica i problemi con il principio "Always-Valid Domain Model".

<details>
<summary>Risposta</summary>

**Problemi:**

1. **Costruttore pubblico senza parametri**
   - ❌ Posso creare `new User()` senza email/password
   - ✅ Dovrebbe essere `private` (per EF Core) + factory method `Create()`

2. **Setter pubblico senza controlli**
   - ❌ `SetEmail(null)` o `SetEmail("")` invalida l'Entity
   - ✅ Dovrebbe avere guard clause o usare Value Object `Email`

3. **Proprietà string invece di Value Object**
   - ❌ Email può contenere qualsiasi stringa (anche "not-an-email")
   - ✅ Dovrebbe essere `Email` Value Object con invariants

4. **Nessuna invariant**
   - ❌ User può esistere in stato invalido
   - ✅ Dovrebbe avere invariants nel costruttore/factory

**Versione corretta:**

```csharp
public class User : Entity
{
    public Email Email { get; private set; }
    public Password Password { get; private set; }

    private User() { }  // EF Core only

    public static User Create(Email email, Password password)
    {
        if (email == null)
            throw new DomainException("Email is required");

        if (password == null)
            throw new DomainException("Password is required");

        return new User { Email = email, Password = password };
    }

    public void ChangeEmail(Email newEmail)
    {
        if (newEmail == null)
            throw new DomainException("Email is required");

        Email = newEmail;
        AddDomainEvent(new UserEmailChangedEvent(Id, newEmail));
    }
}
```

</details>

---

## Risorse per Approfondire

- **📝 [Vladimir Khorikov - Validations vs Invariants](https://khorikov.org/posts/2022-06-06-validation-vs-invariants/)** - Articolo originale
- **📝 [Vladimir Khorikov - Always-Valid Domain Model](https://vkhorikov.medium.com/always-valid-domain-model-706e5f3d24b0)** - Principio fondamentale
- **📝 [Vladimir Khorikov - Validation and DDD](https://enterprisecraftsmanship.com/posts/validation-and-ddd/)** - Approfondimento completo
- **📖 [Domain-Driven Design - Eric Evans](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)** - Il libro fondamentale

---

### Q4: Execute/CanExecute - Perché Non TryExecute?

Un collega propone di usare `TryDeliver()` che ritorna `bool` e muta lo stato se valido.

Qual è il problema principale di questo approccio rispetto a `CanDeliver()` + `Deliver()`?

<details>
<summary>Risposta</summary>

**Viola CQS (Command-Query Separation)**

`TryDeliver()` fa due cose:
1. **Query:** Controlla se può consegnare (ritorna bool)
2. **Command:** Muta lo stato se valido

CQS dice: un metodo deve fare UNA cosa - o ritornare dati (query) o mutare stato (command), mai entrambi.

Con Execute/CanExecute:
- `CanDeliver()` → pura query (ritorna errori, non muta)
- `Deliver()` → puro command (muta stato, lancia se fallisce)

**Trade-off:** TryExecute è accettabile se CQS non è prioritario, ma Execute/CanExecute è più pulito.

</details>

---

### Q5: CRUD vs Task-Based

Stai implementando un form di modifica ordine con 10 campi. Quale approccio scegli per la validazione nel Domain?

A) `CanUpdate()` + `Update()` con lista di stringhe
B) `CanUpdate()` + `Update()` con oggetti `ValidationError(Field, Message)`
C) Solo FluentValidation in Application Layer
D) `TryUpdate()` che ritorna `Result<Unit>`

<details>
<summary>Risposta</summary>

**B) `CanUpdate()` + `Update()` con oggetti `ValidationError(Field, Message)`**

Per scenari CRUD con molti campi:
- Devi **mappare errori ai campi specifici** per la UI
- "Nome obbligatorio" deve indicare QUALE campo
- Serve arricchire gli errori con il campo sorgente

```csharp
public record ValidationError(string Field, string Message);

public IReadOnlyList<ValidationError> CanUpdate(...)
{
    var errors = new List<ValidationError>();
    if (string.IsNullOrEmpty(name))
        errors.Add(new ValidationError("CustomerName", "Required"));
    return errors;
}
```

**Perché non C (solo FluentValidation)?**
Se la logica è Domain (invariants), deve stare nel Domain, non solo in Application.

</details>

---

*Nota creata da Dan il 2026-02-26, aggiornata il 2026-02-28 con Execute/CanExecute pattern*
