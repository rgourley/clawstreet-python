from enum import Enum


class GetV1OptionsQuoteOccSymbolResponse200Type(str, Enum):
    CALL = "call"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
