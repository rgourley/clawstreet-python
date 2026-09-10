from enum import StrEnum


class GetV1QuotesResponse200QuotesAdditionalPropertySource(StrEnum):
    DELAYED = "delayed"
    FMV = "fmv"

    def __str__(self) -> str:
        return str(self.value)
