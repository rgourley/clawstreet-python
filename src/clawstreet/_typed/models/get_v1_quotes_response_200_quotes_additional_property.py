from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_quotes_response_200_quotes_additional_property_source import (
    GetV1QuotesResponse200QuotesAdditionalPropertySource,
)

T = TypeVar("T", bound="GetV1QuotesResponse200QuotesAdditionalProperty")


@_attrs_define
class GetV1QuotesResponse200QuotesAdditionalProperty:
    """
    Attributes:
        price (float):
        previous_close (float | None):
        change_pct (float | None):
        timestamp (datetime.datetime):
        as_of (datetime.datetime): Time of the price observation. Behind `timestamp` by about 15 minutes on delayed
            tiers.
        delayed (bool): True on tiers without real-time data. The price is the SIP-delayed last trade.
        source (GetV1QuotesResponse200QuotesAdditionalPropertySource):
        is_tradeable (bool): False when the symbol has a quote but is not in the tradeable universe. Orders to open a
            position in it are rejected with INVALID_SYMBOL.
        volume (float | None): Cumulative volume of the current session: shares for stocks, coins for crypto (UTC day).
            Stock volume is as of the SIP-delayed last trade on every tier, so it can lag `as_of` by about 15 minutes; read
            `volume_as_of`. Null when the session has no trades yet (weekend, holiday, before the first trade) or the
            snapshot has no row for the symbol. Example: 19438431.
        volume_as_of (datetime.datetime | None): Time of the snapshot that `volume` reflects. Null when `volume` is
            null.
        avg_volume_20d (float | None): Average daily volume over the 20 completed sessions before today, in the same
            unit as `volume`. Today's session is not included. Null when the symbol has fewer than 20 completed sessions or
            the history is not available. Example: 42235863.
    """

    price: float
    previous_close: float | None
    change_pct: float | None
    timestamp: datetime.datetime
    as_of: datetime.datetime
    delayed: bool
    source: GetV1QuotesResponse200QuotesAdditionalPropertySource
    is_tradeable: bool
    volume: float | None
    volume_as_of: datetime.datetime | None
    avg_volume_20d: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        previous_close: float | None
        previous_close = self.previous_close

        change_pct: float | None
        change_pct = self.change_pct

        timestamp = self.timestamp.isoformat()

        as_of = self.as_of.isoformat()

        delayed = self.delayed

        source = self.source.value

        is_tradeable = self.is_tradeable

        volume: float | None
        volume = self.volume

        volume_as_of: None | str
        if isinstance(self.volume_as_of, datetime.datetime):
            volume_as_of = self.volume_as_of.isoformat()
        else:
            volume_as_of = self.volume_as_of

        avg_volume_20d: float | None
        avg_volume_20d = self.avg_volume_20d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "previous_close": previous_close,
                "change_pct": change_pct,
                "timestamp": timestamp,
                "as_of": as_of,
                "delayed": delayed,
                "source": source,
                "is_tradeable": is_tradeable,
                "volume": volume,
                "volume_as_of": volume_as_of,
                "avg_volume_20d": avg_volume_20d,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        price = d.pop("price")

        def _parse_previous_close(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        previous_close = _parse_previous_close(d.pop("previous_close"))

        def _parse_change_pct(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        change_pct = _parse_change_pct(d.pop("change_pct"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        delayed = d.pop("delayed")

        source = GetV1QuotesResponse200QuotesAdditionalPropertySource(d.pop("source"))

        is_tradeable = d.pop("is_tradeable")

        def _parse_volume(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        volume = _parse_volume(d.pop("volume"))

        def _parse_volume_as_of(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                volume_as_of_type_0 = datetime.datetime.fromisoformat(data)

                return volume_as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        volume_as_of = _parse_volume_as_of(d.pop("volume_as_of"))

        def _parse_avg_volume_20d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_volume_20d = _parse_avg_volume_20d(d.pop("avg_volume_20d"))

        get_v1_quotes_response_200_quotes_additional_property = cls(
            price=price,
            previous_close=previous_close,
            change_pct=change_pct,
            timestamp=timestamp,
            as_of=as_of,
            delayed=delayed,
            source=source,
            is_tradeable=is_tradeable,
            volume=volume,
            volume_as_of=volume_as_of,
            avg_volume_20d=avg_volume_20d,
        )

        get_v1_quotes_response_200_quotes_additional_property.additional_properties = d
        return get_v1_quotes_response_200_quotes_additional_property

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
