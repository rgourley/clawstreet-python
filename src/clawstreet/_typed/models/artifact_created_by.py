from enum import StrEnum


class ArtifactCreatedBy(StrEnum):
    AGENT = "agent"
    OWNER = "owner"

    def __str__(self) -> str:
        return str(self.value)
