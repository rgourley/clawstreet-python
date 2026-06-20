from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="Portfolio")


@_attrs_define
class Portfolio:
    """
    Attributes:
        success (bool):
        cash (float):
        equity (float):
        total_return_pct (float):
        unrealized_pl (float):
        positions (list[Position]):
        initial_balance (float):
    """

    success: bool
    cash: float
    equity: float
    total_return_pct: float
    unrealized_pl: float
    positions: list[Position]
    initial_balance: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        cash = self.cash

        equity = self.equity

        total_return_pct = self.total_return_pct

        unrealized_pl = self.unrealized_pl

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        initial_balance = self.initial_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "cash": cash,
                "equity": equity,
                "total_return_pct": total_return_pct,
                "unrealized_pl": unrealized_pl,
                "positions": positions,
                "initial_balance": initial_balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position

        d = dict(src_dict)
        success = d.pop("success")

        cash = d.pop("cash")

        equity = d.pop("equity")

        total_return_pct = d.pop("total_return_pct")

        unrealized_pl = d.pop("unrealized_pl")

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        initial_balance = d.pop("initial_balance")

        portfolio = cls(
            success=success,
            cash=cash,
            equity=equity,
            total_return_pct=total_return_pct,
            unrealized_pl=unrealized_pl,
            positions=positions,
            initial_balance=initial_balance,
        )

        portfolio.additional_properties = d
        return portfolio

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
