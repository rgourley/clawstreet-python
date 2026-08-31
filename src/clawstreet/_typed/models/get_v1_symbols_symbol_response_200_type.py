from enum import StrEnum


class GetV1SymbolsSymbolResponse200Type(StrEnum):
    CRYPTO = "crypto"
    STOCK = "stock"

    def __str__(self) -> str:
        return str(self.value)
