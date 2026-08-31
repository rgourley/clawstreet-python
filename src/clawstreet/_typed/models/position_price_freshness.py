from enum import StrEnum


class PositionPriceFreshness(StrEnum):
    COST = "cost"
    LIVE = "live"
    RECENT = "recent"
    STALE = "stale"
    TODAY = "today"

    def __str__(self) -> str:
        return str(self.value)
