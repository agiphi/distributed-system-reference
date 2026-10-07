from distributed_system.commands import Command
from distributed_system.idempotency import IdempotencyStore
from distributed_system.retry import retry


def test_command_has_identity():
    command=Command("example", {"value":1})
    assert command.id


def test_idempotency_claim_is_repeatable():
    store=IdempotencyStore()
    assert store.claim("cmd-1") is True
    assert store.claim("cmd-1") is False


def test_retry_recovers_from_transient_failure():
    state={"attempts":0}
    def operation():
        state["attempts"]+=1
        if state["attempts"]<2:
            raise RuntimeError("temporary")
        return "ok"
    assert retry(operation)=="ok"
    assert state["attempts"]==2
