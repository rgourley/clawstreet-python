from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_news_response_200_articles_item import (
        GetV1SymbolsSymbolNewsResponse200ArticlesItem,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolNewsResponse200")


@_attrs_define
class GetV1SymbolsSymbolNewsResponse200:
    """
    Attributes:
        success (bool):
        articles (list[GetV1SymbolsSymbolNewsResponse200ArticlesItem]):
        newest_published_at (None | str): ISO time of the newest article returned. Null when there are none.
        newest_age_hours (float | None): Hours since the newest article. Null when there are none.
        coverage_stale (bool): True when the newest article is over 72 hours old, or there are none. The window spans a
            weekend so a Friday article still reads as current on Monday.
    """

    success: bool
    articles: list[GetV1SymbolsSymbolNewsResponse200ArticlesItem]
    newest_published_at: None | str
    newest_age_hours: float | None
    coverage_stale: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        articles = []
        for articles_item_data in self.articles:
            articles_item = articles_item_data.to_dict()
            articles.append(articles_item)

        newest_published_at: None | str
        newest_published_at = self.newest_published_at

        newest_age_hours: float | None
        newest_age_hours = self.newest_age_hours

        coverage_stale = self.coverage_stale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "articles": articles,
                "newest_published_at": newest_published_at,
                "newest_age_hours": newest_age_hours,
                "coverage_stale": coverage_stale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_symbols_symbol_news_response_200_articles_item import (
            GetV1SymbolsSymbolNewsResponse200ArticlesItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        articles = []
        _articles = d.pop("articles")
        for articles_item_data in _articles:
            articles_item = GetV1SymbolsSymbolNewsResponse200ArticlesItem.from_dict(
                articles_item_data
            )

            articles.append(articles_item)

        def _parse_newest_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        newest_published_at = _parse_newest_published_at(d.pop("newest_published_at"))

        def _parse_newest_age_hours(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        newest_age_hours = _parse_newest_age_hours(d.pop("newest_age_hours"))

        coverage_stale = d.pop("coverage_stale")

        get_v1_symbols_symbol_news_response_200 = cls(
            success=success,
            articles=articles,
            newest_published_at=newest_published_at,
            newest_age_hours=newest_age_hours,
            coverage_stale=coverage_stale,
        )

        get_v1_symbols_symbol_news_response_200.additional_properties = d
        return get_v1_symbols_symbol_news_response_200

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
