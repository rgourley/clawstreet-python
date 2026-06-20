from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order import Order
    from ..models.position import Position


T = TypeVar("T", bound="GetV1MeAgentsIdIterateResponse200Preview")


@_attrs_define
class GetV1MeAgentsIdIterateResponse200Preview:
    """
    Attributes:
        open_positions (list[Position]):
        pending_orders (list[Order]):
        estimated_flatten_value (float):
        estimated_realized_pnl (float):
    """

    open_positions: list[Position]
    pending_orders: list[Order]
    estimated_flatten_value: float
    estimated_realized_pnl: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_positions = []
        for open_positions_item_data in self.open_positions:
            open_positions_item = open_positions_item_data.to_dict()
            open_positions.append(open_positions_item)

        pending_orders = []
        for pending_orders_item_data in self.pending_orders:
            pending_orders_item = pending_orders_item_data.to_dict()
            pending_orders.append(pending_orders_item)

        estimated_flatten_value = self.estimated_flatten_value

        estimated_realized_pnl = self.estimated_realized_pnl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "openPositions": open_positions,
                "pendingOrders": pending_orders,
                "estimatedFlattenValue": estimated_flatten_value,
                "estimatedRealizedPnl": estimated_realized_pnl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order import Order
        from ..models.position import Position

        d = dict(src_dict)
        open_positions = []
        _open_positions = d.pop("openPositions")
        for open_positions_item_data in _open_positions:
            open_positions_item = Position.from_dict(open_positions_item_data)

            open_positions.append(open_positions_item)

        pending_orders = []
        _pending_orders = d.pop("pendingOrders")
        for pending_orders_item_data in _pending_orders:
            pending_orders_item = Order.from_dict(pending_orders_item_data)

            pending_orders.append(pending_orders_item)

        estimated_flatten_value = d.pop("estimatedFlattenValue")

        estimated_realized_pnl = d.pop("estimatedRealizedPnl")

        get_v1_me_agents_id_iterate_response_200_preview = cls(
            open_positions=open_positions,
            pending_orders=pending_orders,
            estimated_flatten_value=estimated_flatten_value,
            estimated_realized_pnl=estimated_realized_pnl,
        )

        get_v1_me_agents_id_iterate_response_200_preview.additional_properties = d
        return get_v1_me_agents_id_iterate_response_200_preview

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
