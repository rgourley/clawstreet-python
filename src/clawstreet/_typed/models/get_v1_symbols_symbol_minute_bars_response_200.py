from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_minute_bars_response_200_bars_item import (
        GetV1SymbolsSymbolMinuteBarsResponse200BarsItem,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolMinuteBarsResponse200")


@_attrs_define
class GetV1SymbolsSymbolMinuteBarsResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        date (str): The session date, YYYY-MM-DD in Eastern Time.
        count (int): Number of bars. 390 for a full session.
        bars (list[GetV1SymbolsSymbolMinuteBarsResponse200BarsItem]): Closed bars, oldest first.
        live (bool): True while the session is open and more bars are coming.
        next_bar_at (None | str): ISO time the next bar can be read. Null when `live` is false.
    """

    success: bool
    symbol: str
    date: str
    count: int
    bars: list[GetV1SymbolsSymbolMinuteBarsResponse200BarsItem]
    live: bool
    next_bar_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        date = self.date

        count = self.count

        bars = []
        for bars_item_data in self.bars:
            bars_item = bars_item_data.to_dict()
            bars.append(bars_item)

        live = self.live

        next_bar_at: None | str
        next_bar_at = self.next_bar_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "date": date,
                "count": count,
                "bars": bars,
                "live": live,
                "next_bar_at": next_bar_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_symbols_symbol_minute_bars_response_200_bars_item import (
            GetV1SymbolsSymbolMinuteBarsResponse200BarsItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        date = d.pop("date")

        count = d.pop("count")

        bars = []
        _bars = d.pop("bars")
        for bars_item_data in _bars:
            bars_item = GetV1SymbolsSymbolMinuteBarsResponse200BarsItem.from_dict(
                bars_item_data
            )

            bars.append(bars_item)

        live = d.pop("live")

        def _parse_next_bar_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_bar_at = _parse_next_bar_at(d.pop("next_bar_at"))

        get_v1_symbols_symbol_minute_bars_response_200 = cls(
            success=success,
            symbol=symbol,
            date=date,
            count=count,
            bars=bars,
            live=live,
            next_bar_at=next_bar_at,
        )

        get_v1_symbols_symbol_minute_bars_response_200.additional_properties = d
        return get_v1_symbols_symbol_minute_bars_response_200

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
