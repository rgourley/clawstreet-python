from enum import StrEnum


class GetV1MeReportsResponse200DataItemStatus(StrEnum):
    FIXED = "fixed"
    NOT_A_BUG = "not_a_bug"
    OPEN = "open"
    WONT_FIX = "wont_fix"

    def __str__(self) -> str:
        return str(self.value)
