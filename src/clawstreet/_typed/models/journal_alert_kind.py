from enum import StrEnum


class JournalAlertKind(StrEnum):
    ALERT = "alert"

    def __str__(self) -> str:
        return str(self.value)
