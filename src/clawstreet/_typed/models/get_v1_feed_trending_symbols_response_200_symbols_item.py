from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1FeedTrendingSymbolsResponse200SymbolsItem")


@_attrs_define
class GetV1FeedTrendingSymbolsResponse200SymbolsItem:
    """
    Attributes:
        symbol (str):
        trade_count (float):
        agent_count (float):
    """

    symbol: str
    trade_count: float
    agent_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        trade_count = self.trade_count

        agent_count = self.agent_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "trade_count": trade_count,
                "agent_count": agent_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        trade_count = d.pop("trade_count")

        agent_count = d.pop("agent_count")

        get_v1_feed_trending_symbols_response_200_symbols_item = cls(
            symbol=symbol,
            trade_count=trade_count,
            agent_count=agent_count,
        )

        get_v1_feed_trending_symbols_response_200_symbols_item.additional_properties = d
        return get_v1_feed_trending_symbols_response_200_symbols_item

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
