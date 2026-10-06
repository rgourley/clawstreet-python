from enum import StrEnum


class PostV1MeReportsBodyKind(StrEnum):
    BUG = "bug"
    DATA = "data"
    DOCS = "docs"

    def __str__(self) -> str:
        return str(self.value)
