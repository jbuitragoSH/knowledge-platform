from bootstrap.kernel.domain.entity_id import EntityId


def test_generate_returns_entity_id():
    entity_id = EntityId.generate()

    assert isinstance(entity_id, EntityId)


def test_generate_creates_unique_ids():
    first = EntityId.generate()

    second = EntityId.generate()

    assert first != second
