from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MeAgentsBody")


@_attrs_define
class PostV1MeAgentsBody:
    """
    Attributes:
        name (str):
        ticker (str | Unset):
        model (None | str | Unset):
        bio (None | str | Unset):
        framework (None | str | Unset):
        owner_email (str | Unset):
    """

    name: str
    ticker: str | Unset = UNSET
    model: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    framework: None | str | Unset = UNSET
    owner_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ticker = self.ticker

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        framework: None | str | Unset
        if isinstance(self.framework, Unset):
            framework = UNSET
        else:
            framework = self.framework

        owner_email = self.owner_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if model is not UNSET:
            field_dict["model"] = model
        if bio is not UNSET:
            field_dict["bio"] = bio
        if framework is not UNSET:
            field_dict["framework"] = framework
        if owner_email is not UNSET:
            field_dict["owner_email"] = owner_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        ticker = d.pop("ticker", UNSET)

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_framework(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        framework = _parse_framework(d.pop("framework", UNSET))

        owner_email = d.pop("owner_email", UNSET)

        post_v1_me_agents_body = cls(
            name=name,
            ticker=ticker,
            model=model,
            bio=bio,
            framework=framework,
            owner_email=owner_email,
        )

        post_v1_me_agents_body.additional_properties = d
        return post_v1_me_agents_body

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
