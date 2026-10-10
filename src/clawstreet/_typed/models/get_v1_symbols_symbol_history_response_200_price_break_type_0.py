from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_symbols_symbol_history_response_200_price_break_type_0_reason import (
    GetV1SymbolsSymbolHistoryResponse200PriceBreakType0Reason,
)

T = TypeVar("T", bound="GetV1SymbolsSymbolHistoryResponse200PriceBreakType0")


@_attrs_define
class GetV1SymbolsSymbolHistoryResponse200PriceBreakType0:
    """The most recent price break in the fetched bars, or null.

    Attributes:
        date (None | str): Trading date (YYYY-MM-DD) of the first bar after the move. Null when the bar has no
            timestamp. Example: 2026-10-01.
        change_pct (float): Close-to-close percent change into `date`. Example: -83.81.
        reason (GetV1SymbolsSymbolHistoryResponse200PriceBreakType0Reason): `split`: Massive records a split on `date`.
            `ticker_change`: Massive records a ticker event on `date`, for example a new company that takes over the symbol.
            `unexplained`: Massive records no action on `date`. A spinoff is usually `unexplained`, because Massive records
            it only on the new company's ticker.
    """

    date: None | str
    change_pct: float
    reason: GetV1SymbolsSymbolHistoryResponse200PriceBreakType0Reason
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str
        date = self.date

        change_pct = self.change_pct

        reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "change_pct": change_pct,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        date = _parse_date(d.pop("date"))

        change_pct = d.pop("change_pct")

        reason = GetV1SymbolsSymbolHistoryResponse200PriceBreakType0Reason(
            d.pop("reason")
        )

        get_v1_symbols_symbol_history_response_200_price_break_type_0 = cls(
            date=date,
            change_pct=change_pct,
            reason=reason,
        )

        get_v1_symbols_symbol_history_response_200_price_break_type_0.additional_properties = d
        return get_v1_symbols_symbol_history_response_200_price_break_type_0

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
