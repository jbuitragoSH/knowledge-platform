from bootstrap.kernel.domain.error import Error


class ProjectErrors:
    DUPLICATED_LABEL = Error(
        code="PROJECT_DUPLICATED_LABEL",
        message="A label with the same name already exists.",
    )

    DUPLICATED_MILESTONE = Error(
        code="PROJECT_DUPLICATED_MILESTONE",
        message="A milestone with the same title already exists.",
    )

    INVALID_ARCHITECTURE_REFERENCE = Error(
        code="INVALID_ARCHITECTURE_REFERENCE",
        message="The architecture reference is invalid.",
    )

    CIRCULAR_DEPENDENCY = Error(
        code="CIRCULAR_DEPENDENCY",
        message="Circular dependency detected.",
    )
