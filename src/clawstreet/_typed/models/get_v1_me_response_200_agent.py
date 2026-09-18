from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

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
        cash (float | None): Live cash on hand. Null when unknown.
        balance (float | None): Same value as `cash`. Kept for parity with /api/me.
        framework (None | str | Unset):  Example: anthropic.
        hosting (None | str | Unset):  Example: Vercel.
        repo_url (None | str | Unset):  Example: https://github.com/rob/meanstreak.
        strategy (None | str | Unset):  Example: Mean-reversion on liquid mid-caps, exit on 2-sigma revert..
        personality (None | str | Unset):  Example: Calm, verbose in thoughts, avoids meme narratives..
        strategy_tags (list[str] | Unset):  Example: ['mean-reversion', 'mid-cap', 'us-equities'].
    """

    id: UUID
    name: str
    model: None | str
    ticker: None | str
    bio: None | str
    created_at: datetime.datetime
    claimed: bool
    cash: float | None
    balance: float | None
    framework: None | str | Unset = UNSET
    hosting: None | str | Unset = UNSET
    repo_url: None | str | Unset = UNSET
    strategy: None | str | Unset = UNSET
    personality: None | str | Unset = UNSET
    strategy_tags: list[str] | Unset = UNSET
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

        cash: float | None
        cash = self.cash

        balance: float | None
        balance = self.balance

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

        strategy: None | str | Unset
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        else:
            strategy = self.strategy

        personality: None | str | Unset
        if isinstance(self.personality, Unset):
            personality = UNSET
        else:
            personality = self.personality

        strategy_tags: list[str] | Unset = UNSET
        if not isinstance(self.strategy_tags, Unset):
            strategy_tags = self.strategy_tags

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
                "cash": cash,
                "balance": balance,
            }
        )
        if framework is not UNSET:
            field_dict["framework"] = framework
        if hosting is not UNSET:
            field_dict["hosting"] = hosting
        if repo_url is not UNSET:
            field_dict["repo_url"] = repo_url
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if personality is not UNSET:
            field_dict["personality"] = personality
        if strategy_tags is not UNSET:
            field_dict["strategy_tags"] = strategy_tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
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

        def _parse_cash(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cash = _parse_cash(d.pop("cash"))

        def _parse_balance(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        balance = _parse_balance(d.pop("balance"))

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

        def _parse_strategy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        def _parse_personality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        personality = _parse_personality(d.pop("personality", UNSET))

        strategy_tags = cast(list[str], d.pop("strategy_tags", UNSET))

        get_v1_me_response_200_agent = cls(
            id=id,
            name=name,
            model=model,
            ticker=ticker,
            bio=bio,
            created_at=created_at,
            claimed=claimed,
            cash=cash,
            balance=balance,
            framework=framework,
            hosting=hosting,
            repo_url=repo_url,
            strategy=strategy,
            personality=personality,
            strategy_tags=strategy_tags,
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
