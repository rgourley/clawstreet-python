from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.post_v1_me_reports_body_kind import PostV1MeReportsBodyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MeReportsBody")


@_attrs_define
class PostV1MeReportsBody:
    """
    Attributes:
        kind (PostV1MeReportsBodyKind):
        endpoint (str):  Example: POST /v1/me/agents/{id}/orders.
        expected (str):  Example: A trailing_stop fills once price falls 9% below the high..
        actual (str):  Example: The order stayed pending for 6 days with price 12% below the high..
        example (str | Unset): An order id, request id or symbol that reproduces it. Example: ord_8f2c.
    """

    kind: PostV1MeReportsBodyKind
    endpoint: str
    expected: str
    actual: str
    example: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        endpoint = self.endpoint

        expected = self.expected

        actual = self.actual

        example = self.example

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "endpoint": endpoint,
                "expected": expected,
                "actual": actual,
            }
        )
        if example is not UNSET:
            field_dict["example"] = example

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = PostV1MeReportsBodyKind(d.pop("kind"))

        endpoint = d.pop("endpoint")

        expected = d.pop("expected")

        actual = d.pop("actual")

        example = d.pop("example", UNSET)

        post_v1_me_reports_body = cls(
            kind=kind,
            endpoint=endpoint,
            expected=expected,
            actual=actual,
            example=example,
        )

        post_v1_me_reports_body.additional_properties = d
        return post_v1_me_reports_body

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
