from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PortfolioLimits")


@_attrs_define
class PortfolioLimits:
    """
    Attributes:
        max_concentration_pct (float):
        max_leverage (float):
    """

    max_concentration_pct: float
    max_leverage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_concentration_pct = self.max_concentration_pct

        max_leverage = self.max_leverage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_concentration_pct": max_concentration_pct,
                "max_leverage": max_leverage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_concentration_pct = d.pop("max_concentration_pct")

        max_leverage = d.pop("max_leverage")

        portfolio_limits = cls(
            max_concentration_pct=max_concentration_pct,
            max_leverage=max_leverage,
        )

        portfolio_limits.additional_properties = d
        return portfolio_limits

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
