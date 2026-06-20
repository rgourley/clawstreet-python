from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_earnings_response_200_earnings_item import (
        GetV1SymbolsSymbolEarningsResponse200EarningsItem,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolEarningsResponse200")


@_attrs_define
class GetV1SymbolsSymbolEarningsResponse200:
    """
    Attributes:
        success (bool):
        earnings (list[GetV1SymbolsSymbolEarningsResponse200EarningsItem]):
    """

    success: bool
    earnings: list[GetV1SymbolsSymbolEarningsResponse200EarningsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        earnings = []
        for earnings_item_data in self.earnings:
            earnings_item = earnings_item_data.to_dict()
            earnings.append(earnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "earnings": earnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_symbols_symbol_earnings_response_200_earnings_item import (
            GetV1SymbolsSymbolEarningsResponse200EarningsItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        earnings = []
        _earnings = d.pop("earnings")
        for earnings_item_data in _earnings:
            earnings_item = GetV1SymbolsSymbolEarningsResponse200EarningsItem.from_dict(
                earnings_item_data
            )

            earnings.append(earnings_item)

        get_v1_symbols_symbol_earnings_response_200 = cls(
            success=success,
            earnings=earnings,
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
