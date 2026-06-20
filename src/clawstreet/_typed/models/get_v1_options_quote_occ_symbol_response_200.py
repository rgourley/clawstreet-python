from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_options_quote_occ_symbol_response_200_multiplier import (
    GetV1OptionsQuoteOccSymbolResponse200Multiplier,
)
from ..models.get_v1_options_quote_occ_symbol_response_200_type import (
    GetV1OptionsQuoteOccSymbolResponse200Type,
)

if TYPE_CHECKING:
    from ..models.get_v1_options_quote_occ_symbol_response_200_day_type_0 import (
        GetV1OptionsQuoteOccSymbolResponse200DayType0,
    )
    from ..models.get_v1_options_quote_occ_symbol_response_200_greeks_type_0 import (
        GetV1OptionsQuoteOccSymbolResponse200GreeksType0,
    )


T = TypeVar("T", bound="GetV1OptionsQuoteOccSymbolResponse200")


@_attrs_define
class GetV1OptionsQuoteOccSymbolResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        underlying (str):
        strike (float):
        expiration (str):
        type_ (GetV1OptionsQuoteOccSymbolResponse200Type):
        multiplier (GetV1OptionsQuoteOccSymbolResponse200Multiplier):
        mark (float | None):
        fmv_last_updated (float | None):
        day (GetV1OptionsQuoteOccSymbolResponse200DayType0 | None):
        open_interest (float):
        implied_volatility (float | None):
        greeks (GetV1OptionsQuoteOccSymbolResponse200GreeksType0 | None):
        underlying_price (float | None):
    """

    success: bool
    symbol: str
    underlying: str
    strike: float
    expiration: str
    type_: GetV1OptionsQuoteOccSymbolResponse200Type
    multiplier: GetV1OptionsQuoteOccSymbolResponse200Multiplier
    mark: float | None
    fmv_last_updated: float | None
    day: GetV1OptionsQuoteOccSymbolResponse200DayType0 | None
    open_interest: float
    implied_volatility: float | None
    greeks: GetV1OptionsQuoteOccSymbolResponse200GreeksType0 | None
    underlying_price: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v1_options_quote_occ_symbol_response_200_day_type_0 import (
            GetV1OptionsQuoteOccSymbolResponse200DayType0,
        )
        from ..models.get_v1_options_quote_occ_symbol_response_200_greeks_type_0 import (
            GetV1OptionsQuoteOccSymbolResponse200GreeksType0,
        )

        success = self.success

        symbol = self.symbol

        underlying = self.underlying

        strike = self.strike

        expiration = self.expiration

        type_ = self.type_.value

        multiplier = self.multiplier.value

        mark: float | None
        mark = self.mark

        fmv_last_updated: float | None
        fmv_last_updated = self.fmv_last_updated

        day: dict[str, Any] | None
        if isinstance(self.day, GetV1OptionsQuoteOccSymbolResponse200DayType0):
            day = self.day.to_dict()
        else:
            day = self.day

        open_interest = self.open_interest

        implied_volatility: float | None
        implied_volatility = self.implied_volatility

        greeks: dict[str, Any] | None
        if isinstance(self.greeks, GetV1OptionsQuoteOccSymbolResponse200GreeksType0):
            greeks = self.greeks.to_dict()
        else:
            greeks = self.greeks

        underlying_price: float | None
        underlying_price = self.underlying_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "underlying": underlying,
                "strike": strike,
                "expiration": expiration,
                "type": type_,
                "multiplier": multiplier,
                "mark": mark,
                "fmv_last_updated": fmv_last_updated,
                "day": day,
                "open_interest": open_interest,
                "implied_volatility": implied_volatility,
                "greeks": greeks,
                "underlying_price": underlying_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_options_quote_occ_symbol_response_200_day_type_0 import (
            GetV1OptionsQuoteOccSymbolResponse200DayType0,
        )
        from ..models.get_v1_options_quote_occ_symbol_response_200_greeks_type_0 import (
            GetV1OptionsQuoteOccSymbolResponse200GreeksType0,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        underlying = d.pop("underlying")

        strike = d.pop("strike")

        expiration = d.pop("expiration")

        type_ = GetV1OptionsQuoteOccSymbolResponse200Type(d.pop("type"))

        multiplier = GetV1OptionsQuoteOccSymbolResponse200Multiplier(
            d.pop("multiplier")
        )

        def _parse_mark(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mark = _parse_mark(d.pop("mark"))

        def _parse_fmv_last_updated(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        fmv_last_updated = _parse_fmv_last_updated(d.pop("fmv_last_updated"))

        def _parse_day(
            data: object,
        ) -> GetV1OptionsQuoteOccSymbolResponse200DayType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                day_type_0 = GetV1OptionsQuoteOccSymbolResponse200DayType0.from_dict(
                    data
                )

                return day_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1OptionsQuoteOccSymbolResponse200DayType0 | None, data)

        day = _parse_day(d.pop("day"))

        open_interest = d.pop("open_interest")

        def _parse_implied_volatility(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        implied_volatility = _parse_implied_volatility(d.pop("implied_volatility"))

        def _parse_greeks(
            data: object,
        ) -> GetV1OptionsQuoteOccSymbolResponse200GreeksType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                greeks_type_0 = (
                    GetV1OptionsQuoteOccSymbolResponse200GreeksType0.from_dict(data)
                )

                return greeks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1OptionsQuoteOccSymbolResponse200GreeksType0 | None, data)

        greeks = _parse_greeks(d.pop("greeks"))

        def _parse_underlying_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        underlying_price = _parse_underlying_price(d.pop("underlying_price"))

        get_v1_options_quote_occ_symbol_response_200 = cls(
            success=success,
            symbol=symbol,
            underlying=underlying,
            strike=strike,
            expiration=expiration,
            type_=type_,
            multiplier=multiplier,
            mark=mark,
            fmv_last_updated=fmv_last_updated,
            day=day,
            open_interest=open_interest,
            implied_volatility=implied_volatility,
            greeks=greeks,
            underlying_price=underlying_price,
        )

        get_v1_options_quote_occ_symbol_response_200.additional_properties = d
        return get_v1_options_quote_occ_symbol_response_200

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
