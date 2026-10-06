from enum import StrEnum


class GetV1MeReportsResponse200DataItemKind(StrEnum):
    BUG = "bug"
    DATA = "data"
    DOCS = "docs"

    def __str__(self) -> str:
        return str(self.value)
