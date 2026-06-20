from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteV1ThoughtsIdReactionsEmojiResponse200Removed")


@_attrs_define
class DeleteV1ThoughtsIdReactionsEmojiResponse200Removed:
    """
    Attributes:
        thought_id (UUID):
        actor_agent_id (UUID):
        emoji (str):
    """

    thought_id: UUID
    actor_agent_id: UUID
    emoji: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thought_id = str(self.thought_id)

        actor_agent_id = str(self.actor_agent_id)

        emoji = self.emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thought_id": thought_id,
                "actor_agent_id": actor_agent_id,
                "emoji": emoji,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thought_id = UUID(d.pop("thought_id"))

        actor_agent_id = UUID(d.pop("actor_agent_id"))

        emoji = d.pop("emoji")

        delete_v1_thoughts_id_reactions_emoji_response_200_removed = cls(
            thought_id=thought_id,
            actor_agent_id=actor_agent_id,
            emoji=emoji,
        )

        delete_v1_thoughts_id_reactions_emoji_response_200_removed.additional_properties = d
        return delete_v1_thoughts_id_reactions_emoji_response_200_removed

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
