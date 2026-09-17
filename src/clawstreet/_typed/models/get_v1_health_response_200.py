from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_health_response_200_database import GetV1HealthResponse200Database

T = TypeVar("T", bound="GetV1HealthResponse200")


@_attrs_define
class GetV1HealthResponse200:
    """
    Attributes:
        success (bool):
        database (GetV1HealthResponse200Database):
        timestamp (datetime.datetime):
        market_open (bool): True during regular US equity hours, 9:30 to 16:00 ET on trading days. Crypto trades at all
            hours.
        next_open (datetime.datetime | None): ISO timestamp of the next market open. Null when the market is currently
            open.
        next_close (datetime.datetime | None): ISO timestamp of the next market close. Null when the market is currently
            closed.
    """

    success: bool
    database: GetV1HealthResponse200Database
    timestamp: datetime.datetime
    market_open: bool
    next_open: datetime.datetime | None
    next_close: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        database = self.database.value

        timestamp = self.timestamp.isoformat()

        market_open = self.market_open

        next_open: None | str
        if isinstance(self.next_open, datetime.datetime):
            next_open = self.next_open.isoformat()
        else:
            next_open = self.next_open

        next_close: None | str
        if isinstance(self.next_close, datetime.datetime):
            next_close = self.next_close.isoformat()
        else:
            next_close = self.next_close

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "database": database,
                "timestamp": timestamp,
                "market_open": market_open,
                "next_open": next_open,
                "next_close": next_close,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success = d.pop("success")

        database = GetV1HealthResponse200Database(d.pop("database"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        market_open = d.pop("market_open")

        def _parse_next_open(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_open_type_0 = datetime.datetime.fromisoformat(data)

                return next_open_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_open = _parse_next_open(d.pop("next_open"))

        def _parse_next_close(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_close_type_0 = datetime.datetime.fromisoformat(data)

                return next_close_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_close = _parse_next_close(d.pop("next_close"))

        get_v1_health_response_200 = cls(
            success=success,
            database=database,
            timestamp=timestamp,
            market_open=market_open,
            next_open=next_open,
            next_close=next_close,
        )

        get_v1_health_response_200.additional_properties = d
        return get_v1_health_response_200

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
