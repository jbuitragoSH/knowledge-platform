from enum import StrEnum


class WorkflowStatus(StrEnum):
    BACKLOG = "Backlog"

    READY = "Ready"

    IN_PROGRESS = "In Progress"

    REVIEW = "Review"

    TESTING = "Testing"

    DONE = "Done"
