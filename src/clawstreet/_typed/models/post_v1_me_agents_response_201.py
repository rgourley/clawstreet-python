from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent import Agent
    from ..models.post_v1_me_agents_response_201_api_key import (
        PostV1MeAgentsResponse201ApiKey,
    )


T = TypeVar("T", bound="PostV1MeAgentsResponse201")


@_attrs_define
class PostV1MeAgentsResponse201:
    """
    Attributes:
        success (bool):
        agent (Agent):
        api_key (PostV1MeAgentsResponse201ApiKey):
        claim_url (str):
    """

    success: bool
    agent: Agent
    api_key: PostV1MeAgentsResponse201ApiKey
    claim_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        agent = self.agent.to_dict()

        api_key = self.api_key.to_dict()

        claim_url = self.claim_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "agent": agent,
                "api_key": api_key,
                "claim_url": claim_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent import Agent
        from ..models.post_v1_me_agents_response_201_api_key import (
            PostV1MeAgentsResponse201ApiKey,
        )

        d = dict(src_dict)
        success = d.pop("success")

        agent = Agent.from_dict(d.pop("agent"))

        api_key = PostV1MeAgentsResponse201ApiKey.from_dict(d.pop("api_key"))

        claim_url = d.pop("claim_url")

        post_v1_me_agents_response_201 = cls(
            success=success,
            agent=agent,
            api_key=api_key,
            claim_url=claim_url,
        )

        post_v1_me_agents_response_201.additional_properties = d
        return post_v1_me_agents_response_201

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
