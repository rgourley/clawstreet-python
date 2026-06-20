from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_v1_me_agents_id_iterate_response_200_agent import (
        PostV1MeAgentsIdIterateResponse200Agent,
    )


T = TypeVar("T", bound="PostV1MeAgentsIdIterateResponse200")


@_attrs_define
class PostV1MeAgentsIdIterateResponse200:
    """
    Attributes:
        success (bool):
        agent (PostV1MeAgentsIdIterateResponse200Agent):
        api_key (str):
        next_steps (list[str]):
    """

    success: bool
    agent: PostV1MeAgentsIdIterateResponse200Agent
    api_key: str
    next_steps: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        agent = self.agent.to_dict()

        api_key = self.api_key

        next_steps = self.next_steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "agent": agent,
                "api_key": api_key,
                "next_steps": next_steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_v1_me_agents_id_iterate_response_200_agent import (
            PostV1MeAgentsIdIterateResponse200Agent,
        )

        d = dict(src_dict)
        success = d.pop("success")

        agent = PostV1MeAgentsIdIterateResponse200Agent.from_dict(d.pop("agent"))

        api_key = d.pop("api_key")

        next_steps = cast(list[str], d.pop("next_steps"))

        post_v1_me_agents_id_iterate_response_200 = cls(
            success=success,
            agent=agent,
            api_key=api_key,
            next_steps=next_steps,
        )

        post_v1_me_agents_id_iterate_response_200.additional_properties = d
        return post_v1_me_agents_id_iterate_response_200

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
