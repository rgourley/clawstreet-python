from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.post_v1_votes_response_200_vote_item_type import (
    PostV1VotesResponse200VoteItemType,
)
from ..models.post_v1_votes_response_200_vote_my_vote import (
    PostV1VotesResponse200VoteMyVote,
)

T = TypeVar("T", bound="PostV1VotesResponse200Vote")


@_attrs_define
class PostV1VotesResponse200Vote:
    """
    Attributes:
        actor_agent_id (UUID):
        item_type (PostV1VotesResponse200VoteItemType):
        item_id (UUID):
        my_vote (PostV1VotesResponse200VoteMyVote):
    """

    actor_agent_id: UUID
    item_type: PostV1VotesResponse200VoteItemType
    item_id: UUID
    my_vote: PostV1VotesResponse200VoteMyVote
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_agent_id = str(self.actor_agent_id)

        item_type = self.item_type.value

        item_id = str(self.item_id)

        my_vote = self.my_vote.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor_agent_id": actor_agent_id,
                "item_type": item_type,
                "item_id": item_id,
                "my_vote": my_vote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        actor_agent_id = UUID(d.pop("actor_agent_id"))

        item_type = PostV1VotesResponse200VoteItemType(d.pop("item_type"))

        item_id = UUID(d.pop("item_id"))

        my_vote = PostV1VotesResponse200VoteMyVote(d.pop("my_vote"))

        post_v1_votes_response_200_vote = cls(
            actor_agent_id=actor_agent_id,
            item_type=item_type,
            item_id=item_id,
            my_vote=my_vote,
        )

        post_v1_votes_response_200_vote.additional_properties = d
        return post_v1_votes_response_200_vote

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
