from enum import Enum


class PositionPriceFreshness(str, Enum):
    COST = "cost"
    LIVE = "live"
    RECENT = "recent"
    STALE = "stale"
    TODAY = "today"

    def __str__(self) -> str:
        return str(self.value)
