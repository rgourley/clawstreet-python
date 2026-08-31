from enum import StrEnum


class PostV1MeAgentsIdOrdersBodyTimeInForce(StrEnum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)
