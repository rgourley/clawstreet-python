from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteV1MeAgentsIdResponse200")


@_attrs_define
class DeleteV1MeAgentsIdResponse200:
    """
    Attributes:
        success (bool):
        soft_deleted (UUID):
    """

    success: bool
    soft_deleted: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        soft_deleted = str(self.soft_deleted)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "soft_deleted": soft_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        soft_deleted = UUID(d.pop("soft_deleted"))

        delete_v1_me_agents_id_response_200 = cls(
            success=success,
            soft_deleted=soft_deleted,
        )

        delete_v1_me_agents_id_response_200.additional_properties = d
        return delete_v1_me_agents_id_response_200

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
