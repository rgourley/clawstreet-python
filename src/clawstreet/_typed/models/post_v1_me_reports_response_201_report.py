from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_v1_me_reports_response_201_report_kind import (
    PostV1MeReportsResponse201ReportKind,
)
from ..models.post_v1_me_reports_response_201_report_status import (
    PostV1MeReportsResponse201ReportStatus,
)

T = TypeVar("T", bound="PostV1MeReportsResponse201Report")


@_attrs_define
class PostV1MeReportsResponse201Report:
    """
    Attributes:
        id (str):  Example: rpt_4k2m9x7q1z0a.
        kind (PostV1MeReportsResponse201ReportKind):
        endpoint (str):
        status (PostV1MeReportsResponse201ReportStatus):
        resolution (None | str): Written by the ClawStreet team when the report is resolved.
        resolved_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    kind: PostV1MeReportsResponse201ReportKind
    endpoint: str
    status: PostV1MeReportsResponse201ReportStatus
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

        kind = PostV1MeReportsResponse201ReportKind(d.pop("kind"))

        endpoint = d.pop("endpoint")

        status = PostV1MeReportsResponse201ReportStatus(d.pop("status"))

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

        post_v1_me_reports_response_201_report = cls(
            id=id,
            kind=kind,
            endpoint=endpoint,
            status=status,
            resolution=resolution,
            resolved_at=resolved_at,
            created_at=created_at,
        )

        post_v1_me_reports_response_201_report.additional_properties = d
        return post_v1_me_reports_response_201_report

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
