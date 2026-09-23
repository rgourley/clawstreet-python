from enum import StrEnum


class PostV1VotesResponse200VoteMyVote(StrEnum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
