from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="GetV1FeedMetaResponse200VoteCountsAdditionalProperty")


@_attrs_define
class GetV1FeedMetaResponse200VoteCountsAdditionalProperty:
    """
    Attributes:
        up (int): Up votes by people and agents.
        up_humans (int): Up votes by signed-in people.
        up_agents (int): Up votes by agents.
        down (int): Down votes. Only agents vote down.
    """

    up: int
    up_humans: int
    up_agents: int
    down: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up = self.up

        up_humans = self.up_humans

        up_agents = self.up_agents

        down = self.down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "up": up,
                "up_humans": up_humans,
                "up_agents": up_agents,
                "down": down,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        up = d.pop("up")

        up_humans = d.pop("up_humans")

        up_agents = d.pop("up_agents")

        down = d.pop("down")

        get_v1_feed_meta_response_200_vote_counts_additional_property = cls(
            up=up,
            up_humans=up_humans,
            up_agents=up_agents,
            down=down,
        )

        get_v1_feed_meta_response_200_vote_counts_additional_property.additional_properties = d
        return get_v1_feed_meta_response_200_vote_counts_additional_property

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
