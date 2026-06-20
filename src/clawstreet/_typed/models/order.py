from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_order_type import OrderOrderType
from ..models.order_side import OrderSide
from ..models.order_time_in_force import OrderTimeInForce
from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@_attrs_define
class Order:
    """
    Attributes:
        id (UUID):
        agent_id (UUID):
        symbol (str):  Example: AAPL.
        side (OrderSide):
        qty (float):  Example: 100.
        order_type (OrderOrderType):  Example: market.
        status (str):  Example: filled.
        created_at (datetime.datetime):
        limit_price (float | None | Unset):
        stop_price (float | None | Unset):
        trail_pct (float | None | Unset):
        time_in_force (OrderTimeInForce | Unset):
        reasoning (None | str | Unset):
        filled_at (datetime.datetime | None | Unset):
        canceled_at (datetime.datetime | None | Unset):
    """

    id: UUID
    agent_id: UUID
    symbol: str
    side: OrderSide
    qty: float
    order_type: OrderOrderType
    status: str
    created_at: datetime.datetime
    limit_price: float | None | Unset = UNSET
    stop_price: float | None | Unset = UNSET
    trail_pct: float | None | Unset = UNSET
    time_in_force: OrderTimeInForce | Unset = UNSET
    reasoning: None | str | Unset = UNSET
    filled_at: datetime.datetime | None | Unset = UNSET
    canceled_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        symbol = self.symbol

        side = self.side.value

        qty = self.qty

        order_type = self.order_type.value

        status = self.status

        created_at = self.created_at.isoformat()

        limit_price: float | None | Unset
        if isinstance(self.limit_price, Unset):
            limit_price = UNSET
        else:
            limit_price = self.limit_price

        stop_price: float | None | Unset
        if isinstance(self.stop_price, Unset):
            stop_price = UNSET
        else:
            stop_price = self.stop_price

        trail_pct: float | None | Unset
        if isinstance(self.trail_pct, Unset):
            trail_pct = UNSET
        else:
            trail_pct = self.trail_pct

        time_in_force: str | Unset = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force.value

        reasoning: None | str | Unset
        if isinstance(self.reasoning, Unset):
            reasoning = UNSET
        else:
            reasoning = self.reasoning

        filled_at: None | str | Unset
        if isinstance(self.filled_at, Unset):
            filled_at = UNSET
        elif isinstance(self.filled_at, datetime.datetime):
            filled_at = self.filled_at.isoformat()
        else:
            filled_at = self.filled_at

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "symbol": symbol,
                "side": side,
                "qty": qty,
                "order_type": order_type,
                "status": status,
                "created_at": created_at,
            }
        )
        if limit_price is not UNSET:
            field_dict["limit_price"] = limit_price
        if stop_price is not UNSET:
            field_dict["stop_price"] = stop_price
        if trail_pct is not UNSET:
            field_dict["trail_pct"] = trail_pct
        if time_in_force is not UNSET:
            field_dict["time_in_force"] = time_in_force
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if filled_at is not UNSET:
            field_dict["filled_at"] = filled_at
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        agent_id = UUID(d.pop("agent_id"))

        symbol = d.pop("symbol")

        side = OrderSide(d.pop("side"))

        qty = d.pop("qty")

        order_type = OrderOrderType(d.pop("order_type"))

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_limit_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        limit_price = _parse_limit_price(d.pop("limit_price", UNSET))

        def _parse_stop_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stop_price = _parse_stop_price(d.pop("stop_price", UNSET))

        def _parse_trail_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trail_pct = _parse_trail_pct(d.pop("trail_pct", UNSET))

        _time_in_force = d.pop("time_in_force", UNSET)
        time_in_force: OrderTimeInForce | Unset
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = OrderTimeInForce(_time_in_force)

        def _parse_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning = _parse_reasoning(d.pop("reasoning", UNSET))

        def _parse_filled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filled_at_type_0 = datetime.datetime.fromisoformat(data)

                return filled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        filled_at = _parse_filled_at(d.pop("filled_at", UNSET))

        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = datetime.datetime.fromisoformat(data)

                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

        order = cls(
            id=id,
            agent_id=agent_id,
            symbol=symbol,
            side=side,
            qty=qty,
            order_type=order_type,
            status=status,
            created_at=created_at,
            limit_price=limit_price,
            stop_price=stop_price,
            trail_pct=trail_pct,
            time_in_force=time_in_force,
            reasoning=reasoning,
            filled_at=filled_at,
            canceled_at=canceled_at,
        )

        order.additional_properties = d
        return order

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
