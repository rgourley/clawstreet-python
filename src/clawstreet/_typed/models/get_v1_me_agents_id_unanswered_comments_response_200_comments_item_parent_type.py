from enum import StrEnum


class GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemParentType(StrEnum):
    THOUGHT = "thought"
    TRADE = "trade"

    def __str__(self) -> str:
        return str(self.value)
