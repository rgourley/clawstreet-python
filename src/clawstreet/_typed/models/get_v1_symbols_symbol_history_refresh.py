from enum import StrEnum


class GetV1SymbolsSymbolHistoryRefresh(StrEnum):
    VALUE_0 = "1"

    def __str__(self) -> str:
        return str(self.value)
