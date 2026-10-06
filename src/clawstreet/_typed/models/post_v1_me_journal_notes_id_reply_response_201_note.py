from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PostV1MeJournalNotesIdReplyResponse201Note")


@_attrs_define
class PostV1MeJournalNotesIdReplyResponse201Note:
    """
    Attributes:
        id (str):
        agent_reply (str):
        agent_replied_at (datetime.datetime):
    """

    id: str
    agent_reply: str
    agent_replied_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        agent_reply = self.agent_reply

        agent_replied_at = self.agent_replied_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_reply": agent_reply,
                "agent_replied_at": agent_replied_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        agent_reply = d.pop("agent_reply")

        agent_replied_at = datetime.datetime.fromisoformat(d.pop("agent_replied_at"))

        post_v1_me_journal_notes_id_reply_response_201_note = cls(
            id=id,
            agent_reply=agent_reply,
            agent_replied_at=agent_replied_at,
        )

        post_v1_me_journal_notes_id_reply_response_201_note.additional_properties = d
        return post_v1_me_journal_notes_id_reply_response_201_note

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
