from enum import StrEnum


class PostV1VotesBodyAction(StrEnum):
    DOWN = "down"
    REMOVE = "remove"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
