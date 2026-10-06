from enum import StrEnum


class PutV1MeArtifactsKindResponse202ArtifactStatus(StrEnum):
    ACCEPTED = "accepted"
    ACTIVE = "active"
    PROPOSED = "proposed"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
