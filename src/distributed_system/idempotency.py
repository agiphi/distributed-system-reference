class IdempotencyStore:
    def __init__(self):
        self._seen=set()

    def claim(self, command_id):
        if command_id in self._seen:
            return False
        self._seen.add(command_id)
        return True
