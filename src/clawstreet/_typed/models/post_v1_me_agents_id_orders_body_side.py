from enum import StrEnum


class PostV1MeAgentsIdOrdersBodySide(StrEnum):
    BUY = "buy"
    COVER = "cover"
    SELL = "sell"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
