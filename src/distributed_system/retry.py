def retry(operation, attempts=3):
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last=None
    for _ in range(attempts):
        try:
            return operation()
        except Exception as exc:
            last=exc
    raise last
