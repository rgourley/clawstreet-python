from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.get_v1_scan_response_200_matches_item_macd_type_0 import (
        GetV1ScanResponse200MatchesItemMacdType0,
    )
    from ..models.get_v1_scan_response_200_matches_item_stochastic_type_0 import (
        GetV1ScanResponse200MatchesItemStochasticType0,
    )


T = TypeVar("T", bound="GetV1ScanResponse200MatchesItem")


@_attrs_define
class GetV1ScanResponse200MatchesItem:
    """
    Attributes:
        symbol (str):
        sector (None | str):
        rsi (float | None):
        stochastic (GetV1ScanResponse200MatchesItemStochasticType0 | None): Null outside live mode.
        macd (GetV1ScanResponse200MatchesItemMacdType0 | None): Null outside live mode.
        bb_position (float | None):
        volume_ratio (float | None):
        price (float | None):
        sma50 (float | None):
        change_1d (float | None): Percent change from the previous session close. During a session this is the move so
            far today. Null when the symbol has too few bars.
        change_5d (float | None):
        change_30d (float | None): Percent change over 30 sessions. Null when the symbol has too few bars.
        max_1d_drop (float | None): Worst single-session percent change in the last 20 sessions, always 0 or less.
            Present in every mode. Null only when the symbol has too few bars, or, in filter and precomputed mode, before
            the nightly cron has filled it.
        price_as_of (str): ISO time `price` was read. In filter mode a row the market cache covers carries a live price
            and a recent timestamp, while a row it does not keeps the daily close and the nightly timestamp. Compare it with
            `dataTimestamp`, which describes the indicators.
        reason (str):
    """

    symbol: str
    sector: None | str
    rsi: float | None
    stochastic: GetV1ScanResponse200MatchesItemStochasticType0 | None
    macd: GetV1ScanResponse200MatchesItemMacdType0 | None
    bb_position: float | None
    volume_ratio: float | None
    price: float | None
    sma50: float | None
    change_1d: float | None
    change_5d: float | None
    change_30d: float | None
    max_1d_drop: float | None
    price_as_of: str
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v1_scan_response_200_matches_item_macd_type_0 import (
            GetV1ScanResponse200MatchesItemMacdType0,
        )
        from ..models.get_v1_scan_response_200_matches_item_stochastic_type_0 import (
            GetV1ScanResponse200MatchesItemStochasticType0,
        )

        symbol = self.symbol

        sector: None | str
        sector = self.sector

        rsi: float | None
        rsi = self.rsi

        stochastic: dict[str, Any] | None
        if isinstance(self.stochastic, GetV1ScanResponse200MatchesItemStochasticType0):
            stochastic = self.stochastic.to_dict()
        else:
            stochastic = self.stochastic

        macd: dict[str, Any] | None
        if isinstance(self.macd, GetV1ScanResponse200MatchesItemMacdType0):
            macd = self.macd.to_dict()
        else:
            macd = self.macd

        bb_position: float | None
        bb_position = self.bb_position

        volume_ratio: float | None
        volume_ratio = self.volume_ratio

        price: float | None
        price = self.price

        sma50: float | None
        sma50 = self.sma50

        change_1d: float | None
        change_1d = self.change_1d

        change_5d: float | None
        change_5d = self.change_5d

        change_30d: float | None
        change_30d = self.change_30d

        max_1d_drop: float | None
        max_1d_drop = self.max_1d_drop

        price_as_of = self.price_as_of

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "sector": sector,
                "rsi": rsi,
                "stochastic": stochastic,
                "macd": macd,
                "bbPosition": bb_position,
                "volumeRatio": volume_ratio,
                "price": price,
                "sma50": sma50,
                "change_1d": change_1d,
                "change_5d": change_5d,
                "change_30d": change_30d,
                "max_1d_drop": max_1d_drop,
                "price_as_of": price_as_of,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_scan_response_200_matches_item_macd_type_0 import (
            GetV1ScanResponse200MatchesItemMacdType0,
        )
        from ..models.get_v1_scan_response_200_matches_item_stochastic_type_0 import (
            GetV1ScanResponse200MatchesItemStochasticType0,
        )

        d = dict(src_dict)
        symbol = d.pop("symbol")

        def _parse_sector(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sector = _parse_sector(d.pop("sector"))

        def _parse_rsi(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rsi = _parse_rsi(d.pop("rsi"))

        def _parse_stochastic(
            data: object,
        ) -> GetV1ScanResponse200MatchesItemStochasticType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stochastic_type_0 = (
                    GetV1ScanResponse200MatchesItemStochasticType0.from_dict(data)
                )

                return stochastic_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1ScanResponse200MatchesItemStochasticType0 | None, data)

        stochastic = _parse_stochastic(d.pop("stochastic"))

        def _parse_macd(
            data: object,
        ) -> GetV1ScanResponse200MatchesItemMacdType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                macd_type_0 = GetV1ScanResponse200MatchesItemMacdType0.from_dict(data)

                return macd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1ScanResponse200MatchesItemMacdType0 | None, data)

        macd = _parse_macd(d.pop("macd"))

        def _parse_bb_position(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        bb_position = _parse_bb_position(d.pop("bbPosition"))

        def _parse_volume_ratio(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        volume_ratio = _parse_volume_ratio(d.pop("volumeRatio"))

        def _parse_price(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        price = _parse_price(d.pop("price"))

        def _parse_sma50(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        sma50 = _parse_sma50(d.pop("sma50"))

        def _parse_change_1d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        change_1d = _parse_change_1d(d.pop("change_1d"))

        def _parse_change_5d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        change_5d = _parse_change_5d(d.pop("change_5d"))

        def _parse_change_30d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        change_30d = _parse_change_30d(d.pop("change_30d"))

        def _parse_max_1d_drop(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        max_1d_drop = _parse_max_1d_drop(d.pop("max_1d_drop"))

        price_as_of = d.pop("price_as_of")

        reason = d.pop("reason")

        get_v1_scan_response_200_matches_item = cls(
            symbol=symbol,
            sector=sector,
            rsi=rsi,
            stochastic=stochastic,
            macd=macd,
            bb_position=bb_position,
            volume_ratio=volume_ratio,
            price=price,
            sma50=sma50,
            change_1d=change_1d,
            change_5d=change_5d,
            change_30d=change_30d,
            max_1d_drop=max_1d_drop,
            price_as_of=price_as_of,
            reason=reason,
        )

        get_v1_scan_response_200_matches_item.additional_properties = d
        return get_v1_scan_response_200_matches_item

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
