import pytest
from distributed_system.idempotency import IdempotencyStore
from distributed_system.retry import retry


def test_duplicate_claim_is_rejected():
    store=IdempotencyStore()
    assert store.claim("x") is True
    assert store.claim("x") is False


def test_retry_exhaustion_surfaces_failure():
    def fail():
        raise RuntimeError("downstream unavailable")
    with pytest.raises(RuntimeError, match="downstream unavailable"):
        retry(fail, attempts=2)


def test_retry_rejects_invalid_attempt_count():
    with pytest.raises(ValueError):
        retry(lambda: None, attempts=0)
