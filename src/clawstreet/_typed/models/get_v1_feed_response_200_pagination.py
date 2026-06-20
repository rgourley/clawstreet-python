from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1FeedResponse200Pagination")


@_attrs_define
class GetV1FeedResponse200Pagination:
    """
    Attributes:
        offset (float):
        limit (float):
        has_more (bool):
        total (float):
    """

    offset: float
    limit: float
    has_more: bool
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        has_more = self.has_more

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "hasMore": has_more,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        has_more = d.pop("hasMore")

        total = d.pop("total")

        get_v1_feed_response_200_pagination = cls(
            offset=offset,
            limit=limit,
            has_more=has_more,
            total=total,
        )

        get_v1_feed_response_200_pagination.additional_properties = d
        return get_v1_feed_response_200_pagination

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
