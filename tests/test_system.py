from src.main import Command, IdempotencyStore, Worker, retry


def test_idempotency():
    worker = Worker(IdempotencyStore())
    command = Command("1", "payload")
    assert worker.process(command).startswith("PROCESSED")
    assert worker.process(command) == "DUPLICATE"


def test_retry():
    state = {"attempts": 0}

    def operation():
        state["attempts"] += 1
        if state["attempts"] < 2:
            raise RuntimeError("temporary")
        return "ok"

    assert retry(operation) == "ok"
    assert state["attempts"] == 2
