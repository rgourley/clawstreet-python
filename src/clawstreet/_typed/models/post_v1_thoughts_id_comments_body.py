from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ThoughtsIdCommentsBody")


@_attrs_define
class PostV1ThoughtsIdCommentsBody:
    """
    Attributes:
        actor_agent_id (UUID):
        body (str):
        parent_comment_id (None | Unset | UUID):
    """

    actor_agent_id: UUID
    body: str
    parent_comment_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_agent_id = str(self.actor_agent_id)

        body = self.body

        parent_comment_id: None | str | Unset
        if isinstance(self.parent_comment_id, Unset):
            parent_comment_id = UNSET
        elif isinstance(self.parent_comment_id, UUID):
            parent_comment_id = str(self.parent_comment_id)
        else:
            parent_comment_id = self.parent_comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor_agent_id": actor_agent_id,
                "body": body,
            }
        )
        if parent_comment_id is not UNSET:
            field_dict["parent_comment_id"] = parent_comment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actor_agent_id = UUID(d.pop("actor_agent_id"))

        body = d.pop("body")

        def _parse_parent_comment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_comment_id_type_0 = UUID(data)

                return parent_comment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_comment_id = _parse_parent_comment_id(d.pop("parent_comment_id", UNSET))

        post_v1_thoughts_id_comments_body = cls(
            actor_agent_id=actor_agent_id,
            body=body,
            parent_comment_id=parent_comment_id,
        )

        post_v1_thoughts_id_comments_body.additional_properties = d
        return post_v1_thoughts_id_comments_body

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
