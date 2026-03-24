# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Learning Hub is a gamified personal learning system built as an Obsidian vault. It tracks Dan's progression from mid-level to AI Engineer (primary target) + Senior/Staff Engineer across two parallel career tracks, with Claude as AI tutor. All content is in Italian (explanations) and English (code).

## Session Protocol

Use `/init` to start a session, `/quiz` for spaced repetition, `/nota` for atomic notes, `/end` to close, `/refactor` for project health check. All skills are in `.claude/skills/`. The full tutoring rules live in `claude/CLAUDE.md`.

## Repository Structure

- **`claude/`** — Tutor state and context (CLAUDE.md, current-state.md, WHY.md, roadmaps/, context/, sessions/)
- **`Knowledge/`** — Atomic notes written during Sedimentazione phase. Index at `Knowledge/CLAUDE.md`
- **`Exams/`** — Assessment records
- **`.claude/`** — Claude Code config: skills (init, quiz, end, nota, ask, exam, context, refactor), hooks (validate-note.sh), settings
- **`coach.py`** — Local Ollama-based CLI coach (Python 3, requires `ollama`, `pyyaml`, `rich`)

Production code projects live in `../../Projects/`:
- `Projects/notification-service/` — Architect Quest P1 (.NET 8 microservice)
- `Projects/TaskManager/` — Senior Engineer P1 (.NET 8, Clean Architecture, TDD)

## Build & Test Commands (.NET Projects)

```bash
# Build
dotnet build

# Run all tests
dotnet test

# Run a single test project
dotnet test path/to/Tests.csproj

# Run tests with filter
dotnet test --filter "FullyQualifiedName~ClassName.MethodName"

# EF Core migrations
dotnet ef migrations add MigrationName -p src/Infrastructure -s src/Api
dotnet ef database update -p src/Infrastructure -s src/Api

# Docker Compose (for integration tests with Testcontainers)
docker compose up -d
```

## .NET Architecture Pattern

All .NET projects follow Clean Architecture with 4 layers:

```
Domain (innermost) → Application → Infrastructure → API (outermost)
```

- **Domain**: Entities with behavior (Rich Domain Model), Value Objects, Domain Events, repository interfaces (ports). No external dependencies.
- **Application**: MediatR Commands/Queries (CQRS), FluentValidation validators, Pipeline Behaviors. Depends only on Domain.
- **Infrastructure**: EF Core DbContext, repository implementations (adapters), external service clients. Implements Domain interfaces.
- **API**: Minimal API endpoints or Controllers, DI composition root. References all layers.

Key constraints: interfaces live in Domain/Application (not Infrastructure), repositories never call SaveChanges (Unit of Work pattern), TDD is mandatory on the Senior Engineer path.

## Hooks

- **PostToolUse (Write)**: `.claude/hooks/validate-note.sh` blocks writes to `Knowledge/**/*.md` that lack required sections (frontmatter with tags/created/source, Cos'è, Quando usarlo, Quiz with 3+ questions)
- **Stop**: Prompt-based reminder to use `/end` before closing

## Key Files to Read

| When | Read |
|------|------|
| First session | `claude/profile.md`, `claude/WHY.md`, `claude/current-state.md` |
| Every session | `claude/current-state.md`, `claude/context/quiz-tracker.md` |
| Creating notes | `Knowledge/CLAUDE.md` (template + tag schema) |
| XP/gamification | `claude/context/gamification.md` |
| Tech decisions | `claude/context/tech-stack.md` |
