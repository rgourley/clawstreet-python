from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_news_response_200_articles_item import (
        GetV1SymbolsSymbolNewsResponse200ArticlesItem,
    )
    from ..models.get_v1_symbols_symbol_news_response_200_news_item import (
        GetV1SymbolsSymbolNewsResponse200NewsItem,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolNewsResponse200")


@_attrs_define
class GetV1SymbolsSymbolNewsResponse200:
    """
    Attributes:
        success (bool):
        articles (list[GetV1SymbolsSymbolNewsResponse200ArticlesItem]):
        news (list[GetV1SymbolsSymbolNewsResponse200NewsItem]): The same list as `articles`, kept for callers that read
            the older key.
        count (int):
        newest_published_at (None | str): ISO time of the newest article returned. Null when there are none.
        newest_age_hours (float | None): Hours since the newest article. Null when there are none.
        coverage_stale (bool): True when the newest article is over 72 hours old, or there are none. The window spans a
            weekend so a Friday article still reads as current on Monday.
    """

    success: bool
    articles: list[GetV1SymbolsSymbolNewsResponse200ArticlesItem]
    news: list[GetV1SymbolsSymbolNewsResponse200NewsItem]
    count: int
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

        news = []
        for news_item_data in self.news:
            news_item = news_item_data.to_dict()
            news.append(news_item)

        count = self.count

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
                "news": news,
                "count": count,
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
        from ..models.get_v1_symbols_symbol_news_response_200_news_item import (
            GetV1SymbolsSymbolNewsResponse200NewsItem,
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

        news = []
        _news = d.pop("news")
        for news_item_data in _news:
            news_item = GetV1SymbolsSymbolNewsResponse200NewsItem.from_dict(
                news_item_data
            )

            news.append(news_item)

        count = d.pop("count")

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
            news=news,
            count=count,
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
