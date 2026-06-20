from enum import Enum


class PostV1MeAgentsIdOrdersBodyTimeInForce(str, Enum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)
