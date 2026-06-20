from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_me_usage_response_200_by_day_item_by_endpoint import (
        GetV1MeUsageResponse200ByDayItemByEndpoint,
    )


T = TypeVar("T", bound="GetV1MeUsageResponse200ByDayItem")


@_attrs_define
class GetV1MeUsageResponse200ByDayItem:
    """
    Attributes:
        date (str):
        calls (float):
        by_endpoint (GetV1MeUsageResponse200ByDayItemByEndpoint):
    """

    date: str
    calls: float
    by_endpoint: GetV1MeUsageResponse200ByDayItemByEndpoint
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        calls = self.calls

        by_endpoint = self.by_endpoint.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "calls": calls,
                "by_endpoint": by_endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_me_usage_response_200_by_day_item_by_endpoint import (
            GetV1MeUsageResponse200ByDayItemByEndpoint,
        )

        d = dict(src_dict)
        date = d.pop("date")

        calls = d.pop("calls")

        by_endpoint = GetV1MeUsageResponse200ByDayItemByEndpoint.from_dict(
            d.pop("by_endpoint")
        )

        get_v1_me_usage_response_200_by_day_item = cls(
            date=date,
            calls=calls,
            by_endpoint=by_endpoint,
        )

        get_v1_me_usage_response_200_by_day_item.additional_properties = d
        return get_v1_me_usage_response_200_by_day_item

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
