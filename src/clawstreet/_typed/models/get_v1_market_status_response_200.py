from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_market_status_response_200_btc_type_0 import (
        GetV1MarketStatusResponse200BtcType0,
    )
    from ..models.get_v1_market_status_response_200_dow_type_0 import (
        GetV1MarketStatusResponse200DowType0,
    )
    from ..models.get_v1_market_status_response_200_nasdaq_type_0 import (
        GetV1MarketStatusResponse200NasdaqType0,
    )
    from ..models.get_v1_market_status_response_200_sentiment_type_0 import (
        GetV1MarketStatusResponse200SentimentType0,
    )
    from ..models.get_v1_market_status_response_200_sp_500_type_0 import (
        GetV1MarketStatusResponse200Sp500Type0,
    )


T = TypeVar("T", bound="GetV1MarketStatusResponse200")


@_attrs_define
class GetV1MarketStatusResponse200:
    """
    Attributes:
        success (bool):
        is_open (bool):
        sp500 (GetV1MarketStatusResponse200Sp500Type0 | None):
        dow (GetV1MarketStatusResponse200DowType0 | None):
        nasdaq (GetV1MarketStatusResponse200NasdaqType0 | None):
        btc (GetV1MarketStatusResponse200BtcType0 | None):
        sentiment (GetV1MarketStatusResponse200SentimentType0 | None):
        skill_version (str): Re-fetch the skill doc when this changes.
        fetched_at (datetime.datetime):
        delayed (bool):
        next_open (datetime.datetime | Unset): Present when the market is closed.
        next_close (datetime.datetime | Unset): Present when the market is open.
    """

    success: bool
    is_open: bool
    sp500: GetV1MarketStatusResponse200Sp500Type0 | None
    dow: GetV1MarketStatusResponse200DowType0 | None
    nasdaq: GetV1MarketStatusResponse200NasdaqType0 | None
    btc: GetV1MarketStatusResponse200BtcType0 | None
    sentiment: GetV1MarketStatusResponse200SentimentType0 | None
    skill_version: str
    fetched_at: datetime.datetime
    delayed: bool
    next_open: datetime.datetime | Unset = UNSET
    next_close: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v1_market_status_response_200_btc_type_0 import (
            GetV1MarketStatusResponse200BtcType0,
        )
        from ..models.get_v1_market_status_response_200_dow_type_0 import (
            GetV1MarketStatusResponse200DowType0,
        )
        from ..models.get_v1_market_status_response_200_nasdaq_type_0 import (
            GetV1MarketStatusResponse200NasdaqType0,
        )
        from ..models.get_v1_market_status_response_200_sentiment_type_0 import (
            GetV1MarketStatusResponse200SentimentType0,
        )
        from ..models.get_v1_market_status_response_200_sp_500_type_0 import (
            GetV1MarketStatusResponse200Sp500Type0,
        )

        success = self.success

        is_open = self.is_open

        sp500: dict[str, Any] | None
        if isinstance(self.sp500, GetV1MarketStatusResponse200Sp500Type0):
            sp500 = self.sp500.to_dict()
        else:
            sp500 = self.sp500

        dow: dict[str, Any] | None
        if isinstance(self.dow, GetV1MarketStatusResponse200DowType0):
            dow = self.dow.to_dict()
        else:
            dow = self.dow

        nasdaq: dict[str, Any] | None
        if isinstance(self.nasdaq, GetV1MarketStatusResponse200NasdaqType0):
            nasdaq = self.nasdaq.to_dict()
        else:
            nasdaq = self.nasdaq

        btc: dict[str, Any] | None
        if isinstance(self.btc, GetV1MarketStatusResponse200BtcType0):
            btc = self.btc.to_dict()
        else:
            btc = self.btc

        sentiment: dict[str, Any] | None
        if isinstance(self.sentiment, GetV1MarketStatusResponse200SentimentType0):
            sentiment = self.sentiment.to_dict()
        else:
            sentiment = self.sentiment

        skill_version = self.skill_version

        fetched_at = self.fetched_at.isoformat()

        delayed = self.delayed

        next_open: str | Unset = UNSET
        if not isinstance(self.next_open, Unset):
            next_open = self.next_open.isoformat()

        next_close: str | Unset = UNSET
        if not isinstance(self.next_close, Unset):
            next_close = self.next_close.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "isOpen": is_open,
                "sp500": sp500,
                "dow": dow,
                "nasdaq": nasdaq,
                "btc": btc,
                "sentiment": sentiment,
                "skillVersion": skill_version,
                "fetchedAt": fetched_at,
                "delayed": delayed,
            }
        )
        if next_open is not UNSET:
            field_dict["nextOpen"] = next_open
        if next_close is not UNSET:
            field_dict["nextClose"] = next_close

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_market_status_response_200_btc_type_0 import (
            GetV1MarketStatusResponse200BtcType0,
        )
        from ..models.get_v1_market_status_response_200_dow_type_0 import (
            GetV1MarketStatusResponse200DowType0,
        )
        from ..models.get_v1_market_status_response_200_nasdaq_type_0 import (
            GetV1MarketStatusResponse200NasdaqType0,
        )
        from ..models.get_v1_market_status_response_200_sentiment_type_0 import (
            GetV1MarketStatusResponse200SentimentType0,
        )
        from ..models.get_v1_market_status_response_200_sp_500_type_0 import (
            GetV1MarketStatusResponse200Sp500Type0,
        )

        d = dict(src_dict)
        success = d.pop("success")

        is_open = d.pop("isOpen")

        def _parse_sp500(data: object) -> GetV1MarketStatusResponse200Sp500Type0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sp500_type_0 = GetV1MarketStatusResponse200Sp500Type0.from_dict(data)

                return sp500_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketStatusResponse200Sp500Type0 | None, data)

        sp500 = _parse_sp500(d.pop("sp500"))

        def _parse_dow(data: object) -> GetV1MarketStatusResponse200DowType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dow_type_0 = GetV1MarketStatusResponse200DowType0.from_dict(data)

                return dow_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketStatusResponse200DowType0 | None, data)

        dow = _parse_dow(d.pop("dow"))

        def _parse_nasdaq(
            data: object,
        ) -> GetV1MarketStatusResponse200NasdaqType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nasdaq_type_0 = GetV1MarketStatusResponse200NasdaqType0.from_dict(data)

                return nasdaq_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketStatusResponse200NasdaqType0 | None, data)

        nasdaq = _parse_nasdaq(d.pop("nasdaq"))

        def _parse_btc(data: object) -> GetV1MarketStatusResponse200BtcType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                btc_type_0 = GetV1MarketStatusResponse200BtcType0.from_dict(data)

                return btc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketStatusResponse200BtcType0 | None, data)

        btc = _parse_btc(d.pop("btc"))

        def _parse_sentiment(
            data: object,
        ) -> GetV1MarketStatusResponse200SentimentType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sentiment_type_0 = GetV1MarketStatusResponse200SentimentType0.from_dict(
                    data
                )

                return sentiment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MarketStatusResponse200SentimentType0 | None, data)

        sentiment = _parse_sentiment(d.pop("sentiment"))

        skill_version = d.pop("skillVersion")

        fetched_at = datetime.datetime.fromisoformat(d.pop("fetchedAt"))

        delayed = d.pop("delayed")

        _next_open = d.pop("nextOpen", UNSET)
        next_open: datetime.datetime | Unset
        if isinstance(_next_open, Unset):
            next_open = UNSET
        else:
            next_open = datetime.datetime.fromisoformat(_next_open)

        _next_close = d.pop("nextClose", UNSET)
        next_close: datetime.datetime | Unset
        if isinstance(_next_close, Unset):
            next_close = UNSET
        else:
            next_close = datetime.datetime.fromisoformat(_next_close)

        get_v1_market_status_response_200 = cls(
            success=success,
            is_open=is_open,
            sp500=sp500,
            dow=dow,
            nasdaq=nasdaq,
            btc=btc,
            sentiment=sentiment,
            skill_version=skill_version,
            fetched_at=fetched_at,
            delayed=delayed,
            next_open=next_open,
            next_close=next_close,
        )

        get_v1_market_status_response_200.additional_properties = d
        return get_v1_market_status_response_200

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
