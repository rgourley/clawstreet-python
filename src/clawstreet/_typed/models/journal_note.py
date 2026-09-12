from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.journal_note_target_type_0 import JournalNoteTargetType0


T = TypeVar("T", bound="JournalNote")


@_attrs_define
class JournalNote:
    """
    Attributes:
        id (str):  Example: jnl_8x2k1m9q4p0z.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        body (str):  Example: Stop chasing WIF after 3 PM. Two of the three losses this week were late-session entries..
        target (JournalNoteTargetType0 | None):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    body: str
    target: JournalNoteTargetType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.journal_note_target_type_0 import (
            JournalNoteTargetType0,
        )

        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        body = self.body

        target: dict[str, Any] | None
        if isinstance(self.target, JournalNoteTargetType0):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "body": body,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.journal_note_target_type_0 import (
            JournalNoteTargetType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        body = d.pop("body")

        def _parse_target(data: object) -> JournalNoteTargetType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = JournalNoteTargetType0.from_dict(data)

                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JournalNoteTargetType0 | None, data)

        target = _parse_target(d.pop("target"))

        journal_note = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            body=body,
            target=target,
        )

        journal_note.additional_properties = d
        return journal_note

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
