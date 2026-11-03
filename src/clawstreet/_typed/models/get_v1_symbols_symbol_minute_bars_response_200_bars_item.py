from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1SymbolsSymbolMinuteBarsResponse200BarsItem")


@_attrs_define
class GetV1SymbolsSymbolMinuteBarsResponse200BarsItem:
    """
    Attributes:
        t (int): Bar start, Unix milliseconds.
        o (float):
        h (float):
        l (float):
        c (float):
        v (float):
    """

    t: int
    o: float
    h: float
    l: float
    c: float
    v: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        t = self.t

        o = self.o

        h = self.h

        l = self.l

        c = self.c

        v = self.v

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t": t,
                "o": o,
                "h": h,
                "l": l,
                "c": c,
                "v": v,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        t = d.pop("t")

        o = d.pop("o")

        h = d.pop("h")

        l = d.pop("l")

        c = d.pop("c")

        v = d.pop("v")

        get_v1_symbols_symbol_minute_bars_response_200_bars_item = cls(
            t=t,
            o=o,
            h=h,
            l=l,
            c=c,
            v=v,
        )

        get_v1_symbols_symbol_minute_bars_response_200_bars_item.additional_properties = d
        return get_v1_symbols_symbol_minute_bars_response_200_bars_item

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
