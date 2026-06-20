from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_feed_response_200_items_item import (
        GetV1FeedResponse200ItemsItem,
    )
    from ..models.get_v1_feed_response_200_pagination import (
        GetV1FeedResponse200Pagination,
    )


T = TypeVar("T", bound="GetV1FeedResponse200")


@_attrs_define
class GetV1FeedResponse200:
    """
    Attributes:
        success (bool):
        items (list[GetV1FeedResponse200ItemsItem]):
        sort (str):
        period (str):
        pagination (GetV1FeedResponse200Pagination):
    """

    success: bool
    items: list[GetV1FeedResponse200ItemsItem]
    sort: str
    period: str
    pagination: GetV1FeedResponse200Pagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        sort = self.sort

        period = self.period

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "items": items,
                "sort": sort,
                "period": period,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_feed_response_200_items_item import (
            GetV1FeedResponse200ItemsItem,
        )
        from ..models.get_v1_feed_response_200_pagination import (
            GetV1FeedResponse200Pagination,
        )

        d = dict(src_dict)
        success = d.pop("success")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GetV1FeedResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        sort = d.pop("sort")

        period = d.pop("period")

        pagination = GetV1FeedResponse200Pagination.from_dict(d.pop("pagination"))

        get_v1_feed_response_200 = cls(
            success=success,
            items=items,
            sort=sort,
            period=period,
            pagination=pagination,
        )

        get_v1_feed_response_200.additional_properties = d
        return get_v1_feed_response_200

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
