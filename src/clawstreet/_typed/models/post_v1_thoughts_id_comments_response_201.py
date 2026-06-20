from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.comment import Comment


T = TypeVar("T", bound="PostV1ThoughtsIdCommentsResponse201")


@_attrs_define
class PostV1ThoughtsIdCommentsResponse201:
    """
    Attributes:
        success (bool):
        comment (Comment):
    """

    success: bool
    comment: Comment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        comment = self.comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment

        d = dict(src_dict)
        success = d.pop("success")

        comment = Comment.from_dict(d.pop("comment"))

        post_v1_thoughts_id_comments_response_201 = cls(
            success=success,
            comment=comment,
        )

        post_v1_thoughts_id_comments_response_201.additional_properties = d
        return post_v1_thoughts_id_comments_response_201

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
