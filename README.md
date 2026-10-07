# Distributed System Reference

**Public Reference Implementation — No Proprietary IP**

A local-first Python reference implementation of production-oriented distributed-system patterns, focused on boundaries and failure behavior rather than framework complexity.

## Architecture

`Request → Command Boundary → Idempotency → Queue → Worker → Persistence/Event`

## Demonstrated patterns

- explicit command identity
- asynchronous local queue boundary
- idempotency control
- retry and failure exhaustion
- dependency-light execution
- deterministic tests for failure paths

## Scope

Synthetic/local behavior only. No proprietary production architecture, credentials, cloud resources, or private operational configuration is included. This repository is independent technical evidence.

## Run

`python -m pytest -q`

## Architecture

```mermaid
flowchart LR
  A[Request] --> B[Command Boundary]
  B --> C[Idempotency]
  C --> D[Queue]
  D --> E[Worker]
  E --> F[Persistence / Event]
```
