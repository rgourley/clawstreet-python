from enum import StrEnum


class OrderSide(StrEnum):
    BUY = "buy"
    COVER = "cover"
    SELL = "sell"
    SHORT = "short"

    def __str__(self) -> str:
        return str(self.value)
