from enum import StrEnum


class GetV1SymbolsSymbolRelatedResponse200Source(StrEnum):
    CURATED = "curated"
    MASSIVE = "massive"

    def __str__(self) -> str:
        return str(self.value)
