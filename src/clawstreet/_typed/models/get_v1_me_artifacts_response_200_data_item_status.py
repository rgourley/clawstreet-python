from enum import StrEnum


class GetV1MeArtifactsResponse200DataItemStatus(StrEnum):
    ACTIVE = "active"
    PROPOSED = "proposed"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
