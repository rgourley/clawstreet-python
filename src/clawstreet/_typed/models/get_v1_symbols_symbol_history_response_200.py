from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_symbols_symbol_history_response_200_timespan import (
    GetV1SymbolsSymbolHistoryResponse200Timespan,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_symbols_symbol_history_response_200_derived import (
        GetV1SymbolsSymbolHistoryResponse200Derived,
    )


T = TypeVar("T", bound="GetV1SymbolsSymbolHistoryResponse200")


@_attrs_define
class GetV1SymbolsSymbolHistoryResponse200:
    """
    Attributes:
        success (bool):
        symbol (str):
        periods (int):
        timespan (GetV1SymbolsSymbolHistoryResponse200Timespan):
        open_ (list[float]):
        high (list[float]):
        low (list[float]):
        prices (list[float]): Close of each bar.
        volumes (list[float]):
        rsi (list[float]):
        current_price (float | None):
        delayed (bool):
        derived (GetV1SymbolsSymbolHistoryResponse200Derived | Unset):
    """

    success: bool
    symbol: str
    periods: int
    timespan: GetV1SymbolsSymbolHistoryResponse200Timespan
    open_: list[float]
    high: list[float]
    low: list[float]
    prices: list[float]
    volumes: list[float]
    rsi: list[float]
    current_price: float | None
    delayed: bool
    derived: GetV1SymbolsSymbolHistoryResponse200Derived | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        symbol = self.symbol

        periods = self.periods

        timespan = self.timespan.value

        open_ = self.open_

        high = self.high

        low = self.low

        prices = self.prices

        volumes = self.volumes

        rsi = self.rsi

        current_price: float | None
        current_price = self.current_price

        delayed = self.delayed

        derived: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived, Unset):
            derived = self.derived.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "symbol": symbol,
                "periods": periods,
                "timespan": timespan,
                "open": open_,
                "high": high,
                "low": low,
                "prices": prices,
                "volumes": volumes,
                "rsi": rsi,
                "current_price": current_price,
                "delayed": delayed,
            }
        )
        if derived is not UNSET:
            field_dict["derived"] = derived

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_symbols_symbol_history_response_200_derived import (
            GetV1SymbolsSymbolHistoryResponse200Derived,
        )

        d = dict(src_dict)
        success = d.pop("success")

        symbol = d.pop("symbol")

        periods = d.pop("periods")

        timespan = GetV1SymbolsSymbolHistoryResponse200Timespan(d.pop("timespan"))

        open_ = cast(list[float], d.pop("open"))

        high = cast(list[float], d.pop("high"))

        low = cast(list[float], d.pop("low"))

        prices = cast(list[float], d.pop("prices"))

        volumes = cast(list[float], d.pop("volumes"))

        rsi = cast(list[float], d.pop("rsi"))

        def _parse_current_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        current_price = _parse_current_price(d.pop("current_price"))

        delayed = d.pop("delayed")

        _derived = d.pop("derived", UNSET)
        derived: GetV1SymbolsSymbolHistoryResponse200Derived | Unset
        if isinstance(_derived, Unset):
            derived = UNSET
        else:
            derived = GetV1SymbolsSymbolHistoryResponse200Derived.from_dict(_derived)

        get_v1_symbols_symbol_history_response_200 = cls(
            success=success,
            symbol=symbol,
            periods=periods,
            timespan=timespan,
            open_=open_,
            high=high,
            low=low,
            prices=prices,
            volumes=volumes,
            rsi=rsi,
            current_price=current_price,
            delayed=delayed,
            derived=derived,
        )

        get_v1_symbols_symbol_history_response_200.additional_properties = d
        return get_v1_symbols_symbol_history_response_200

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
