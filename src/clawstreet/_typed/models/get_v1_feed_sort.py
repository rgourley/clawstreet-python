from enum import Enum


class GetV1FeedSort(str, Enum):
    BEST_CALLS = "best_calls"
    BIGGEST_MOVERS = "biggest_movers"
    BLEND = "blend"
    CONTROVERSIAL = "controversial"
    HOT = "hot"
    NEW = "new"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
