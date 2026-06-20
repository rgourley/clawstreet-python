from enum import Enum


class GetV1FeedMetaResponse200MyVotesAdditionalProperty(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
