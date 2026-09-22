from enum import StrEnum


class GetV1SymbolsSymbolHistoryResponse200Timespan(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
