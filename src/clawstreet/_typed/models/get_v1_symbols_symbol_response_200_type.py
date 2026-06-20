from enum import Enum


class GetV1SymbolsSymbolResponse200Type(str, Enum):
    CRYPTO = "crypto"
    STOCK = "stock"

    def __str__(self) -> str:
        return str(self.value)
