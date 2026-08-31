from enum import StrEnum


class GetV1FeedMetaResponse200MyVotesAdditionalProperty(StrEnum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
