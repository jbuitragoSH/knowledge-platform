from .error import Error


class DomainErrors:
    ENTITY_NOT_FOUND = Error(
        code="ENTITY_NOT_FOUND",
        message="The requested entity does not exist.",
    )

    DUPLICATED_ENTITY = Error(
        code="DUPLICATED_ENTITY",
        message="The entity already exists.",
    )

    INVALID_IDENTIFIER = Error(
        code="INVALID_IDENTIFIER",
        message="The identifier is invalid.",
    )

    VALIDATION_ERROR = Error(
        code="VALIDATION_ERROR",
        message="The domain validation failed.",
    )
