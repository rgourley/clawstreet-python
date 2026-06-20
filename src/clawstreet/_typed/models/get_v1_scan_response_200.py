from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_scan_response_200_matches_item import (
        GetV1ScanResponse200MatchesItem,
    )


T = TypeVar("T", bound="GetV1ScanResponse200")


@_attrs_define
class GetV1ScanResponse200:
    """
    Attributes:
        success (bool):
        matches (list[GetV1ScanResponse200MatchesItem]):
    """

    success: bool
    matches: list[GetV1ScanResponse200MatchesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "matches": matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_scan_response_200_matches_item import (
            GetV1ScanResponse200MatchesItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = GetV1ScanResponse200MatchesItem.from_dict(matches_item_data)

            matches.append(matches_item)

        get_v1_scan_response_200 = cls(
            success=success,
            matches=matches,
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
