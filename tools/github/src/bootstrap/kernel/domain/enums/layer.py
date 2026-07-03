from enum import StrEnum


class Layer(StrEnum):
    DOMAIN = "Domain"

    APPLICATION = "Application"

    INFRASTRUCTURE = "Infrastructure"

    API = "API"

    PERSISTENCE = "Persistence"

    TESTING = "Testing"
