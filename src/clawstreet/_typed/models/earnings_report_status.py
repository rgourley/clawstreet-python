from enum import StrEnum


class EarningsReportStatus(StrEnum):
    NO_DATA = "no_data"
    REPORTED = "reported"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
