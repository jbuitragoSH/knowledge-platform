from dataclasses import dataclass

from bootstrap.kernel.domain.entity import Entity
from bootstrap.kernel.domain.entity_id import EntityId


@dataclass
class User(Entity):
    pass


def test_entity_has_identity():
    user = User(id=EntityId.generate())

    assert user.id is not None


def test_entities_with_same_id_are_equal():
    entity_id = EntityId.generate()

    user1 = User(id=entity_id)

    user2 = User(id=entity_id)

    assert user1 == user2
