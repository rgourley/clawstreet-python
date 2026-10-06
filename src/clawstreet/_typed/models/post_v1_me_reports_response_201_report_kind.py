from enum import StrEnum


class PostV1MeReportsResponse201ReportKind(StrEnum):
    BUG = "bug"
    DATA = "data"
    DOCS = "docs"

    def __str__(self) -> str:
        return str(self.value)
