---
tags: [senior-engineer, project, p1.5, security]
status: locked
duration: 1 week
---

# 🔐 Progetto 1.5: Auth & Security

## 📋 Overview
Implementare autenticazione JWT da zero. Capire cosa fa Azure AD B2C "under the hood".

**Durata:** 1 settimana | **Focus:** JWT, Security, OWASP

---

## 🎯 Obiettivo
Colmare il gap security. Capire come funziona l'autenticazione internamente.

---

## 🛠️ Stack
- .NET 8 Web API
- JWT Bearer Authentication
- BCrypt password hashing
- Refresh tokens in Redis

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| JWT Structure | Header, Payload, Signature |
| Token Types | Access tokens vs Refresh tokens |
| Password Security | BCrypt (mai SHA/MD5!) |
| Refresh Flow | Token rotation in Redis |
| OWASP Top 10 | Awareness delle vulnerabilità comuni |
| Rate Limiting | Protezione brute force su login |

---

## 🎨 Patterns

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Token Pattern** | Stateless authentication |
| **Decorator** | Aggiunge auth a qualsiasi handler |

---

## 📅 Piano Settimana

**Days 1-2: JWT From Scratch**
```csharp
// Capisci COME funziona JWT
public string GenerateToken(User user)
{
    var claims = new[]
    {
        new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()),
        new Claim(ClaimTypes.Email, user.Email),
        new Claim(ClaimTypes.Role, user.Role)
    };

    var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_config["Jwt:Secret"]));
    var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

    var token = new JwtSecurityToken(
        issuer: _config["Jwt:Issuer"],
        audience: _config["Jwt:Audience"],
        claims: claims,
        expires: DateTime.UtcNow.AddMinutes(15), // Short-lived!
        signingCredentials: credentials
    );

    return new JwtSecurityTokenHandler().WriteToken(token);
}
```

**Days 3-4: Refresh Tokens + Redis**
```csharp
// Refresh token in Redis con expiry
public async Task<string> CreateRefreshToken(Guid userId)
{
    var refreshToken = Convert.ToBase64String(RandomNumberGenerator.GetBytes(64));

    await _redis.SetStringAsync(
        $"refresh:{refreshToken}",
        userId.ToString(),
        new DistributedCacheEntryOptions
        {
            AbsoluteExpirationRelativeToNow = TimeSpan.FromDays(7)
        });

    return refreshToken;
}
```

**Day 5: OWASP Checklist**
- [ ] SQL Injection → Parameterized queries (EF Core OK)
- [ ] XSS → Input validation, output encoding
- [ ] CSRF → Anti-forgery tokens
- [ ] Broken Auth → Secure password policy
- [ ] Sensitive Data → HTTPS, no secrets in code
- [ ] Rate Limiting → Per IP/User

---

## 📦 Deliverables

- [ ] JWT authentication funzionante
- [ ] Refresh token rotation
- [ ] Password hashing con BCrypt
- [ ] Rate limiting su login (5 tentativi/minuto)
- [ ] OWASP checklist completata
- [ ] 20+ security-focused tests

---

## 🔗 Come Rinforza Architect

```
ARCHITECT P2: Azure AD B2C (managed)    SENIOR P1.5: JWT (custom)
─────────────────────────────────────────────────────────────
"Configura Azure AD B2C"          →    "Implementa JWT da zero"
"Usa token forniti"               →    "Genera e valida token"
"Managed refresh"                 →    "Scrivi refresh logic"

RISULTATO: Capisci COSA fa Azure AD B2C internamente
```

---

## 🏆 Boss Battle: "API Key Management"

**Scenario:** Implementa un sistema di API key per third-party access.

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per API key storage (hashed vs encrypted) |
| **B. Implementazione** | Generate, revoke, rotate API keys + rate limiting per key |
| **C. Testing** | Security tests (key leak, brute force protection) |
| **D. Performance** | Key validation < 5ms (Redis lookup) |

---

*Ultimo aggiornamento: 2026-03-04*
