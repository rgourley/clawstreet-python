from enum import StrEnum


class PutV1MeArtifactsKindResponse201ArtifactKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PLAYBOOK = "playbook"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
