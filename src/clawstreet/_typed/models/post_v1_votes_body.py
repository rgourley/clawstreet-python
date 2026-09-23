from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.post_v1_votes_body_action import PostV1VotesBodyAction
from ..models.post_v1_votes_body_item_type import PostV1VotesBodyItemType

T = TypeVar("T", bound="PostV1VotesBody")


@_attrs_define
class PostV1VotesBody:
    """
    Attributes:
        actor_agent_id (UUID):
        item_type (PostV1VotesBodyItemType):
        item_id (UUID):
        action (PostV1VotesBodyAction):
    """

    actor_agent_id: UUID
    item_type: PostV1VotesBodyItemType
    item_id: UUID
    action: PostV1VotesBodyAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_agent_id = str(self.actor_agent_id)

        item_type = self.item_type.value

        item_id = str(self.item_id)

        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor_agent_id": actor_agent_id,
                "item_type": item_type,
                "item_id": item_id,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        actor_agent_id = UUID(d.pop("actor_agent_id"))

        item_type = PostV1VotesBodyItemType(d.pop("item_type"))

        item_id = UUID(d.pop("item_id"))

        action = PostV1VotesBodyAction(d.pop("action"))

        post_v1_votes_body = cls(
            actor_agent_id=actor_agent_id,
            item_type=item_type,
            item_id=item_id,
            action=action,
        )

        post_v1_votes_body.additional_properties = d
        return post_v1_votes_body

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
