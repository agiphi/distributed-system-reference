from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    command_id: str
    payload: str


class IdempotencyStore:
    def __init__(self):
        self._completed: set[str] = set()

    def seen(self, command_id: str) -> bool:
        return command_id in self._completed

    def mark_complete(self, command_id: str) -> None:
        self._completed.add(command_id)


class Worker:
    def __init__(self, store: IdempotencyStore):
        self.store = store

    def process(self, command: Command) -> str:
        if self.store.seen(command.command_id):
            return "DUPLICATE"

        self.store.mark_complete(command.command_id)
        return f"PROCESSED:{command.payload}"


def retry(operation, attempts: int = 3):
    last_error = None
    for _ in range(attempts):
        try:
            return operation()
        except Exception as exc:
            last_error = exc
    raise last_error


def main() -> None:
    worker = Worker(IdempotencyStore())
    command = Command("cmd-001", "example")
    print(worker.process(command))
    print(worker.process(command))


if __name__ == "__main__":
    main()
