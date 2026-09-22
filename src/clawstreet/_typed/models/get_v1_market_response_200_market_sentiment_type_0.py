from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_market_response_200_market_sentiment_type_0_level import (
    GetV1MarketResponse200MarketSentimentType0Level,
)

T = TypeVar("T", bound="GetV1MarketResponse200MarketSentimentType0")


@_attrs_define
class GetV1MarketResponse200MarketSentimentType0:
    """
    Attributes:
        level (GetV1MarketResponse200MarketSentimentType0Level):
        spy_change_pct (float):
    """

    level: GetV1MarketResponse200MarketSentimentType0Level
    spy_change_pct: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level.value

        spy_change_pct = self.spy_change_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "spyChangePct": spy_change_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        level = GetV1MarketResponse200MarketSentimentType0Level(d.pop("level"))

        spy_change_pct = d.pop("spyChangePct")

        get_v1_market_response_200_market_sentiment_type_0 = cls(
            level=level,
            spy_change_pct=spy_change_pct,
        )

        get_v1_market_response_200_market_sentiment_type_0.additional_properties = d
        return get_v1_market_response_200_market_sentiment_type_0

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
