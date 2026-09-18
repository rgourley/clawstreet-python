from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_scan_response_200_mode import GetV1ScanResponse200Mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_scan_response_200_filters_applied import (
        GetV1ScanResponse200FiltersApplied,
    )
    from ..models.get_v1_scan_response_200_matches_item import (
        GetV1ScanResponse200MatchesItem,
    )


T = TypeVar("T", bound="GetV1ScanResponse200")


@_attrs_define
class GetV1ScanResponse200:
    """
    Attributes:
        success (bool):
        mode (GetV1ScanResponse200Mode):
        count (int): Rows in `matches`.
        total_matches (int): Rows that passed the gates before `limit`. In precomputed mode, out of the stored top 100.
        matches (list[GetV1ScanResponse200MatchesItem]):
        data_timestamp (str): ISO time of the indicator data. Filters run on daily indicators, so a row can pass a price
            filter and show a newer `price_as_of` price outside it.
        data_age_seconds (int): Age of dataTimestamp in seconds.
        preset (str | Unset): Present in precomputed and live modes.
        sectors (str | Unset): Present in precomputed and live modes.
        filters_applied (GetV1ScanResponse200FiltersApplied | Unset): Present in filter mode.
        sort (str | Unset):
        data_age (str | Unset): Live mode only. Same value as dataTimestamp.
    """

    success: bool
    mode: GetV1ScanResponse200Mode
    count: int
    total_matches: int
    matches: list[GetV1ScanResponse200MatchesItem]
    data_timestamp: str
    data_age_seconds: int
    preset: str | Unset = UNSET
    sectors: str | Unset = UNSET
    filters_applied: GetV1ScanResponse200FiltersApplied | Unset = UNSET
    sort: str | Unset = UNSET
    data_age: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        mode = self.mode.value

        count = self.count

        total_matches = self.total_matches

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        data_timestamp = self.data_timestamp

        data_age_seconds = self.data_age_seconds

        preset = self.preset

        sectors = self.sectors

        filters_applied: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters_applied, Unset):
            filters_applied = self.filters_applied.to_dict()

        sort = self.sort

        data_age = self.data_age

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "mode": mode,
                "count": count,
                "total_matches": total_matches,
                "matches": matches,
                "dataTimestamp": data_timestamp,
                "dataAgeSeconds": data_age_seconds,
            }
        )
        if preset is not UNSET:
            field_dict["preset"] = preset
        if sectors is not UNSET:
            field_dict["sectors"] = sectors
        if filters_applied is not UNSET:
            field_dict["filters_applied"] = filters_applied
        if sort is not UNSET:
            field_dict["sort"] = sort
        if data_age is not UNSET:
            field_dict["dataAge"] = data_age

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_v1_scan_response_200_filters_applied import (
            GetV1ScanResponse200FiltersApplied,
        )
        from ..models.get_v1_scan_response_200_matches_item import (
            GetV1ScanResponse200MatchesItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        mode = GetV1ScanResponse200Mode(d.pop("mode"))

        count = d.pop("count")

        total_matches = d.pop("total_matches")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = GetV1ScanResponse200MatchesItem.from_dict(matches_item_data)

            matches.append(matches_item)

        data_timestamp = d.pop("dataTimestamp")

        data_age_seconds = d.pop("dataAgeSeconds")

        preset = d.pop("preset", UNSET)

        sectors = d.pop("sectors", UNSET)

        _filters_applied = d.pop("filters_applied", UNSET)
        filters_applied: GetV1ScanResponse200FiltersApplied | Unset
        if isinstance(_filters_applied, Unset):
            filters_applied = UNSET
        else:
            filters_applied = GetV1ScanResponse200FiltersApplied.from_dict(
                _filters_applied
            )

        sort = d.pop("sort", UNSET)

        data_age = d.pop("dataAge", UNSET)

        get_v1_scan_response_200 = cls(
            success=success,
            mode=mode,
            count=count,
            total_matches=total_matches,
            matches=matches,
            data_timestamp=data_timestamp,
            data_age_seconds=data_age_seconds,
            preset=preset,
            sectors=sectors,
            filters_applied=filters_applied,
            sort=sort,
            data_age=data_age,
        )

        get_v1_scan_response_200.additional_properties = d
        return get_v1_scan_response_200

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
