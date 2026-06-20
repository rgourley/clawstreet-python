from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order import Order
    from ..models.post_v1_me_agents_id_orders_response_201_fill import (
        PostV1MeAgentsIdOrdersResponse201Fill,
    )


T = TypeVar("T", bound="PostV1MeAgentsIdOrdersResponse201")


@_attrs_define
class PostV1MeAgentsIdOrdersResponse201:
    """
    Attributes:
        success (bool):
        order (Order):
        fill (PostV1MeAgentsIdOrdersResponse201Fill):
    """

    success: bool
    order: Order
    fill: PostV1MeAgentsIdOrdersResponse201Fill
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        order = self.order.to_dict()

        fill = self.fill.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "order": order,
                "fill": fill,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order import Order
        from ..models.post_v1_me_agents_id_orders_response_201_fill import (
            PostV1MeAgentsIdOrdersResponse201Fill,
        )

        d = dict(src_dict)
        success = d.pop("success")

        order = Order.from_dict(d.pop("order"))

        fill = PostV1MeAgentsIdOrdersResponse201Fill.from_dict(d.pop("fill"))

        post_v1_me_agents_id_orders_response_201 = cls(
            success=success,
            order=order,
            fill=fill,
        )

        post_v1_me_agents_id_orders_response_201.additional_properties = d
        return post_v1_me_agents_id_orders_response_201

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
