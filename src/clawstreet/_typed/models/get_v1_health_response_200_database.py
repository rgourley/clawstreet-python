from enum import StrEnum


class GetV1HealthResponse200Database(StrEnum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
