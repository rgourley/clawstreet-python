from enum import StrEnum


class GetV1MeArtifactsResponse200DataItemKind(StrEnum):
    CONFIG = "config"
    LESSONS = "lessons"
    PLAYBOOK = "playbook"
    PROMPT = "prompt"

    def __str__(self) -> str:
        return str(self.value)
