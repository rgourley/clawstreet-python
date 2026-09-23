from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_indicators_response_200_indicators import (
        GetV1SymbolsSymbolIndicatorsResponse200Indicators,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolIndicatorsResponse200")


@_attrs_define
class GetV1SymbolsSymbolIndicatorsResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        indicators (GetV1SymbolsSymbolIndicatorsResponse200Indicators):
        timestamp (datetime.datetime):
        data_timestamp (datetime.datetime):
    """

    success: bool
    symbol: str
    indicators: GetV1SymbolsSymbolIndicatorsResponse200Indicators
    timestamp: datetime.datetime
    data_timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        indicators = self.indicators.to_dict()

        timestamp = self.timestamp.isoformat()

        data_timestamp = self.data_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "indicators": indicators,
                "timestamp": timestamp,
                "dataTimestamp": data_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_symbols_symbol_indicators_response_200_indicators import (
            GetV1SymbolsSymbolIndicatorsResponse200Indicators,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        indicators = GetV1SymbolsSymbolIndicatorsResponse200Indicators.from_dict(
            d.pop("indicators")
        )

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        data_timestamp = datetime.datetime.fromisoformat(d.pop("dataTimestamp"))

        get_v1_symbols_symbol_indicators_response_200 = cls(
            success=success,
            symbol=symbol,
            indicators=indicators,
            timestamp=timestamp,
            data_timestamp=data_timestamp,
        )

        get_v1_symbols_symbol_indicators_response_200.additional_properties = d
        return get_v1_symbols_symbol_indicators_response_200

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
