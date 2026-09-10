from enum import StrEnum


class ArtifactKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
