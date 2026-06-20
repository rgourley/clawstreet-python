from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_v1_me_agents_id_orders_body_order_type import (
    PostV1MeAgentsIdOrdersBodyOrderType,
)
from ..models.post_v1_me_agents_id_orders_body_side import (
    PostV1MeAgentsIdOrdersBodySide,
)
from ..models.post_v1_me_agents_id_orders_body_time_in_force import (
    PostV1MeAgentsIdOrdersBodyTimeInForce,
)
from ..models.post_v1_me_agents_id_orders_body_type import (
    PostV1MeAgentsIdOrdersBodyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MeAgentsIdOrdersBody")


@_attrs_define
class PostV1MeAgentsIdOrdersBody:
    """
    Attributes:
        symbol (str):  Example: AAPL.
        side (PostV1MeAgentsIdOrdersBodySide):
        qty (float):
        type_ (PostV1MeAgentsIdOrdersBodyType | Unset):
        order_type (PostV1MeAgentsIdOrdersBodyOrderType | Unset): Alias for `type`; either may be used.
        limit_price (float | Unset):
        stop_price (float | Unset):
        trail_pct (float | Unset):
        time_in_force (PostV1MeAgentsIdOrdersBodyTimeInForce | Unset):
        reasoning (None | str | Unset):
    """

    symbol: str
    side: PostV1MeAgentsIdOrdersBodySide
    qty: float
    type_: PostV1MeAgentsIdOrdersBodyType | Unset = UNSET
    order_type: PostV1MeAgentsIdOrdersBodyOrderType | Unset = UNSET
    limit_price: float | Unset = UNSET
    stop_price: float | Unset = UNSET
    trail_pct: float | Unset = UNSET
    time_in_force: PostV1MeAgentsIdOrdersBodyTimeInForce | Unset = UNSET
    reasoning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        side = self.side.value

        qty = self.qty

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        order_type: str | Unset = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.value

        limit_price = self.limit_price

        stop_price = self.stop_price

        trail_pct = self.trail_pct

        time_in_force: str | Unset = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force.value

        reasoning: None | str | Unset
        if isinstance(self.reasoning, Unset):
            reasoning = UNSET
        else:
            reasoning = self.reasoning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "side": side,
                "qty": qty,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if order_type is not UNSET:
            field_dict["order_type"] = order_type
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        side = PostV1MeAgentsIdOrdersBodySide(d.pop("side"))

        qty = d.pop("qty")

        _type_ = d.pop("type", UNSET)
        type_: PostV1MeAgentsIdOrdersBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostV1MeAgentsIdOrdersBodyType(_type_)

        _order_type = d.pop("order_type", UNSET)
        order_type: PostV1MeAgentsIdOrdersBodyOrderType | Unset
        if isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = PostV1MeAgentsIdOrdersBodyOrderType(_order_type)

        limit_price = d.pop("limit_price", UNSET)

        stop_price = d.pop("stop_price", UNSET)

        trail_pct = d.pop("trail_pct", UNSET)

        _time_in_force = d.pop("time_in_force", UNSET)
        time_in_force: PostV1MeAgentsIdOrdersBodyTimeInForce | Unset
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = PostV1MeAgentsIdOrdersBodyTimeInForce(_time_in_force)

        def _parse_reasoning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning = _parse_reasoning(d.pop("reasoning", UNSET))

        post_v1_me_agents_id_orders_body = cls(
            symbol=symbol,
            side=side,
            qty=qty,
            type_=type_,
            order_type=order_type,
            limit_price=limit_price,
            stop_price=stop_price,
            trail_pct=trail_pct,
            time_in_force=time_in_force,
            reasoning=reasoning,
        )

        post_v1_me_agents_id_orders_body.additional_properties = d
        return post_v1_me_agents_id_orders_body

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
