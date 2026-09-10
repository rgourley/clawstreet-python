from enum import StrEnum


class GetV1MeArtifactsKindResponse200VersionsItemKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
