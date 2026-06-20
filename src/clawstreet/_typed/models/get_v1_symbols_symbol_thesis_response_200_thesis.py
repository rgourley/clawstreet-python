from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1SymbolsSymbolThesisResponse200Thesis")


@_attrs_define
class GetV1SymbolsSymbolThesisResponse200Thesis:
    """
    Attributes:
        bulls (list[str]):
        bears (list[str]):
    """

    bulls: list[str]
    bears: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bulls = self.bulls

        bears = self.bears

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bulls": bulls,
                "bears": bears,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bulls = cast(list[str], d.pop("bulls"))

        bears = cast(list[str], d.pop("bears"))

        get_v1_symbols_symbol_thesis_response_200_thesis = cls(
            bulls=bulls,
            bears=bears,
        )

        get_v1_symbols_symbol_thesis_response_200_thesis.additional_properties = d
        return get_v1_symbols_symbol_thesis_response_200_thesis

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
