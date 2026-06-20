from enum import Enum


class GetV1FeedPeriod(str, Enum):
    ALL = "all"
    MONTH = "month"
    TODAY = "today"
    VALUE_4 = "24h"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
