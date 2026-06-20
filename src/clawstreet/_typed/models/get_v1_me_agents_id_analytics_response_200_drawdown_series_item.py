from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem")


@_attrs_define
class GetV1MeAgentsIdAnalyticsResponse200DrawdownSeriesItem:
    """
    Attributes:
        t (str):
        drawdown_pct (float):
    """

    t: str
    drawdown_pct: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        t = self.t

        drawdown_pct = self.drawdown_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "t": t,
                "drawdown_pct": drawdown_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        t = d.pop("t")

        drawdown_pct = d.pop("drawdown_pct")

        get_v1_me_agents_id_analytics_response_200_drawdown_series_item = cls(
            t=t,
            drawdown_pct=drawdown_pct,
        )

        get_v1_me_agents_id_analytics_response_200_drawdown_series_item.additional_properties = d
        return get_v1_me_agents_id_analytics_response_200_drawdown_series_item

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
