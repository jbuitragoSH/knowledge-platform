from dataclasses import dataclass, field

from .domain_event import DomainEvent
from .entity import Entity


@dataclass(eq=False)
class AggregateRoot(Entity):
    _events: list[DomainEvent] = field(default_factory=list, init=False)
