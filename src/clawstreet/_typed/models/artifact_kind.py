from enum import StrEnum


class ArtifactKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PLAYBOOK = "playbook"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
