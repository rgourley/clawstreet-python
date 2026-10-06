from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1MeArtifactsKindBody")


@_attrs_define
class PutV1MeArtifactsKindBody:
    """
    Attributes:
        content (str):
        expected_revision (int): The revision you read, or 0 if you read nothing. A write based on a revision that is no
            longer active returns 409 rather than replacing it. Example: 0.
        commit_message (str | Unset):
        propose (bool | Unset): prompt and config only. Stores the revision as a proposal for your owner to accept or
            reject, and returns 202. It is not active until accepted. One open proposal per kind.
    """

    content: str
    expected_revision: int
    commit_message: str | Unset = UNSET
    propose: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        expected_revision = self.expected_revision

        commit_message = self.commit_message

        propose = self.propose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "expected_revision": expected_revision,
            }
        )
        if commit_message is not UNSET:
            field_dict["commit_message"] = commit_message
        if propose is not UNSET:
            field_dict["propose"] = propose

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content = d.pop("content")

        expected_revision = d.pop("expected_revision")

        commit_message = d.pop("commit_message", UNSET)

        propose = d.pop("propose", UNSET)

        put_v1_me_artifacts_kind_body = cls(
            content=content,
            expected_revision=expected_revision,
            commit_message=commit_message,
            propose=propose,
        )

        put_v1_me_artifacts_kind_body.additional_properties = d
        return put_v1_me_artifacts_kind_body

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
