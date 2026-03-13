# Tech Stack

## Backend
| Tecnologia | Versione | Note |
|------------|----------|------|
| .NET | 8 | NON versioni precedenti |
| C# | 12 | |
| Entity Framework Core | 8 | |
| MediatR | Latest | Per CQRS |
| FluentValidation | Latest | |
| AutoMapper | Latest | |
| Serilog | Latest | Logging |
| Polly | Latest | Resilience |
| MassTransit | Latest | Message bus, Sagas |

## Frontend
| Tecnologia | Note |
|------------|------|
| React 18 | |
| TypeScript | Strict mode |
| Redux Toolkit | NON Zustand! Dan lo conosce gia |
| RTK Query | API calls |
| React Hook Form + Zod | Forms |
| Tailwind CSS | Styling |
| Vite | Build tool |

## Data
| Tecnologia | Uso |
|------------|-----|
| SQL Server | Primary DB (Senior path) |
| PostgreSQL | Primary DB (Architect path) |
| Redis | Caching → Pub/Sub → Primary DB |
| Marten | Event Sourcing .NET |
| Elasticsearch | Full-text search |

## Infrastructure
| Tecnologia | Uso |
|------------|-----|
| Docker | Containerization |
| Docker Compose | Local development |
| Kubernetes | Production (AKS) |
| Helm | K8s packaging |
| Terraform | Infrastructure as Code |
| GitHub Actions | CI/CD |

## Messaging
| Tecnologia | Uso |
|------------|-----|
| Azure Service Bus | Production |
| RabbitMQ | Local dev |
| Redis Streams | Event streaming |

## Observability
| Tecnologia | Uso |
|------------|-----|
| OpenTelemetry | Instrumentation |
| Prometheus + Grafana | Metrics + Dashboards |
| Jaeger | Distributed tracing |
| Serilog + Seq | Logging |

## Testing
| Tecnologia | Uso |
|------------|-----|
| xUnit | Test framework |
| FluentAssertions | Assertions |
| Moq | Mocking |
| Testcontainers | Integration tests |
| k6 | Load testing |

---

*Aggiornato: 2026-03-13*
