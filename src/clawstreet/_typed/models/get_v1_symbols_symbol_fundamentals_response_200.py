from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_fundamentals_response_200_fundamentals import (
        GetV1SymbolsSymbolFundamentalsResponse200Fundamentals,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolFundamentalsResponse200")


@_attrs_define
class GetV1SymbolsSymbolFundamentalsResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        fundamentals (GetV1SymbolsSymbolFundamentalsResponse200Fundamentals):
        timestamp (str):
    """

    success: bool
    symbol: str
    fundamentals: GetV1SymbolsSymbolFundamentalsResponse200Fundamentals
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        fundamentals = self.fundamentals.to_dict()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "fundamentals": fundamentals,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_symbols_symbol_fundamentals_response_200_fundamentals import (
            GetV1SymbolsSymbolFundamentalsResponse200Fundamentals,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        fundamentals = GetV1SymbolsSymbolFundamentalsResponse200Fundamentals.from_dict(
            d.pop("fundamentals")
        )

        timestamp = d.pop("timestamp")

        get_v1_symbols_symbol_fundamentals_response_200 = cls(
            success=success,
            symbol=symbol,
            fundamentals=fundamentals,
            timestamp=timestamp,
        )

        get_v1_symbols_symbol_fundamentals_response_200.additional_properties = d
        return get_v1_symbols_symbol_fundamentals_response_200

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
