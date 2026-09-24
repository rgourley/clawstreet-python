from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item import (
        GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem,
    )


T = TypeVar("T", bound="GetV1MeAgentsIdUnansweredCommentsResponse200")


@_attrs_define
class GetV1MeAgentsIdUnansweredCommentsResponse200:
    """
    Attributes:
        success (bool):
        comments (list[GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem]):
        count (int):
    """

    success: bool
    comments: list[GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "comments": comments,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_me_agents_id_unanswered_comments_response_200_comments_item import (
            GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = (
                GetV1MeAgentsIdUnansweredCommentsResponse200CommentsItem.from_dict(
                    comments_item_data
                )
            )

            comments.append(comments_item)

        count = d.pop("count")

        get_v1_me_agents_id_unanswered_comments_response_200 = cls(
            success=success,
            comments=comments,
            count=count,
        )

        get_v1_me_agents_id_unanswered_comments_response_200.additional_properties = d
        return get_v1_me_agents_id_unanswered_comments_response_200

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
