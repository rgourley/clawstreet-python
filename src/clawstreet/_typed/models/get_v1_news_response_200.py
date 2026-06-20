from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_news_response_200_articles_item import (
        GetV1NewsResponse200ArticlesItem,
    )


T = TypeVar("T", bound="GetV1NewsResponse200")


@_attrs_define
class GetV1NewsResponse200:
    """
    Attributes:
        success (bool):
        articles (list[GetV1NewsResponse200ArticlesItem]):
    """

    success: bool
    articles: list[GetV1NewsResponse200ArticlesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        articles = []
        for articles_item_data in self.articles:
            articles_item = articles_item_data.to_dict()
            articles.append(articles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "articles": articles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_news_response_200_articles_item import (
            GetV1NewsResponse200ArticlesItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        articles = []
        _articles = d.pop("articles")
        for articles_item_data in _articles:
            articles_item = GetV1NewsResponse200ArticlesItem.from_dict(
                articles_item_data
            )

            articles.append(articles_item)

        get_v1_news_response_200 = cls(
            success=success,
            articles=articles,
        )

        get_v1_news_response_200.additional_properties = d
        return get_v1_news_response_200

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
