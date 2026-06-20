from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_health_response_200_database import GetV1HealthResponse200Database

T = TypeVar("T", bound="GetV1HealthResponse200")


@_attrs_define
class GetV1HealthResponse200:
    """
    Attributes:
        success (bool):
        database (GetV1HealthResponse200Database):
        timestamp (datetime.datetime):
    """

    success: bool
    database: GetV1HealthResponse200Database
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        database = self.database.value

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "database": database,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        database = GetV1HealthResponse200Database(d.pop("database"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        get_v1_health_response_200 = cls(
            success=success,
            database=database,
            timestamp=timestamp,
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
