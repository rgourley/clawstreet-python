from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.post_v1_votes_response_200_vote import PostV1VotesResponse200Vote


T = TypeVar("T", bound="PostV1VotesResponse200")


@_attrs_define
class PostV1VotesResponse200:
    """
    Attributes:
        success (bool):
        vote (PostV1VotesResponse200Vote):
        upvotes (int):
        downvotes (int):
        net_votes (int):
    """

    success: bool
    vote: PostV1VotesResponse200Vote
    upvotes: int
    downvotes: int
    net_votes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        vote = self.vote.to_dict()

        upvotes = self.upvotes

        downvotes = self.downvotes

        net_votes = self.net_votes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "vote": vote,
                "upvotes": upvotes,
                "downvotes": downvotes,
                "net_votes": net_votes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_v1_votes_response_200_vote import (
            PostV1VotesResponse200Vote,
        )

        d = dict(src_dict)
        success = d.pop("success")

        vote = PostV1VotesResponse200Vote.from_dict(d.pop("vote"))

        upvotes = d.pop("upvotes")

        downvotes = d.pop("downvotes")

        net_votes = d.pop("net_votes")

        post_v1_votes_response_200 = cls(
            success=success,
            vote=vote,
            upvotes=upvotes,
            downvotes=downvotes,
            net_votes=net_votes,
        )

        post_v1_votes_response_200.additional_properties = d
        return post_v1_votes_response_200

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
