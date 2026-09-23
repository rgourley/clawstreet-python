from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_market_response_200_market import GetV1MarketResponse200Market


T = TypeVar("T", bound="GetV1MarketResponse200")


@_attrs_define
class GetV1MarketResponse200:
    """
    Attributes:
        success (bool):
        market (GetV1MarketResponse200Market):
        fetched_at (datetime.datetime):
        delayed (bool):
    """

    success: bool
    market: GetV1MarketResponse200Market
    fetched_at: datetime.datetime
    delayed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        market = self.market.to_dict()

        fetched_at = self.fetched_at.isoformat()

        delayed = self.delayed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "market": market,
                "fetchedAt": fetched_at,
                "delayed": delayed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_market_response_200_market import (
            GetV1MarketResponse200Market,
        )

        d = dict(src_dict)
        success = d.pop("success")

        market = GetV1MarketResponse200Market.from_dict(d.pop("market"))

        fetched_at = datetime.datetime.fromisoformat(d.pop("fetchedAt"))

        delayed = d.pop("delayed")

        get_v1_market_response_200 = cls(
            success=success,
            market=market,
            fetched_at=fetched_at,
            delayed=delayed,
        )

        get_v1_market_response_200.additional_properties = d
        return get_v1_market_response_200

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
