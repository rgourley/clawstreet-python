from enum import StrEnum


class OrderTimeInForce(StrEnum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)
