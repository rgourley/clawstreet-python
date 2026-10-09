from enum import StrEnum


class GetV1SymbolsSymbolFundamentalsResponse200FundamentalsAnnualNetIncomeBasis(
    StrEnum
):
    ANNUAL = "annual"
    TTM = "ttm"

    def __str__(self) -> str:
        return str(self.value)
