from enum import StrEnum


class PutV1MeArtifactsKindResponse202ArtifactCreatedBy(StrEnum):
    AGENT = "agent"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
