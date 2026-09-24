from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_me_response_200_agent import GetV1MeResponse200Agent
    from ..models.get_v1_me_response_200_plan import GetV1MeResponse200Plan


T = TypeVar("T", bound="GetV1MeResponse200")


@_attrs_define
class GetV1MeResponse200:
    """
    Attributes:
        success (bool):
        agent (GetV1MeResponse200Agent):
        scopes (list[str]):
        plan (GetV1MeResponse200Plan):
    """

    success: bool
    agent: GetV1MeResponse200Agent
    scopes: list[str]
    plan: GetV1MeResponse200Plan
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        agent = self.agent.to_dict()

        scopes = self.scopes

        plan = self.plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "agent": agent,
                "scopes": scopes,
                "plan": plan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_me_response_200_agent import (
            GetV1MeResponse200Agent,
        )
        from ..models.get_v1_me_response_200_plan import (
            GetV1MeResponse200Plan,
        )

        d = dict(src_dict)
        success = d.pop("success")

        agent = GetV1MeResponse200Agent.from_dict(d.pop("agent"))

        scopes = cast(list[str], d.pop("scopes"))

        plan = GetV1MeResponse200Plan.from_dict(d.pop("plan"))

        get_v1_me_response_200 = cls(
            success=success,
            agent=agent,
            scopes=scopes,
            plan=plan,
        )

        get_v1_me_response_200.additional_properties = d
        return get_v1_me_response_200

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
