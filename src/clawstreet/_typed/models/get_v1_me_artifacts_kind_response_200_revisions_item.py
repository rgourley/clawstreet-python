from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.get_v1_me_artifacts_kind_response_200_revisions_item_created_by import (
    GetV1MeArtifactsKindResponse200RevisionsItemCreatedBy,
)
from ..models.get_v1_me_artifacts_kind_response_200_revisions_item_kind import (
    GetV1MeArtifactsKindResponse200RevisionsItemKind,
)
from ..models.get_v1_me_artifacts_kind_response_200_revisions_item_status import (
    GetV1MeArtifactsKindResponse200RevisionsItemStatus,
)

T = TypeVar("T", bound="GetV1MeArtifactsKindResponse200RevisionsItem")


@_attrs_define
class GetV1MeArtifactsKindResponse200RevisionsItem:
    """
    Attributes:
        id (str):  Example: art_3k9f2m1x8p0q.
        kind (GetV1MeArtifactsKindResponse200RevisionsItemKind):
        revision (int): Numbered copy of this artifact. Distinct from the agent version (v1, v2). Example: 3.
        parent_revision (int | None):
        content_hash (str):  Example: 9f86d081884c7d65....
        commit_message (None | str):
        created_by (GetV1MeArtifactsKindResponse200RevisionsItemCreatedBy):
        status (GetV1MeArtifactsKindResponse200RevisionsItemStatus):
        activated_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    kind: GetV1MeArtifactsKindResponse200RevisionsItemKind
    revision: int
    parent_revision: int | None
    content_hash: str
    commit_message: None | str
    created_by: GetV1MeArtifactsKindResponse200RevisionsItemCreatedBy
    status: GetV1MeArtifactsKindResponse200RevisionsItemStatus
    activated_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind.value

        revision = self.revision

        parent_revision: int | None
        parent_revision = self.parent_revision

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
                "revision": revision,
                "parent_revision": parent_revision,
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

        kind = GetV1MeArtifactsKindResponse200RevisionsItemKind(d.pop("kind"))

        revision = d.pop("revision")

        def _parse_parent_revision(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        parent_revision = _parse_parent_revision(d.pop("parent_revision"))

        content_hash = d.pop("content_hash")

        def _parse_commit_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        commit_message = _parse_commit_message(d.pop("commit_message"))

        created_by = GetV1MeArtifactsKindResponse200RevisionsItemCreatedBy(
            d.pop("created_by")
        )

        status = GetV1MeArtifactsKindResponse200RevisionsItemStatus(d.pop("status"))

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

        get_v1_me_artifacts_kind_response_200_revisions_item = cls(
            id=id,
            kind=kind,
            revision=revision,
            parent_revision=parent_revision,
            content_hash=content_hash,
            commit_message=commit_message,
            created_by=created_by,
            status=status,
            activated_at=activated_at,
            created_at=created_at,
        )

        get_v1_me_artifacts_kind_response_200_revisions_item.additional_properties = d
        return get_v1_me_artifacts_kind_response_200_revisions_item

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
