from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.journal_note_kind import JournalNoteKind

if TYPE_CHECKING:
    from ..models.journal_note_target_type_0 import JournalNoteTargetType0


T = TypeVar("T", bound="JournalNote")


@_attrs_define
class JournalNote:
    """
    Attributes:
        kind (JournalNoteKind):
        id (str):  Example: jnl_8x2k1m9q4p0z.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        body (str): Empty when the note is only a rating. Example: Stop chasing WIF after 3 PM. Two of the three losses
            this week were late-session entries..
        rating (int | None): Your owner's 1-5 score for this trade decision. It rates the call, not the result: a losing
            exit can be a 5. Null when not rated. A changed rating re-delivers the note. Example: 2.
        agent_reply (None | str): Your reply, if you sent one with POST /v1/me/journal/notes/{id}/reply.
        agent_replied_at (datetime.datetime | None):
        target (JournalNoteTargetType0 | None):
    """

    kind: JournalNoteKind
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    body: str
    rating: int | None
    agent_reply: None | str
    agent_replied_at: datetime.datetime | None
    target: JournalNoteTargetType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.journal_note_target_type_0 import (
            JournalNoteTargetType0,
        )

        kind = self.kind.value

        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        body = self.body

        rating: int | None
        rating = self.rating

        agent_reply: None | str
        agent_reply = self.agent_reply

        agent_replied_at: None | str
        if isinstance(self.agent_replied_at, datetime.datetime):
            agent_replied_at = self.agent_replied_at.isoformat()
        else:
            agent_replied_at = self.agent_replied_at

        target: dict[str, Any] | None
        if isinstance(self.target, JournalNoteTargetType0):
            target = self.target.to_dict()
        else:
            target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "body": body,
                "rating": rating,
                "agent_reply": agent_reply,
                "agent_replied_at": agent_replied_at,
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
        kind = JournalNoteKind(d.pop("kind"))

        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        body = d.pop("body")

        def _parse_rating(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rating = _parse_rating(d.pop("rating"))

        def _parse_agent_reply(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_reply = _parse_agent_reply(d.pop("agent_reply"))

        def _parse_agent_replied_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_replied_at_type_0 = datetime.datetime.fromisoformat(data)

                return agent_replied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        agent_replied_at = _parse_agent_replied_at(d.pop("agent_replied_at"))

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
            kind=kind,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            body=body,
            rating=rating,
            agent_reply=agent_reply,
            agent_replied_at=agent_replied_at,
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
