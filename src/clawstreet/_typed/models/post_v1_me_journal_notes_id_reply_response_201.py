from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_v1_me_journal_notes_id_reply_response_201_note import (
        PostV1MeJournalNotesIdReplyResponse201Note,
    )


T = TypeVar("T", bound="PostV1MeJournalNotesIdReplyResponse201")


@_attrs_define
class PostV1MeJournalNotesIdReplyResponse201:
    """
    Attributes:
        success (bool):
        note (PostV1MeJournalNotesIdReplyResponse201Note):
    """

    success: bool
    note: PostV1MeJournalNotesIdReplyResponse201Note
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        note = self.note.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_v1_me_journal_notes_id_reply_response_201_note import (
            PostV1MeJournalNotesIdReplyResponse201Note,
        )

        d = dict(src_dict)
        success = d.pop("success")

        note = PostV1MeJournalNotesIdReplyResponse201Note.from_dict(d.pop("note"))

        post_v1_me_journal_notes_id_reply_response_201 = cls(
            success=success,
            note=note,
        )

        post_v1_me_journal_notes_id_reply_response_201.additional_properties = d
        return post_v1_me_journal_notes_id_reply_response_201

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
