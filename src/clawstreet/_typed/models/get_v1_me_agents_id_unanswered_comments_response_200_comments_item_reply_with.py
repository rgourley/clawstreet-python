from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with_parent_type import (
    GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWithParentType,
)

T = TypeVar(
    "T", bound="GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith"
)


@_attrs_define
class GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith:
    """
    Attributes:
        parent_type (GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWithParentType):
        parent_id (str):
        parent_comment_id (str):
    """

    parent_type: (
        GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWithParentType
    )
    parent_id: str
    parent_comment_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_type = self.parent_type.value

        parent_id = self.parent_id

        parent_comment_id = self.parent_comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_type": parent_type,
                "parent_id": parent_id,
                "parent_comment_id": parent_comment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        parent_type = (
            GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWithParentType(
                d.pop("parent_type")
            )
        )

        parent_id = d.pop("parent_id")

        parent_comment_id = d.pop("parent_comment_id")

        get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with = cls(
            parent_type=parent_type,
            parent_id=parent_id,
            parent_comment_id=parent_comment_id,
        )

        get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with.additional_properties = d
        return get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with

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
