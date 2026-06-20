from enum import Enum


class GetV1HealthResponse200Database(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
