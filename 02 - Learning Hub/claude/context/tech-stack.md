# Tech Stack

> Stack di riferimento per i progetti del Learning Hub. **Stack primario .NET-first**, con AI tooling in espansione e awareness su altri linguaggi (Java/Python/Node) lasciata al pickup on-the-job.

## Backend (Primario)
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

## Backend (Secondario — solo se progetto AI lo richiede)
| Tecnologia | Versione | Note |
|------------|----------|------|
| Python | 3.11+ | **Solo per Python AI Bridge Project** (FastAPI + LangGraph). NO modulo "studia Python" — pickup on-the-job |
| FastAPI | Latest | Web framework Python per AI services |
| Pydantic | v2 | Validation Python |
| SQLAlchemy | Latest | ORM Python (per AI Bridge) |

> **Filosofia stack secondario:** Java/Spring Boot e Node/TS BE non sono "must learn upfront". Si imparano on-the-job se richiesto dal cluster target. Concentrarsi sui **concetti universali** (DDD, CQRS, EDA, Clean Arch) trasferibili in 2-4 settimane sul lavoro reale.

## Frontend
| Tecnologia | Note |
|------------|------|
| React 18-19 | Concurrent features, Server Components (Next.js) |
| TypeScript | Strict mode, branded types, well-modeled domain |
| Redux Toolkit | NON Zustand! Dan lo conosce gia |
| RTK Query | API calls |
| React Hook Form + Zod | Forms |
| Tailwind CSS | Styling |
| Vite | Build tool |
| Next.js | 15 App Router + Server Components (per P4, P6) |
| Storybook | 8+ — design system docs (per P3) |
| shadcn/ui + Radix UI | Componenti accessibili (per P1, P3) |

## Frontend Testing & Quality
| Tecnologia | Uso |
|------------|-----|
| Vitest | Unit + integration testing moderno |
| Playwright | E2E + visual regression |
| Testing Library | Component testing user-centric |
| MSW | Mock Service Worker (API mocking) |
| Chromatic | Visual regression hosted (Storybook) |

## Data Visualization (per P2 + Cluster #6 Data-Heavy AI FE)
| Tecnologia | Uso |
|------------|-----|
| Recharts / Tremor | Entry-level, declarative-based |
| D3.js | Low-level mastery |
| Visx (Airbnb) | D3 + React pattern |
| TanStack Virtual | Virtualization liste/tabelle large |

## Data
| Tecnologia | Uso |
|------------|-----|
| SQL Server | Primary DB (Senior path) |
| PostgreSQL | Primary DB (Architect path) |
| Redis | Caching → Pub/Sub → Distributed locks → Primary DB |
| Marten | Event Sourcing .NET |
| Elasticsearch | Full-text search |
| pgvector | Vector search (extension Postgres, per RAG) |

## Vector DB (AI/RAG)
| Tecnologia | Uso |
|------------|-----|
| pgvector | Default — già in stack Postgres |
| Qdrant | Awareness — quando vector DB dedicato batte embedded |
| Pinecone | Awareness — managed serverless |
| Weaviate / Chroma | Awareness |

## AI Stack 🤖 (NUOVO — espansione 2026-04-23)
| Tecnologia | Uso |
|------------|-----|
| **Claude API** | Cloud LLM provider primario (Anthropic SDK .NET + Python) |
| **Ollama** | LLM locale (Llama 3.1, Mistral, Phi) per fast intent + privacy |
| **MCP Protocol** | Model Context Protocol — estendi Claude/agenti con tool custom |
| **LangChain + LangGraph** | Agent frameworks production (Python, primario) |
| **LiteLLM** | Multi-provider LLM proxy (alternativa custom IAIProvider) |
| **Hugging Face Transformers** | Awareness — model loading, fine-tuning |
| **Vercel AI SDK** | Streaming UI + chat patterns (per FE P6 AI-Native) |
| **Ragas + DeepEval** | Evaluation pipelines AI (faithfulness, answer_relevancy) |
| **Langfuse** | Observability LLM (tracing, eval, dataset management) |
| **Anthropic SDK** | .NET + TypeScript + Python clients |

### AI Coding Tools (mastery richiesta — cluster #4 AI-Augmented SWE)
| Tool | Note |
|------|------|
| **Claude Code** | Cert ottenuta ✅ (8/8 Perfect Score 2026-03-13) |
| **Cursor** | AI-first IDE (composer, agent mode, .cursorrules) |
| **GitHub Copilot** | Pair programming AI |
| **Windsurf** | Codeium AI IDE (awareness) |

## Infrastructure
| Tecnologia | Uso |
|------------|-----|
| Docker | Containerization |
| Docker Compose | Local development |
| Kubernetes | Production (AKS / EKS / GKE) |
| Helm | K8s packaging |
| **Terraform** | Infrastructure as Code (primario) |
| **Pulumi** | IaC awareness (.NET-friendly, scrivi infra in C#) |
| **GitHub Actions** | CI/CD primario |
| **Azure DevOps Pipelines** | CI/CD enterprise alt (awareness) |

## Cloud Providers (1 hands-on, altri awareness)
| Provider | Uso |
|----------|-----|
| **Azure** | Primario (AKS, Service Bus, Cosmos DB, App Service, Functions, Container Apps, .NET Aspire) — coerente con AZ-204 cert (Tier 1) + AZ-400 cert opzionale (Tier 2) |
| **AWS** | Awareness — Lambda, ECS, SQS, SNS, DynamoDB, RDS, S3, EventBridge, Bedrock |
| **GCP** | Awareness — Cloud Run, Cloud Functions, Pub/Sub, Firestore, Cloud SQL, Vertex AI |

## Messaging
| Tecnologia | Uso |
|------------|-----|
| Azure Service Bus | Production (Azure-native) |
| RabbitMQ | Local dev + on-prem |
| Apache Kafka | Awareness — fintech standard (NatWest, Spotify) |
| Redis Streams | Event streaming lightweight |
| Redis Pub/Sub | Messaging in-process |

## Observability (M-T2 Modern Observability Stack)
| Tecnologia | Uso |
|------------|-----|
| **OpenTelemetry** | Vendor-neutral instrumentation (traces + metrics + logs) |
| **Prometheus + Grafana** | Metrics + dashboards |
| **Jaeger / Tempo** | Distributed tracing |
| **ELK Stack** | Awareness — Elasticsearch + Logstash + Kibana |
| **New Relic** | Awareness (cluster #2/#7 mercato) |
| Serilog + Seq | Logging .NET locale |
| Loki | Log aggregation cloud-native (awareness) |

## Identity Standards (M-T7 Enterprise Identity)
| Tecnologia | Uso |
|------------|-----|
| **JWT** | Custom implementation (P1.5) |
| **OAuth 2.0 + OIDC** | Enterprise auth standard |
| **SAML 2.0** | Awareness (SP-initiated SSO) |
| **SCIM** | Awareness (user provisioning) |
| **Auth0 / Keycloak** | IdP managed (almeno 1 hands-on) |

## Testing
| Tecnologia | Uso |
|------------|-----|
| xUnit | Test framework .NET |
| FluentAssertions | Assertions |
| NSubstitute | Mocking |
| Testcontainers | Integration tests |
| k6 / NBomber | Load testing |
| Vitest + Playwright | Frontend (vedi sezione FE Testing) |

## Mobile (Senior Frontend P5)
| Tecnologia | Uso |
|------------|-----|
| Flutter 3.x | iOS + Android single codebase |
| Riverpod | State management |
| Drift | Local DB SQLite |
| go_router | Navigation |

---

## Filosofia Stack

1. **Stack primario stabile**: .NET 8 + C# 12 + React/TypeScript = base solida tutti i progetti.
2. **Stack secondario on-the-job**: Java/Spring Boot, Node/TS BE = si imparano sul lavoro se cluster target lo richiede. Non investire upfront.
3. **AI stack in espansione**: ogni nuovo annuncio "must-have" porta a valutazione hands-on (es. LangGraph + MCP entrati 2026-04-23).
4. **Cloud primario Azure** (cert AZ-204 + Terraform in Tier 1 roadmap, vedi `career-strategy.md` > Certification Roadmap), AWS/GCP awareness sufficiente per most cluster (Tier 3 future).
5. **DevOps moderno = standard**: Docker + K8s + Terraform + GitHub Actions + OpenTelemetry sono baseline 2026, non opzionali.

---

*Aggiornato: 2026-05-07 (refactor — Azure cert riferimento aggiornato AZ-305→AZ-204+AZ-400 dopo decisione Certification Roadmap; Container Apps + .NET Aspire aggiunti allo stack Azure)*

*Versione precedente: 2026-04-23 (v2.0 — refactor post job-postings enrichment: aggiunti AI Stack + Identity Standards + Modern Observability + Frontend Testing/Viz + Cloud Awareness + filosofia "stack secondario on-the-job")*
