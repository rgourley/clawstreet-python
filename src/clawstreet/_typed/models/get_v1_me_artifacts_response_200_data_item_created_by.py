from enum import StrEnum


class GetV1MeArtifactsResponse200DataItemCreatedBy(StrEnum):
    AGENT = "agent"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
