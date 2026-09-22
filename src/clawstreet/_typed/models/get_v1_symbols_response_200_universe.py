from enum import StrEnum


class GetV1SymbolsResponse200Universe(StrEnum):
    FREE = "free"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
