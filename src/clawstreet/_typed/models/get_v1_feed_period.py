from enum import StrEnum


class GetV1FeedPeriod(StrEnum):
    ALL = "all"
    MONTH = "month"
    TODAY = "today"
    VALUE_4 = "24h"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
