from enum import StrEnum


class PostV1VotesResponse200VoteItemType(StrEnum):
    COMMENT = "comment"
    THOUGHT = "thought"
    TRADE = "trade"

    def __str__(self) -> str:
        return str(self.value)
