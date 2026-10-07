from dataclasses import dataclass
from uuid import uuid4

@dataclass(frozen=True)
class Command:
    name: str
    payload: dict
    id: str = ""

    def __post_init__(self):
        if not self.id: object.__setattr__(self, "id", str(uuid4()))
