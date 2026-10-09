from enum import StrEnum


class GetV1SymbolsSymbolFundamentalsResponse200FundamentalsPeBasis(StrEnum):
    ANNUAL = "annual"
    QUARTERLY_X4 = "quarterly_x4"
    TTM = "ttm"

    def __str__(self) -> str:
        return str(self.value)
