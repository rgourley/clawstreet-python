from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostV1MeAgentsIdIterateResponse200Agent")


@_attrs_define
class PostV1MeAgentsIdIterateResponse200Agent:
    """
    Attributes:
        id (UUID):
        version (int):
        slug (str):
    """

    id: UUID
    version: int
    slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        version = self.version

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        version = d.pop("version")

        slug = d.pop("slug")

        post_v1_me_agents_id_iterate_response_200_agent = cls(
            id=id,
            version=version,
            slug=slug,
        )

        post_v1_me_agents_id_iterate_response_200_agent.additional_properties = d
        return post_v1_me_agents_id_iterate_response_200_agent

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
