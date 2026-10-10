from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.earnings_report import EarningsReport


T = TypeVar("T", bound="GetV1SymbolsSymbolEarningsResponse200")


@_attrs_define
class GetV1SymbolsSymbolEarningsResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):  Example: NKE.
        earnings (list[EarningsReport]):
        days (int):
        past (int):
        count (int):
        fetched_at (datetime.datetime):
    """

    success: bool
    symbol: str
    earnings: list[EarningsReport]
    days: int
    past: int
    count: int
    fetched_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        earnings = []
        for earnings_item_data in self.earnings:
            earnings_item = earnings_item_data.to_dict()
            earnings.append(earnings_item)

        days = self.days

        past = self.past

        count = self.count

        fetched_at = self.fetched_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "earnings": earnings,
                "days": days,
                "past": past,
                "count": count,
                "fetchedAt": fetched_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.earnings_report import EarningsReport

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        earnings = []
        _earnings = d.pop("earnings")
        for earnings_item_data in _earnings:
            earnings_item = EarningsReport.from_dict(earnings_item_data)

            earnings.append(earnings_item)

        days = d.pop("days")

        past = d.pop("past")

        count = d.pop("count")

        fetched_at = datetime.datetime.fromisoformat(d.pop("fetchedAt"))

        get_v1_symbols_symbol_earnings_response_200 = cls(
            success=success,
            symbol=symbol,
            earnings=earnings,
            days=days,
            past=past,
            count=count,
            fetched_at=fetched_at,
        )

        get_v1_symbols_symbol_earnings_response_200.additional_properties = d
        return get_v1_symbols_symbol_earnings_response_200

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
