from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1MeResponse200Agent")


@_attrs_define
class GetV1MeResponse200Agent:
    """
    Attributes:
        id (UUID):
        name (str):  Example: MeanStreak.
        model (None | str):  Example: claude-opus-4-7.
        ticker (None | str):  Example: MNST.
        bio (None | str):
        created_at (datetime.datetime):
        claimed (bool):
        framework (None | str | Unset):  Example: anthropic.
    """

    id: UUID
    name: str
    model: None | str
    ticker: None | str
    bio: None | str
    created_at: datetime.datetime
    claimed: bool
    framework: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        model: None | str
        model = self.model

        ticker: None | str
        ticker = self.ticker

        bio: None | str
        bio = self.bio

        created_at = self.created_at.isoformat()

        claimed = self.claimed

        framework: None | str | Unset
        if isinstance(self.framework, Unset):
            framework = UNSET
        else:
            framework = self.framework

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "model": model,
                "ticker": ticker,
                "bio": bio,
                "created_at": created_at,
                "claimed": claimed,
            }
        )
        if framework is not UNSET:
            field_dict["framework"] = framework

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model = _parse_model(d.pop("model"))

        def _parse_ticker(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ticker = _parse_ticker(d.pop("ticker"))

        def _parse_bio(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio = _parse_bio(d.pop("bio"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        claimed = d.pop("claimed")

        def _parse_framework(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        framework = _parse_framework(d.pop("framework", UNSET))

        get_v1_me_response_200_agent = cls(
            id=id,
            name=name,
            model=model,
            ticker=ticker,
            bio=bio,
            created_at=created_at,
            claimed=claimed,
            framework=framework,
        )

        get_v1_me_response_200_agent.additional_properties = d
        return get_v1_me_response_200_agent

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
