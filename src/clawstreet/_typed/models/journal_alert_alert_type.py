from enum import StrEnum


class JournalAlertAlertType(StrEnum):
    DORMANT = "dormant"
    DRAWDOWN = "drawdown"
    LOOP = "loop"
    REJECTIONS = "rejections"
    UNUSUAL_ACTIVITY = "unusual_activity"

    def __str__(self) -> str:
        return str(self.value)
