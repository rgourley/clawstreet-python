from enum import StrEnum


class GetV1ScanResponse200Mode(StrEnum):
    FILTER = "filter"
    LIVE = "live"
    PRECOMPUTED = "precomputed"

    def __str__(self) -> str:
        return str(self.value)
