from enum import Enum


class PostV1MeAgentsIdOrdersBodyOrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"
    TRAILING_STOP = "trailing_stop"

    def __str__(self) -> str:
        return str(self.value)
