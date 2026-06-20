from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1Response200RateLimit")


@_attrs_define
class GetV1Response200RateLimit:
    """
    Attributes:
        default_requests (float):
        default_window_seconds (float):
        note (str):
    """

    default_requests: float
    default_window_seconds: float
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_requests = self.default_requests

        default_window_seconds = self.default_window_seconds

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_requests": default_requests,
                "default_window_seconds": default_window_seconds,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_requests = d.pop("default_requests")

        default_window_seconds = d.pop("default_window_seconds")

        note = d.pop("note")

        get_v1_response_200_rate_limit = cls(
            default_requests=default_requests,
            default_window_seconds=default_window_seconds,
            note=note,
        )

        get_v1_response_200_rate_limit.additional_properties = d
        return get_v1_response_200_rate_limit

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
