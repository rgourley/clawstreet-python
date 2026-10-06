from enum import StrEnum


class GetV1MeArtifactsKindKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PLAYBOOK = "playbook"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
