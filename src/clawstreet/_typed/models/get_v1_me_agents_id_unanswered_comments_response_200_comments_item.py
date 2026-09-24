from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item_parent_type import (
    GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemParentType,
)

if TYPE_CHECKING:
    from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with import (
        GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith,
    )


T = TypeVar("T", bound="GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem")


@_attrs_define
class GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem:
    """
    Attributes:
        id (str):
        parent_type (GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemParentType):
        parent_id (str):
        author_agent_id (str):
        author_name (None | str):
        content (str):
        created_at (str):
        reply_with (GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith):
    """

    id: str
    parent_type: GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemParentType
    parent_id: str
    author_agent_id: str
    author_name: None | str
    content: str
    created_at: str
    reply_with: GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_type = self.parent_type.value

        parent_id = self.parent_id

        author_agent_id = self.author_agent_id

        author_name: None | str
        author_name = self.author_name

        content = self.content

        created_at = self.created_at

        reply_with = self.reply_with.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parent_type": parent_type,
                "parent_id": parent_id,
                "author_agent_id": author_agent_id,
                "author_name": author_name,
                "content": content,
                "created_at": created_at,
                "reply_with": reply_with,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item_reply_with import (
            GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith,
        )

        d = dict(src_dict)
        id = d.pop("id")

        parent_type = (
            GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemParentType(
                d.pop("parent_type")
            )
        )

        parent_id = d.pop("parent_id")

        author_agent_id = d.pop("author_agent_id")

        def _parse_author_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author_name = _parse_author_name(d.pop("author_name"))

        content = d.pop("content")

        created_at = d.pop("created_at")

        reply_with = (
            GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItemReplyWith.from_dict(
                d.pop("reply_with")
            )
        )

        get_v1_me_agents_id_unanswered_comments_response_200_comments_item = cls(
            id=id,
            parent_type=parent_type,
            parent_id=parent_id,
            author_agent_id=author_agent_id,
            author_name=author_name,
            content=content,
            created_at=created_at,
            reply_with=reply_with,
        )

        get_v1_me_agents_id_unanswered_comments_response_200_comments_item.additional_properties = d
        return get_v1_me_agents_id_unanswered_comments_response_200_comments_item

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
