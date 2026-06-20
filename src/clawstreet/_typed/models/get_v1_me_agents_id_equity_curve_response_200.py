from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_me_agents_id_equity_curve_response_200_period import (
    GetV1MeAgentsIdEquityCurveResponse200Period,
)

if TYPE_CHECKING:
    from ..models.equity_point import EquityPoint


T = TypeVar("T", bound="GetV1MeAgentsIdEquityCurveResponse200")


@_attrs_define
class GetV1MeAgentsIdEquityCurveResponse200:
    """
    Attributes:
        success (bool):
        period (GetV1MeAgentsIdEquityCurveResponse200Period):
        points (list[EquityPoint]):
    """

    success: bool
    period: GetV1MeAgentsIdEquityCurveResponse200Period
    points: list[EquityPoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        period = self.period.value

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "period": period,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equity_point import EquityPoint

        d = dict(src_dict)
        success = d.pop("success")

        period = GetV1MeAgentsIdEquityCurveResponse200Period(d.pop("period"))

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = EquityPoint.from_dict(points_item_data)

            points.append(points_item)

        get_v1_me_agents_id_equity_curve_response_200 = cls(
            success=success,
            period=period,
            points=points,
        )

        get_v1_me_agents_id_equity_curve_response_200.additional_properties = d
        return get_v1_me_agents_id_equity_curve_response_200

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
