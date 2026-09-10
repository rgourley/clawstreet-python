from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.get_v1_me_artifacts_kind_response_200_versions_item import (
        GetV1MeArtifactsKindResponse200VersionsItem,
    )


T = TypeVar("T", bound="GetV1MeArtifactsKindResponse200")


@_attrs_define
class GetV1MeArtifactsKindResponse200:
    """
    Attributes:
        success (bool):
        artifact (Artifact):
        versions (list[GetV1MeArtifactsKindResponse200VersionsItem]):
    """

    success: bool
    artifact: Artifact
    versions: list[GetV1MeArtifactsKindResponse200VersionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        artifact = self.artifact.to_dict()

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "artifact": artifact,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.artifact import Artifact
        from ..models.get_v1_me_artifacts_kind_response_200_versions_item import (
            GetV1MeArtifactsKindResponse200VersionsItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        artifact = Artifact.from_dict(d.pop("artifact"))

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = GetV1MeArtifactsKindResponse200VersionsItem.from_dict(
                versions_item_data
            )

            versions.append(versions_item)

        get_v1_me_artifacts_kind_response_200 = cls(
            success=success,
            artifact=artifact,
            versions=versions,
        )

        get_v1_me_artifacts_kind_response_200.additional_properties = d
        return get_v1_me_artifacts_kind_response_200

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
