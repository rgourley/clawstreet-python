from enum import StrEnum


class GetV1SymbolsSymbolHistoryResponse200PriceBreakType0Reason(StrEnum):
    SPLIT = "split"
    TICKER_CHANGE = "ticker_change"
    UNEXPLAINED = "unexplained"

    def __str__(self) -> str:
        return str(self.value)
