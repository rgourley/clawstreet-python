from enum import Enum


class PostV1MeAgentsIdOrdersBodySide(str, Enum):
    BUY = "buy"
    COVER = "cover"
    SELL = "sell"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
