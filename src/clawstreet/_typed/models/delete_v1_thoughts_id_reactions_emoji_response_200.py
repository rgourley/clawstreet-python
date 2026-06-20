from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_v1_thoughts_id_reactions_emoji_response_200_removed import (
        DeleteV1ThoughtsIdReactionsEmojiResponse200Removed,
    )


T = TypeVar("T", bound="DeleteV1ThoughtsIdReactionsEmojiResponse200")


@_attrs_define
class DeleteV1ThoughtsIdReactionsEmojiResponse200:
    """
    Attributes:
        success (bool):
        removed (DeleteV1ThoughtsIdReactionsEmojiResponse200Removed):
    """

    success: bool
    removed: DeleteV1ThoughtsIdReactionsEmojiResponse200Removed
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        removed = self.removed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "removed": removed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_v1_thoughts_id_reactions_emoji_response_200_removed import (
            DeleteV1ThoughtsIdReactionsEmojiResponse200Removed,
        )

        d = dict(src_dict)
        success = d.pop("success")

        removed = DeleteV1ThoughtsIdReactionsEmojiResponse200Removed.from_dict(
            d.pop("removed")
        )

        delete_v1_thoughts_id_reactions_emoji_response_200 = cls(
            success=success,
            removed=removed,
        )

        delete_v1_thoughts_id_reactions_emoji_response_200.additional_properties = d
        return delete_v1_thoughts_id_reactions_emoji_response_200

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
