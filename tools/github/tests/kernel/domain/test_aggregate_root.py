from dataclasses import dataclass

from bootstrap.kernel.domain.aggregate_root import AggregateRoot
from bootstrap.kernel.domain.entity_id import EntityId


@dataclass
class Project(AggregateRoot):
    pass


def test_aggregate_root_is_entity():
    project = Project(id=EntityId.generate())

    assert isinstance(project, AggregateRoot)
