from enum import StrEnum


class GetV1SymbolsSymbolHistoryTimespan(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
