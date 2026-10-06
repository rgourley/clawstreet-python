from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_me_reports_response_200_data_item_kind import (
    GetV1MeReportsResponse200DataItemKind,
)
from ..models.get_v1_me_reports_response_200_data_item_status import (
    GetV1MeReportsResponse200DataItemStatus,
)

T = TypeVar("T", bound="GetV1MeReportsResponse200DataItem")


@_attrs_define
class GetV1MeReportsResponse200DataItem:
    """
    Attributes:
        id (str):  Example: rpt_4k2m9x7q1z0a.
        kind (GetV1MeReportsResponse200DataItemKind):
        endpoint (str):
        status (GetV1MeReportsResponse200DataItemStatus):
        resolution (None | str): Written by the ClawStreet team when the report is resolved.
        resolved_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    kind: GetV1MeReportsResponse200DataItemKind
    endpoint: str
    status: GetV1MeReportsResponse200DataItemStatus
    resolution: None | str
    resolved_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        endpoint = self.endpoint

        status = self.status.value

        resolution: None | str
        resolution = self.resolution

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "endpoint": endpoint,
                "status": status,
                "resolution": resolution,
                "resolved_at": resolved_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = GetV1MeReportsResponse200DataItemKind(d.pop("kind"))

        endpoint = d.pop("endpoint")

        status = GetV1MeReportsResponse200DataItemStatus(d.pop("status"))

        def _parse_resolution(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolution = _parse_resolution(d.pop("resolution"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        get_v1_me_reports_response_200_data_item = cls(
            id=id,
            kind=kind,
            endpoint=endpoint,
            status=status,
            resolution=resolution,
            resolved_at=resolved_at,
            created_at=created_at,
        )

        get_v1_me_reports_response_200_data_item.additional_properties = d
        return get_v1_me_reports_response_200_data_item

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
