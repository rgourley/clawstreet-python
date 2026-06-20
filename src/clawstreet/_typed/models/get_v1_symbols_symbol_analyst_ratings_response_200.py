from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_analyst_ratings_response_200_ratings import (
        GetV1SymbolsSymbolAnalystRatingsResponse200Ratings,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolAnalystRatingsResponse200")


@_attrs_define
class GetV1SymbolsSymbolAnalystRatingsResponse200:
    """
    Attributes:
        success (bool):
        ratings (GetV1SymbolsSymbolAnalystRatingsResponse200Ratings):
    """

    success: bool
    ratings: GetV1SymbolsSymbolAnalystRatingsResponse200Ratings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        ratings = self.ratings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "ratings": ratings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_symbols_symbol_analyst_ratings_response_200_ratings import (
            GetV1SymbolsSymbolAnalystRatingsResponse200Ratings,
        )

        d = dict(src_dict)
        success = d.pop("success")

        ratings = GetV1SymbolsSymbolAnalystRatingsResponse200Ratings.from_dict(
            d.pop("ratings")
        )

        get_v1_symbols_symbol_analyst_ratings_response_200 = cls(
            success=success,
            ratings=ratings,
        )

        get_v1_symbols_symbol_analyst_ratings_response_200.additional_properties = d
        return get_v1_symbols_symbol_analyst_ratings_response_200

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
