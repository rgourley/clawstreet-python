from enum import StrEnum


class GetV1OptionsQuoteOccSymbolResponse200Type(StrEnum):
    CALL = "call"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
