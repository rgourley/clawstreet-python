from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_symbols_symbol_response_200_type import (
    GetV1SymbolsSymbolResponse200Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SymbolsSymbolResponse200")


@_attrs_define
class GetV1SymbolsSymbolResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        type_ (GetV1SymbolsSymbolResponse200Type):
        name (str | Unset):
    """

    success: bool
    symbol: str
    type_: GetV1SymbolsSymbolResponse200Type
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        type_ = GetV1SymbolsSymbolResponse200Type(d.pop("type"))

        name = d.pop("name", UNSET)

        get_v1_symbols_symbol_response_200 = cls(
            success=success,
            symbol=symbol,
            type_=type_,
            name=name,
        )

        get_v1_symbols_symbol_response_200.additional_properties = d
        return get_v1_symbols_symbol_response_200

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
