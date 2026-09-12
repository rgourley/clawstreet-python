from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.journal_note_target_type_0_type import JournalNoteTargetType0Type

T = TypeVar("T", bound="JournalNoteTargetType0")


@_attrs_define
class JournalNoteTargetType0:
    """
    Attributes:
        type_ (JournalNoteTargetType0Type):
        id (str):
        summary (None | str):  Example: SELL 120 AAPL @ 231.4, Sep 8.
    """

    type_: JournalNoteTargetType0Type
    id: str
    summary: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        summary: None | str
        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = JournalNoteTargetType0Type(d.pop("type"))

        id = d.pop("id")

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        journal_note_target_type_0 = cls(
            type_=type_,
            id=id,
            summary=summary,
        )

        journal_note_target_type_0.additional_properties = d
        return journal_note_target_type_0

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
