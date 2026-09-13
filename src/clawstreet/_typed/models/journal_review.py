from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.journal_review_kind import JournalReviewKind

if TYPE_CHECKING:
    from ..models.journal_review_body import JournalReviewBody


T = TypeVar("T", bound="JournalReview")


@_attrs_define
class JournalReview:
    """
    Attributes:
        kind (JournalReviewKind):
        id (str):  Example: jnl_9p2m4k7s1x0q.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        period_start (str):  Example: 2026-08-31.
        period_end (str):  Example: 2026-09-06.
        title (str):  Example: MeanStreak, week of Aug 31: +2.4%, +$3,118 realized, 38 trades..
        summary (None | str):
        body (JournalReviewBody): The computed digest: return, realized P&L by symbol, hour, weekday, what changed,
            notes.
    """

    kind: JournalReviewKind
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    period_start: str
    period_end: str
    title: str
    summary: None | str
    body: JournalReviewBody
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        period_start = self.period_start

        period_end = self.period_end

        title = self.title

        summary: None | str
        summary = self.summary

        body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "period_start": period_start,
                "period_end": period_end,
                "title": title,
                "summary": summary,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.journal_review_body import JournalReviewBody

        d = dict(src_dict)
        kind = JournalReviewKind(d.pop("kind"))

        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        period_start = d.pop("period_start")

        period_end = d.pop("period_end")

        title = d.pop("title")

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        body = JournalReviewBody.from_dict(d.pop("body"))

        journal_review = cls(
            kind=kind,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            period_start=period_start,
            period_end=period_end,
            title=title,
            summary=summary,
            body=body,
        )

        journal_review.additional_properties = d
        return journal_review

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
