from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_with_secret import ApiKeyWithSecret


T = TypeVar("T", bound="PostV1MeApiKeysIdRotateResponse200")


@_attrs_define
class PostV1MeApiKeysIdRotateResponse200:
    """
    Attributes:
        success (bool):
        api_key (ApiKeyWithSecret):
    """

    success: bool
    api_key: ApiKeyWithSecret
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        api_key = self.api_key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "api_key": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_with_secret import ApiKeyWithSecret

        d = dict(src_dict)
        success = d.pop("success")

        api_key = ApiKeyWithSecret.from_dict(d.pop("api_key"))

        post_v1_me_api_keys_id_rotate_response_200 = cls(
            success=success,
            api_key=api_key,
        )

        post_v1_me_api_keys_id_rotate_response_200.additional_properties = d
        return post_v1_me_api_keys_id_rotate_response_200

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
