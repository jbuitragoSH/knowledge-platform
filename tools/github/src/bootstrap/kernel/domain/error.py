from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Error:
    code: str

    message: str
