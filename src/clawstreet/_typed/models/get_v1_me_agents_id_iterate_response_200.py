from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_me_agents_id_iterate_response_200_preview import (
        GetV1MeAgentsIdIterateResponse200Preview,
    )


T = TypeVar("T", bound="GetV1MeAgentsIdIterateResponse200")


@_attrs_define
class GetV1MeAgentsIdIterateResponse200:
    """
    Attributes:
        success (bool):
        preview (GetV1MeAgentsIdIterateResponse200Preview):
    """

    success: bool
    preview: GetV1MeAgentsIdIterateResponse200Preview
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        preview = self.preview.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "preview": preview,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_me_agents_id_iterate_response_200_preview import (
            GetV1MeAgentsIdIterateResponse200Preview,
        )

        d = dict(src_dict)
        success = d.pop("success")

        preview = GetV1MeAgentsIdIterateResponse200Preview.from_dict(d.pop("preview"))

        get_v1_me_agents_id_iterate_response_200 = cls(
            success=success,
            preview=preview,
        )

        get_v1_me_agents_id_iterate_response_200.additional_properties = d
        return get_v1_me_agents_id_iterate_response_200

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
