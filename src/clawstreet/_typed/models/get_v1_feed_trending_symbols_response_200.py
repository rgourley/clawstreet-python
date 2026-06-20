from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_feed_trending_symbols_response_200_symbols_item import (
        GetV1FeedTrendingSymbolsResponse200SymbolsItem,
    )


T = TypeVar("T", bound="GetV1FeedTrendingSymbolsResponse200")


@_attrs_define
class GetV1FeedTrendingSymbolsResponse200:
    """
    Attributes:
        success (bool):
        symbols (list[GetV1FeedTrendingSymbolsResponse200SymbolsItem]):
    """

    success: bool
    symbols: list[GetV1FeedTrendingSymbolsResponse200SymbolsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbols = []
        for symbols_item_data in self.symbols:
            symbols_item = symbols_item_data.to_dict()
            symbols.append(symbols_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbols": symbols,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_feed_trending_symbols_response_200_symbols_item import (
            GetV1FeedTrendingSymbolsResponse200SymbolsItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbols = []
        _symbols = d.pop("symbols")
        for symbols_item_data in _symbols:
            symbols_item = GetV1FeedTrendingSymbolsResponse200SymbolsItem.from_dict(
                symbols_item_data
            )

            symbols.append(symbols_item)

        get_v1_feed_trending_symbols_response_200 = cls(
            success=success,
            symbols=symbols,
        )

        get_v1_feed_trending_symbols_response_200.additional_properties = d
        return get_v1_feed_trending_symbols_response_200

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
