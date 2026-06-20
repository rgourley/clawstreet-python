from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.margin_event_event_type import MarginEventEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarginEvent")


@_attrs_define
class MarginEvent:
    """
    Attributes:
        id (UUID):
        event_type (MarginEventEventType):
        equity_at_event (float):
        maintenance_required (float):
        created_at (datetime.datetime):
        positions_liquidated (Any | Unset):
    """

    id: UUID
    event_type: MarginEventEventType
    equity_at_event: float
    maintenance_required: float
    created_at: datetime.datetime
    positions_liquidated: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        event_type = self.event_type.value

        equity_at_event = self.equity_at_event

        maintenance_required = self.maintenance_required

        created_at = self.created_at.isoformat()

        positions_liquidated = self.positions_liquidated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_type": event_type,
                "equity_at_event": equity_at_event,
                "maintenance_required": maintenance_required,
                "created_at": created_at,
            }
        )
        if positions_liquidated is not UNSET:
            field_dict["positions_liquidated"] = positions_liquidated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        event_type = MarginEventEventType(d.pop("event_type"))

        equity_at_event = d.pop("equity_at_event")

        maintenance_required = d.pop("maintenance_required")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        positions_liquidated = d.pop("positions_liquidated", UNSET)

        margin_event = cls(
            id=id,
            event_type=event_type,
            equity_at_event=equity_at_event,
            maintenance_required=maintenance_required,
            created_at=created_at,
            positions_liquidated=positions_liquidated,
        )

        margin_event.additional_properties = d
        return margin_event

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
