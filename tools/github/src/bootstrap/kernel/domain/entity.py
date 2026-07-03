from abc import ABC
from dataclasses import dataclass

from .entity_id import EntityId


@dataclass(eq=False)
class Entity(ABC):
    id: EntityId

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
