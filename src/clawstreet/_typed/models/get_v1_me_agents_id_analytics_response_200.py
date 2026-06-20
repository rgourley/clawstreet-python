from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equity_point import EquityPoint
    from ..models.get_v1_me_agents_id_analytics_response_200_drawdown_series_item import (
        GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem,
    )
    from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0 import (
        GetV1MeAgentsIdAnalyticsResponse200MetricsType0,
    )


T = TypeVar("T", bound="GetV1MeAgentsIdAnalyticsResponse200")


@_attrs_define
class GetV1MeAgentsIdAnalyticsResponse200:
    """
    Attributes:
        success (bool):
        metrics (GetV1MeAgentsIdAnalyticsResponse200MetricsType0 | None):
        equity_curve (list[EquityPoint] | Unset):
        drawdown_series (list[GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem] | Unset):
        message (str | Unset):
    """

    success: bool
    metrics: GetV1MeAgentsIdAnalyticsResponse200MetricsType0 | None
    equity_curve: list[EquityPoint] | Unset = UNSET
    drawdown_series: (
        list[GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem] | Unset
    ) = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0 import (
            GetV1MeAgentsIdAnalyticsResponse200MetricsType0,
        )

        success = self.success

        metrics: dict[str, Any] | None
        if isinstance(self.metrics, GetV1MeAgentsIdAnalyticsResponse200MetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        equity_curve: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.equity_curve, Unset):
            equity_curve = []
            for equity_curve_item_data in self.equity_curve:
                equity_curve_item = equity_curve_item_data.to_dict()
                equity_curve.append(equity_curve_item)

        drawdown_series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drawdown_series, Unset):
            drawdown_series = []
            for drawdown_series_item_data in self.drawdown_series:
                drawdown_series_item = drawdown_series_item_data.to_dict()
                drawdown_series.append(drawdown_series_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "metrics": metrics,
            }
        )
        if equity_curve is not UNSET:
            field_dict["equity_curve"] = equity_curve
        if drawdown_series is not UNSET:
            field_dict["drawdown_series"] = drawdown_series
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_point import EquityPoint
        from ..models.get_v1_me_agents_id_analytics_response_200_drawdown_series_item import (
            GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem,
        )
        from ..models.get_v1_me_agents_id_analytics_response_200_metrics_type_0 import (
            GetV1MeAgentsIdAnalyticsResponse200MetricsType0,
        )

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_metrics(
            data: object,
        ) -> GetV1MeAgentsIdAnalyticsResponse200MetricsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = (
                    GetV1MeAgentsIdAnalyticsResponse200MetricsType0.from_dict(data)
                )

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetV1MeAgentsIdAnalyticsResponse200MetricsType0 | None, data)

        metrics = _parse_metrics(d.pop("metrics"))

        _equity_curve = d.pop("equity_curve", UNSET)
        equity_curve: list[EquityPoint] | Unset = UNSET
        if _equity_curve is not UNSET:
            equity_curve = []
            for equity_curve_item_data in _equity_curve:
                equity_curve_item = EquityPoint.from_dict(equity_curve_item_data)

                equity_curve.append(equity_curve_item)

        _drawdown_series = d.pop("drawdown_series", UNSET)
        drawdown_series: (
            list[GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem] | Unset
        ) = UNSET
        if _drawdown_series is not UNSET:
            drawdown_series = []
            for drawdown_series_item_data in _drawdown_series:
                drawdown_series_item = (
                    GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem.from_dict(
                        drawdown_series_item_data
                    )
                )

                drawdown_series.append(drawdown_series_item)

        message = d.pop("message", UNSET)

        get_v1_me_agents_id_analytics_response_200 = cls(
            success=success,
            metrics=metrics,
            equity_curve=equity_curve,
            drawdown_series=drawdown_series,
            message=message,
        )

        get_v1_me_agents_id_analytics_response_200.additional_properties = d
        return get_v1_me_agents_id_analytics_response_200

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
