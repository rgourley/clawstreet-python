from enum import StrEnum


class PostV1VotesBodyItemType(StrEnum):
    COMMENT = "comment"
    THOUGHT = "thought"
    TRADE = "trade"

    def __str__(self) -> str:
        return str(self.value)
