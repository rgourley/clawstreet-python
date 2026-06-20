from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0_rolling_returns import (
        GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns,
    )
    from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0_trades import (
        GetV1MeAgentsIdAnalyticsResponse200MetricsType0Trades,
    )


T = TypeVar("T", bound="GetV1MeAgentsIdAnalyticsResponse200MetricsType0")


@_attrs_define
class GetV1MeAgentsIdAnalyticsResponse200MetricsType0:
    """
    Attributes:
        sortino (float):
        calmar (float):
        max_drawdown_pct (float):
        rolling_returns (GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns):
        trades (GetV1MeAgentsIdAnalyticsResponse200MetricsType0Trades):
    """

    sortino: float
    calmar: float
    max_drawdown_pct: float
    rolling_returns: GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns
    trades: GetV1MeAgentsIdAnalyticsResponse200MetricsType0Trades
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sortino = self.sortino

        calmar = self.calmar

        max_drawdown_pct = self.max_drawdown_pct

        rolling_returns = self.rolling_returns.to_dict()

        trades = self.trades.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sortino": sortino,
                "calmar": calmar,
                "max_drawdown_pct": max_drawdown_pct,
                "rolling_returns": rolling_returns,
                "trades": trades,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0_rolling_returns import (
            GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns,
        )
        from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0_trades import (
            GetV1MeAgentsIdAnalyticsResponse200MetricsType0Trades,
        )

        d = dict(src_dict)
        sortino = d.pop("sortino")

        calmar = d.pop("calmar")

        max_drawdown_pct = d.pop("max_drawdown_pct")

        rolling_returns = (
            GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns.from_dict(
                d.pop("rolling_returns")
            )
        )

        trades = GetV1MeAgentsIdAnalyticsResponse200MetricsType0Trades.from_dict(
            d.pop("trades")
        )

        get_v1_me_agents_id_analytics_response_200_metrics_type_0 = cls(
            sortino=sortino,
            calmar=calmar,
            max_drawdown_pct=max_drawdown_pct,
            rolling_returns=rolling_returns,
            trades=trades,
        )

        get_v1_me_agents_id_analytics_response_200_metrics_type_0.additional_properties = d
        return get_v1_me_agents_id_analytics_response_200_metrics_type_0

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
