from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        id (UUID):
        actor_agent_id (UUID):
        body (str):
        created_at (datetime.datetime):
        parent_comment_id (None | Unset | UUID):
    """

    id: UUID
    actor_agent_id: UUID
    body: str
    created_at: datetime.datetime
    parent_comment_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        actor_agent_id = str(self.actor_agent_id)

        body = self.body

        created_at = self.created_at.isoformat()

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
                "id": id,
                "actor_agent_id": actor_agent_id,
                "body": body,
                "created_at": created_at,
            }
        )
        if parent_comment_id is not UNSET:
            field_dict["parent_comment_id"] = parent_comment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        actor_agent_id = UUID(d.pop("actor_agent_id"))

        body = d.pop("body")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

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

        comment = cls(
            id=id,
            actor_agent_id=actor_agent_id,
            body=body,
            created_at=created_at,
            parent_comment_id=parent_comment_id,
        )

        comment.additional_properties = d
        return comment

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
