from enum import StrEnum


class GetV1SymbolsSymbolHistoryResponse200DerivedRsiTrend(StrEnum):
    FALLING = "falling"
    FLAT = "flat"
    RISING = "rising"

    def __str__(self) -> str:
        return str(self.value)
