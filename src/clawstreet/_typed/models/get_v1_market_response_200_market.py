from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_market_response_200_market_sector_performance import (
        GetV1MarketResponse200MarketSectorPerformance,
    )
    from ..models.get_v1_market_response_200_market_sentiment_type_0 import (
        GetV1MarketResponse200MarketSentimentType0,
    )


T = TypeVar("T", bound="GetV1MarketResponse200Market")


@_attrs_define
class GetV1MarketResponse200Market:
    """
    Attributes:
        spy_return_1d (float | None):
        sentiment (GetV1MarketResponse200MarketSentimentType0 | None):
        sector_performance (GetV1MarketResponse200MarketSectorPerformance):  Example: {'technology': 0.0123, 'energy':
            -0.0045}.
        as_of (datetime.datetime | None):
        data_age_seconds (int | None):
    """

    spy_return_1d: float | None
    sentiment: GetV1MarketResponse200MarketSentimentType0 | None
    sector_performance: GetV1MarketResponse200MarketSectorPerformance
    as_of: datetime.datetime | None
    data_age_seconds: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v1_market_response_200_market_sentiment_type_0 import (
            GetV1MarketResponse200MarketSentimentType0,
        )

        spy_return_1d: float | None
        spy_return_1d = self.spy_return_1d

        sentiment: dict[str, Any] | None
        if isinstance(self.sentiment, GetV1MarketResponse200MarketSentimentType0):
            sentiment = self.sentiment.to_dict()
        else:
            sentiment = self.sentiment

        sector_performance = self.sector_performance.to_dict()

        as_of: None | str
        if isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        data_age_seconds: int | None
        data_age_seconds = self.data_age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spy_return_1d": spy_return_1d,
                "sentiment": sentiment,
                "sector_performance": sector_performance,
                "asOf": as_of,
                "dataAgeSeconds": data_age_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_market_response_200_market_sector_performance import (
            GetV1MarketResponse200MarketSectorPerformance,
        )
        from ..models.get_v1_market_response_200_market_sentiment_type_0 import (
            GetV1MarketResponse200MarketSentimentType0,
        )

        d = dict(src_dict)

        def _parse_spy_return_1d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        spy_return_1d = _parse_spy_return_1d(d.pop("spy_return_1d"))

        def _parse_sentiment(
            data: object,
        ) -> GetV1MarketResponse200MarketSentimentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sentiment_type_0 = GetV1MarketResponse200MarketSentimentType0.from_dict(
                    data
                )

                return sentiment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketResponse200MarketSentimentType0 | None, data)

        sentiment = _parse_sentiment(d.pop("sentiment"))

        sector_performance = GetV1MarketResponse200MarketSectorPerformance.from_dict(
            d.pop("sector_performance")
        )

        def _parse_as_of(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        as_of = _parse_as_of(d.pop("asOf"))

        def _parse_data_age_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        data_age_seconds = _parse_data_age_seconds(d.pop("dataAgeSeconds"))

        get_v1_market_response_200_market = cls(
            spy_return_1d=spy_return_1d,
            sentiment=sentiment,
            sector_performance=sector_performance,
            as_of=as_of,
            data_age_seconds=data_age_seconds,
        )

        get_v1_market_response_200_market.additional_properties = d
        return get_v1_market_response_200_market

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
