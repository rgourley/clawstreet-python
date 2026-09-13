from enum import StrEnum


class JournalReviewKind(StrEnum):
    REVIEW = "review"

    def __str__(self) -> str:
        return str(self.value)
