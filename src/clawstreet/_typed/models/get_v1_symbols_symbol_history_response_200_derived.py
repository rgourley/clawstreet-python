from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_symbols_symbol_history_response_200_derived_rsi_trend import (
    GetV1SymbolsSymbolHistoryResponse200DerivedRsiTrend,
)

T = TypeVar("T", bound="GetV1SymbolsSymbolHistoryResponse200Derived")


@_attrs_define
class GetV1SymbolsSymbolHistoryResponse200Derived:
    """
    Attributes:
        price_change_1d (float | None):
        price_change_5d (float | None):
        volume_ratio (float | None):
        rsi_trend (GetV1SymbolsSymbolHistoryResponse200DerivedRsiTrend):
        bb_position (float | None):
        distance_from_sma50 (float | None):
    """

    price_change_1d: float | None
    price_change_5d: float | None
    volume_ratio: float | None
    rsi_trend: GetV1SymbolsSymbolHistoryResponse200DerivedRsiTrend
    bb_position: float | None
    distance_from_sma50: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price_change_1d: float | None
        price_change_1d = self.price_change_1d

        price_change_5d: float | None
        price_change_5d = self.price_change_5d

        volume_ratio: float | None
        volume_ratio = self.volume_ratio

        rsi_trend = self.rsi_trend.value

        bb_position: float | None
        bb_position = self.bb_position

        distance_from_sma50: float | None
        distance_from_sma50 = self.distance_from_sma50

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price_change_1d": price_change_1d,
                "price_change_5d": price_change_5d,
                "volume_ratio": volume_ratio,
                "rsi_trend": rsi_trend,
                "bb_position": bb_position,
                "distance_from_sma50": distance_from_sma50,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_price_change_1d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price_change_1d = _parse_price_change_1d(d.pop("price_change_1d"))

        def _parse_price_change_5d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price_change_5d = _parse_price_change_5d(d.pop("price_change_5d"))

        def _parse_volume_ratio(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        volume_ratio = _parse_volume_ratio(d.pop("volume_ratio"))

        rsi_trend = GetV1SymbolsSymbolHistoryResponse200DerivedRsiTrend(
            d.pop("rsi_trend")
        )

        def _parse_bb_position(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        bb_position = _parse_bb_position(d.pop("bb_position"))

        def _parse_distance_from_sma50(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        distance_from_sma50 = _parse_distance_from_sma50(d.pop("distance_from_sma50"))

        get_v1_symbols_symbol_history_response_200_derived = cls(
            price_change_1d=price_change_1d,
            price_change_5d=price_change_5d,
            volume_ratio=volume_ratio,
            rsi_trend=rsi_trend,
            bb_position=bb_position,
            distance_from_sma50=distance_from_sma50,
        )

        get_v1_symbols_symbol_history_response_200_derived.additional_properties = d
        return get_v1_symbols_symbol_history_response_200_derived

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
