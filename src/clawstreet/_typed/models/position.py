from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_side import PositionSide

T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    """
    Attributes:
        symbol (str):
        qty (float):
        side (PositionSide):
        avg_cost (float):
        current_price (float | None):
        market_value (float | None):
        unrealized_pl (float | None):
        unrealized_pl_pct (float | None):
    """

    symbol: str
    qty: float
    side: PositionSide
    avg_cost: float
    current_price: float | None
    market_value: float | None
    unrealized_pl: float | None
    unrealized_pl_pct: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        qty = self.qty

        side = self.side.value

        avg_cost = self.avg_cost

        current_price: float | None
        current_price = self.current_price

        market_value: float | None
        market_value = self.market_value

        unrealized_pl: float | None
        unrealized_pl = self.unrealized_pl

        unrealized_pl_pct: float | None
        unrealized_pl_pct = self.unrealized_pl_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "qty": qty,
                "side": side,
                "avg_cost": avg_cost,
                "current_price": current_price,
                "market_value": market_value,
                "unrealized_pl": unrealized_pl,
                "unrealized_pl_pct": unrealized_pl_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        qty = d.pop("qty")

        side = PositionSide(d.pop("side"))

        avg_cost = d.pop("avg_cost")

        def _parse_current_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        current_price = _parse_current_price(d.pop("current_price"))

        def _parse_market_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        market_value = _parse_market_value(d.pop("market_value"))

        def _parse_unrealized_pl(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        unrealized_pl = _parse_unrealized_pl(d.pop("unrealized_pl"))

        def _parse_unrealized_pl_pct(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        unrealized_pl_pct = _parse_unrealized_pl_pct(d.pop("unrealized_pl_pct"))

        position = cls(
            symbol=symbol,
            qty=qty,
            side=side,
            avg_cost=avg_cost,
            current_price=current_price,
            market_value=market_value,
            unrealized_pl=unrealized_pl,
            unrealized_pl_pct=unrealized_pl_pct,
        )

        position.additional_properties = d
        return position

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
