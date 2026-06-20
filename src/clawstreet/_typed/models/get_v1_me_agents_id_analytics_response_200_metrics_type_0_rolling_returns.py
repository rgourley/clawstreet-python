from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns")


@_attrs_define
class GetV1MeAgentsIdAnalyticsResponse200MetricsType0RollingReturns:
    """
    Attributes:
        f_1d (float | None):
        f_1w (float | None):
        f_1m (float | None):
        f_3m (float | None):
    """

    f_1d: float | None
    f_1w: float | None
    f_1m: float | None
    f_3m: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        f_1d: float | None
        f_1d = self.f_1d

        f_1w: float | None
        f_1w = self.f_1w

        f_1m: float | None
        f_1m = self.f_1m

        f_3m: float | None
        f_3m = self.f_3m

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "1D": f_1d,
                "1W": f_1w,
                "1M": f_1m,
                "3M": f_3m,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_f_1d(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        f_1d = _parse_f_1d(d.pop("1D"))

        def _parse_f_1w(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        f_1w = _parse_f_1w(d.pop("1W"))

        def _parse_f_1m(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        f_1m = _parse_f_1m(d.pop("1M"))

        def _parse_f_3m(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        f_3m = _parse_f_3m(d.pop("3M"))

        get_v1_me_agents_id_analytics_response_200_metrics_type_0_rolling_returns = cls(
            f_1d=f_1d,
            f_1w=f_1w,
            f_1m=f_1m,
            f_3m=f_3m,
        )

        get_v1_me_agents_id_analytics_response_200_metrics_type_0_rolling_returns.additional_properties = d
        return get_v1_me_agents_id_analytics_response_200_metrics_type_0_rolling_returns

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
