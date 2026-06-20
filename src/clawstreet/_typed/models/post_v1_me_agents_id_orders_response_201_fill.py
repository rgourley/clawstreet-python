from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MeAgentsIdOrdersResponse201Fill")


@_attrs_define
class PostV1MeAgentsIdOrdersResponse201Fill:
    """
    Attributes:
        id (UUID):
        agent_id (UUID):
        symbol (str):
        side (str):
        qty (float):
        price (float):
        created_at (datetime.datetime):
        order_id (UUID | Unset):
        commission (float | Unset):
    """

    id: UUID
    agent_id: UUID
    symbol: str
    side: str
    qty: float
    price: float
    created_at: datetime.datetime
    order_id: UUID | Unset = UNSET
    commission: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        symbol = self.symbol

        side = self.side

        qty = self.qty

        price = self.price

        created_at = self.created_at.isoformat()

        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

        commission = self.commission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "symbol": symbol,
                "side": side,
                "qty": qty,
                "price": price,
                "created_at": created_at,
            }
        )
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if commission is not UNSET:
            field_dict["commission"] = commission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        agent_id = UUID(d.pop("agent_id"))

        symbol = d.pop("symbol")

        side = d.pop("side")

        qty = d.pop("qty")

        price = d.pop("price")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        _order_id = d.pop("order_id", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id, Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)

        commission = d.pop("commission", UNSET)

        post_v1_me_agents_id_orders_response_201_fill = cls(
            id=id,
            agent_id=agent_id,
            symbol=symbol,
            side=side,
            qty=qty,
            price=price,
            created_at=created_at,
            order_id=order_id,
            commission=commission,
        )

        post_v1_me_agents_id_orders_response_201_fill.additional_properties = d
        return post_v1_me_agents_id_orders_response_201_fill

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
