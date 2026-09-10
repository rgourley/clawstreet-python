from enum import StrEnum


class GetV1MeArtifactsKindResponse200VersionsItemCreatedBy(StrEnum):
    AGENT = "agent"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
