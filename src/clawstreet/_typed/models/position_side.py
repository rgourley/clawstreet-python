from enum import StrEnum


class PositionSide(StrEnum):
    LONG = "long"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
