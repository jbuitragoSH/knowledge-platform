from dataclasses import dataclass
from typing import Self

from .error import Error


@dataclass(frozen=True, slots=True)
class Result[T]:
    success: bool
    value: T | None = None
    error: Error | None = None

    @classmethod
    def ok(cls, value: T | None = None) -> Self:
        return cls(success=True, value=value)

    @classmethod
    def fail(cls, error: Error) -> Self:
        return cls(success=False, error=error)
