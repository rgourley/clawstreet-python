from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_symbols_response_200_universe import (
    GetV1SymbolsResponse200Universe,
)

T = TypeVar("T", bound="GetV1SymbolsResponse200")


@_attrs_define
class GetV1SymbolsResponse200:
    """
    Attributes:
        success (bool):
        symbols (list[str]):  Example: ['AAPL', 'MSFT', 'X:BTCUSD'].
        count (int):
        universe (GetV1SymbolsResponse200Universe):
    """

    success: bool
    symbols: list[str]
    count: int
    universe: GetV1SymbolsResponse200Universe
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbols = self.symbols

        count = self.count

        universe = self.universe.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbols": symbols,
                "count": count,
                "universe": universe,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        symbols = cast(list[str], d.pop("symbols"))

        count = d.pop("count")

        universe = GetV1SymbolsResponse200Universe(d.pop("universe"))

        get_v1_symbols_response_200 = cls(
            success=success,
            symbols=symbols,
            count=count,
            universe=universe,
        )

        get_v1_symbols_response_200.additional_properties = d
        return get_v1_symbols_response_200

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
