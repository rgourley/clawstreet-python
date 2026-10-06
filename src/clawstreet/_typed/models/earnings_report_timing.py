from enum import StrEnum


class EarningsReportTiming(StrEnum):
    AMC = "AMC"
    BMO = "BMO"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
