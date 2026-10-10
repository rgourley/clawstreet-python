from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1MeResponse200Plan")


@_attrs_define
class GetV1MeResponse200Plan:
    """
    Attributes:
        name (str): Free, Plus, Pro, or "Launch access" while a launch trial supplies the tier. Example: Free.
        level (int): 0 Free, 1 Plus, 2 Pro.
        price (str):  Example: $0.
        realtime_data (bool):
        universe (str): free or full.
        crypto (str): none, btc, btc_eth or all.
        history_days (int):
        rate_limit_per_min (int):
        max_agents (int):
        versions (bool):
        private_agents (bool):
        journal (bool): Read `/v1/me/journal`. False on Free.
        alerts (bool): Alerts appear in the journal stream.
        weekly_review (bool): The weekly review appears in the journal stream.
        cloud_backup (bool): Read and write `/v1/me/artifacts`. False on Free.
        attribution (bool): Owner-facing performance breakdowns.
        trial_ends_at (None | str): When a launch trial supplies this tier, the moment it ends. Null otherwise.
        after_trial (None | str): The plan this key falls to when the trial ends. Null when there is no trial. Example:
            Free.
        upgrade_url (str):
    """

    name: str
    level: int
    price: str
    realtime_data: bool
    universe: str
    crypto: str
    history_days: int
    rate_limit_per_min: int
    max_agents: int
    versions: bool
    private_agents: bool
    journal: bool
    alerts: bool
    weekly_review: bool
    cloud_backup: bool
    attribution: bool
    trial_ends_at: None | str
    after_trial: None | str
    upgrade_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        level = self.level

        price = self.price

        realtime_data = self.realtime_data

        universe = self.universe

        crypto = self.crypto

        history_days = self.history_days

        rate_limit_per_min = self.rate_limit_per_min

        max_agents = self.max_agents

        versions = self.versions

        private_agents = self.private_agents

        journal = self.journal

        alerts = self.alerts

        weekly_review = self.weekly_review

        cloud_backup = self.cloud_backup

        attribution = self.attribution

        trial_ends_at: None | str
        trial_ends_at = self.trial_ends_at

        after_trial: None | str
        after_trial = self.after_trial

        upgrade_url = self.upgrade_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "level": level,
                "price": price,
                "realtime_data": realtime_data,
                "universe": universe,
                "crypto": crypto,
                "history_days": history_days,
                "rate_limit_per_min": rate_limit_per_min,
                "max_agents": max_agents,
                "versions": versions,
                "private_agents": private_agents,
                "journal": journal,
                "alerts": alerts,
                "weekly_review": weekly_review,
                "cloud_backup": cloud_backup,
                "attribution": attribution,
                "trial_ends_at": trial_ends_at,
                "after_trial": after_trial,
                "upgrade_url": upgrade_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        level = d.pop("level")

        price = d.pop("price")

        realtime_data = d.pop("realtime_data")

        universe = d.pop("universe")

        crypto = d.pop("crypto")

        history_days = d.pop("history_days")

        rate_limit_per_min = d.pop("rate_limit_per_min")

        max_agents = d.pop("max_agents")

        versions = d.pop("versions")

        private_agents = d.pop("private_agents")

        journal = d.pop("journal")

        alerts = d.pop("alerts")

        weekly_review = d.pop("weekly_review")

        cloud_backup = d.pop("cloud_backup")

        attribution = d.pop("attribution")

        def _parse_trial_ends_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        trial_ends_at = _parse_trial_ends_at(d.pop("trial_ends_at"))

        def _parse_after_trial(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        after_trial = _parse_after_trial(d.pop("after_trial"))

        upgrade_url = d.pop("upgrade_url")

        get_v1_me_response_200_plan = cls(
            name=name,
            level=level,
            price=price,
            realtime_data=realtime_data,
            universe=universe,
            crypto=crypto,
            history_days=history_days,
            rate_limit_per_min=rate_limit_per_min,
            max_agents=max_agents,
            versions=versions,
            private_agents=private_agents,
            journal=journal,
            alerts=alerts,
            weekly_review=weekly_review,
            cloud_backup=cloud_backup,
            attribution=attribution,
            trial_ends_at=trial_ends_at,
            after_trial=after_trial,
            upgrade_url=upgrade_url,
        )

        get_v1_me_response_200_plan.additional_properties = d
        return get_v1_me_response_200_plan

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
