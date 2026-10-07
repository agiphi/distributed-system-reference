# Distributed System Reference

A local-first reference implementation of production-oriented distributed-system patterns.

The repository focuses on boundaries and failure behavior rather than framework complexity.

## Demonstrated patterns

- service boundaries
- asynchronous work
- retries
- idempotency
- durable local state
- health checks
- explicit failure handling

## Architecture

`Request → Command Boundary → Idempotency Check → Queue → Worker → Persistence → Event`

The implementation is dependency-light and runnable locally.

## Run

```bash
python -m src.main
```

## Design goals

- make failure states explicit
- prevent duplicate processing
- keep components independently testable
- make operational state observable
- avoid unnecessary infrastructure dependencies
