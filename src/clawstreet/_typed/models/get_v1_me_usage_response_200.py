from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_me_usage_response_200_by_day_item import (
        GetV1MeUsageResponse200ByDayItem,
    )


T = TypeVar("T", bound="GetV1MeUsageResponse200")


@_attrs_define
class GetV1MeUsageResponse200:
    """
    Attributes:
        success (bool):
        period (str):
        total_calls (float):
        by_day (list[GetV1MeUsageResponse200ByDayItem]):
    """

    success: bool
    period: str
    total_calls: float
    by_day: list[GetV1MeUsageResponse200ByDayItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        period = self.period

        total_calls = self.total_calls

        by_day = []
        for by_day_item_data in self.by_day:
            by_day_item = by_day_item_data.to_dict()
            by_day.append(by_day_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "period": period,
                "total_calls": total_calls,
                "by_day": by_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_me_usage_response_200_by_day_item import (
            GetV1MeUsageResponse200ByDayItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        period = d.pop("period")

        total_calls = d.pop("total_calls")

        by_day = []
        _by_day = d.pop("by_day")
        for by_day_item_data in _by_day:
            by_day_item = GetV1MeUsageResponse200ByDayItem.from_dict(by_day_item_data)

            by_day.append(by_day_item)

        get_v1_me_usage_response_200 = cls(
            success=success,
            period=period,
            total_calls=total_calls,
            by_day=by_day,
        )

        get_v1_me_usage_response_200.additional_properties = d
        return get_v1_me_usage_response_200

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
