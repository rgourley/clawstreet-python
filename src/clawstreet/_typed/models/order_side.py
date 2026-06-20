from enum import Enum


class OrderSide(str, Enum):
    BUY = "buy"
    COVER = "cover"
    SELL = "sell"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
