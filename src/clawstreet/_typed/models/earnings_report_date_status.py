from enum import StrEnum


class EarningsReportDateStatus(StrEnum):
    CONFIRMED = "confirmed"
    PROJECTED = "projected"

    def __str__(self) -> str:
        return str(self.value)
