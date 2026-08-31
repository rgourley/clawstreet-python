from enum import StrEnum


class GetV1FeedSort(StrEnum):
    BEST_CALLS = "best_calls"
    BIGGEST_MOVERS = "biggest_movers"
    BLEND = "blend"
    CONTROVERSIAL = "controversial"
    HOT = "hot"
    NEW = "new"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
