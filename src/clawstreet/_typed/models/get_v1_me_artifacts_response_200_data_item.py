from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_me_artifacts_response_200_data_item_created_by import (
    GetV1MeArtifactsResponse200DataItemCreatedBy,
)
from ..models.get_v1_me_artifacts_response_200_data_item_kind import (
    GetV1MeArtifactsResponse200DataItemKind,
)
from ..models.get_v1_me_artifacts_response_200_data_item_status import (
    GetV1MeArtifactsResponse200DataItemStatus,
)

T = TypeVar("T", bound="GetV1MeArtifactsResponse200DataItem")


@_attrs_define
class GetV1MeArtifactsResponse200DataItem:
    """
    Attributes:
        id (str):  Example: art_3k9f2m1x8p0q.
        kind (GetV1MeArtifactsResponse200DataItemKind):
        version (int):  Example: 3.
        parent_version (int | None):
        content_hash (str):  Example: 9f86d081884c7d65....
        commit_message (None | str):
        created_by (GetV1MeArtifactsResponse200DataItemCreatedBy):
        status (GetV1MeArtifactsResponse200DataItemStatus):
        activated_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    kind: GetV1MeArtifactsResponse200DataItemKind
    version: int
    parent_version: int | None
    content_hash: str
    commit_message: None | str
    created_by: GetV1MeArtifactsResponse200DataItemCreatedBy
    status: GetV1MeArtifactsResponse200DataItemStatus
    activated_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        version = self.version

        parent_version: int | None
        parent_version = self.parent_version

        content_hash = self.content_hash

        commit_message: None | str
        commit_message = self.commit_message

        created_by = self.created_by.value

        status = self.status.value

        activated_at: None | str
        if isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "version": version,
                "parent_version": parent_version,
                "content_hash": content_hash,
                "commit_message": commit_message,
                "created_by": created_by,
                "status": status,
                "activated_at": activated_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        kind = GetV1MeArtifactsResponse200DataItemKind(d.pop("kind"))

        version = d.pop("version")

        def _parse_parent_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        parent_version = _parse_parent_version(d.pop("parent_version"))

        content_hash = d.pop("content_hash")

        def _parse_commit_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_message = _parse_commit_message(d.pop("commit_message"))

        created_by = GetV1MeArtifactsResponse200DataItemCreatedBy(d.pop("created_by"))

        status = GetV1MeArtifactsResponse200DataItemStatus(d.pop("status"))

        def _parse_activated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)

                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        activated_at = _parse_activated_at(d.pop("activated_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        get_v1_me_artifacts_response_200_data_item = cls(
            id=id,
            kind=kind,
            version=version,
            parent_version=parent_version,
            content_hash=content_hash,
            commit_message=commit_message,
            created_by=created_by,
            status=status,
            activated_at=activated_at,
            created_at=created_at,
        )

        get_v1_me_artifacts_response_200_data_item.additional_properties = d
        return get_v1_me_artifacts_response_200_data_item

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
