from enum import StrEnum


class GetV1MarketResponse200MarketSentimentType0Level(StrEnum):
    CALM = "calm"
    CAUTIOUS = "cautious"
    FEARFUL = "fearful"

    def __str__(self) -> str:
        return str(self.value)
