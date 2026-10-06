from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PortfolioMargin")


@_attrs_define
class PortfolioMargin:
    """
    Attributes:
        in_violation (bool): True when equity is under the maintenance requirement. The matcher liquidates the worst
            position on its next run.
        equity (float):
        maintenance_required (float):
    """

    in_violation: bool
    equity: float
    maintenance_required: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_violation = self.in_violation

        equity = self.equity

        maintenance_required = self.maintenance_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in_violation": in_violation,
                "equity": equity,
                "maintenance_required": maintenance_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        in_violation = d.pop("in_violation")

        equity = d.pop("equity")

        maintenance_required = d.pop("maintenance_required")

        portfolio_margin = cls(
            in_violation=in_violation,
            equity=equity,
            maintenance_required=maintenance_required,
        )

        portfolio_margin.additional_properties = d
        return portfolio_margin

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
