from dataclasses import dataclass
from typing import Self
from uuid import uuid4

from .value_object import ValueObject


@dataclass(frozen=True, slots=True)
class EntityId(ValueObject):
    value: str

    @classmethod
    def generate(cls) -> Self:
        return cls(str(uuid4()))
