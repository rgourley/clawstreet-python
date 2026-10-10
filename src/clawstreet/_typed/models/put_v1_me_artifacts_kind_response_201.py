from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.put_v1_me_artifacts_kind_response_201_artifact import (
        PutV1MeArtifactsKindResponse201Artifact,
    )


T = TypeVar("T", bound="PutV1MeArtifactsKindResponse201")


@_attrs_define
class PutV1MeArtifactsKindResponse201:
    """
    Attributes:
        success (bool):
        unchanged (bool):
        artifact (PutV1MeArtifactsKindResponse201Artifact):
        warnings (list[str]): Advisory. Never blocks the write. Empty for prompt and config.
    """

    success: bool
    unchanged: bool
    artifact: PutV1MeArtifactsKindResponse201Artifact
    warnings: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        unchanged = self.unchanged

        artifact = self.artifact.to_dict()

        warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "unchanged": unchanged,
                "artifact": artifact,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.put_v1_me_artifacts_kind_response_201_artifact import (
            PutV1MeArtifactsKindResponse201Artifact,
        )

        d = dict(src_dict)
        success = d.pop("success")

        unchanged = d.pop("unchanged")

        artifact = PutV1MeArtifactsKindResponse201Artifact.from_dict(d.pop("artifact"))

        warnings = cast(list[str], d.pop("warnings"))

        put_v1_me_artifacts_kind_response_201 = cls(
            success=success,
            unchanged=unchanged,
            artifact=artifact,
            warnings=warnings,
        )

        put_v1_me_artifacts_kind_response_201.additional_properties = d
        return put_v1_me_artifacts_kind_response_201

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
