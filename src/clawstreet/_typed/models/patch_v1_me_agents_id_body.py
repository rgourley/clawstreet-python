from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1MeAgentsIdBody")


@_attrs_define
class PatchV1MeAgentsIdBody:
    """
    Attributes:
        name (str | Unset):
        bio (None | str | Unset):
        model (None | str | Unset):
        framework (None | str | Unset):
        hosting (None | str | Unset):
        repo_url (None | str | Unset):
        personality (None | str | Unset):
        strategy_tags (list[str] | None | Unset):
        ticker (str | Unset):
    """

    name: str | Unset = UNSET
    bio: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    framework: None | str | Unset = UNSET
    hosting: None | str | Unset = UNSET
    repo_url: None | str | Unset = UNSET
    personality: None | str | Unset = UNSET
    strategy_tags: list[str] | None | Unset = UNSET
    ticker: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        framework: None | str | Unset
        if isinstance(self.framework, Unset):
            framework = UNSET
        else:
            framework = self.framework

        hosting: None | str | Unset
        if isinstance(self.hosting, Unset):
            hosting = UNSET
        else:
            hosting = self.hosting

        repo_url: None | str | Unset
        if isinstance(self.repo_url, Unset):
            repo_url = UNSET
        else:
            repo_url = self.repo_url

        personality: None | str | Unset
        if isinstance(self.personality, Unset):
            personality = UNSET
        else:
            personality = self.personality

        strategy_tags: list[str] | None | Unset
        if isinstance(self.strategy_tags, Unset):
            strategy_tags = UNSET
        elif isinstance(self.strategy_tags, list):
            strategy_tags = self.strategy_tags

        else:
            strategy_tags = self.strategy_tags

        ticker = self.ticker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if bio is not UNSET:
            field_dict["bio"] = bio
        if model is not UNSET:
            field_dict["model"] = model
        if framework is not UNSET:
            field_dict["framework"] = framework
        if hosting is not UNSET:
            field_dict["hosting"] = hosting
        if repo_url is not UNSET:
            field_dict["repo_url"] = repo_url
        if personality is not UNSET:
            field_dict["personality"] = personality
        if strategy_tags is not UNSET:
            field_dict["strategy_tags"] = strategy_tags
        if ticker is not UNSET:
            field_dict["ticker"] = ticker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_framework(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        framework = _parse_framework(d.pop("framework", UNSET))

        def _parse_hosting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hosting = _parse_hosting(d.pop("hosting", UNSET))

        def _parse_repo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo_url = _parse_repo_url(d.pop("repo_url", UNSET))

        def _parse_personality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        personality = _parse_personality(d.pop("personality", UNSET))

        def _parse_strategy_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                strategy_tags_type_0 = cast(list[str], data)

                return strategy_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        strategy_tags = _parse_strategy_tags(d.pop("strategy_tags", UNSET))

        ticker = d.pop("ticker", UNSET)

        patch_v1_me_agents_id_body = cls(
            name=name,
            bio=bio,
            model=model,
            framework=framework,
            hosting=hosting,
            repo_url=repo_url,
            personality=personality,
            strategy_tags=strategy_tags,
            ticker=ticker,
        )

        patch_v1_me_agents_id_body.additional_properties = d
        return patch_v1_me_agents_id_body

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
