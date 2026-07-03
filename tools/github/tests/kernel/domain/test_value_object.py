from dataclasses import dataclass

from bootstrap.kernel.domain.value_object import ValueObject


@dataclass(frozen=True)
class Money(ValueObject):
    amount: int


def test_value_object_compares_by_value():
    a = Money(amount=100)

    b = Money(amount=100)

    assert a == b
