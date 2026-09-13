from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.journal_alert_alert_type import JournalAlertAlertType
from ..models.journal_alert_kind import JournalAlertKind

if TYPE_CHECKING:
    from ..models.journal_alert_body import JournalAlertBody


T = TypeVar("T", bound="JournalAlert")


@_attrs_define
class JournalAlert:
    """
    Attributes:
        kind (JournalAlertKind):
        id (str):  Example: jnl_4k9s2m1x7q0b.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        alert_type (JournalAlertAlertType):
        title (str):  Example: Bear Claw is down 10.4% from its 30-day peak..
        body (JournalAlertBody): The numbers behind the title. Fields vary by alert_type.
        cleared_at (datetime.datetime | None): Set once the condition no longer holds.
    """

    kind: JournalAlertKind
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    alert_type: JournalAlertAlertType
    title: str
    body: JournalAlertBody
    cleared_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        alert_type = self.alert_type.value

        title = self.title

        body = self.body.to_dict()

        cleared_at: None | str
        if isinstance(self.cleared_at, datetime.datetime):
            cleared_at = self.cleared_at.isoformat()
        else:
            cleared_at = self.cleared_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "alert_type": alert_type,
                "title": title,
                "body": body,
                "cleared_at": cleared_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.journal_alert_body import JournalAlertBody

        d = dict(src_dict)
        kind = JournalAlertKind(d.pop("kind"))

        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alert_type = JournalAlertAlertType(d.pop("alert_type"))

        title = d.pop("title")

        body = JournalAlertBody.from_dict(d.pop("body"))

        def _parse_cleared_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cleared_at_type_0 = datetime.datetime.fromisoformat(data)

                return cleared_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        cleared_at = _parse_cleared_at(d.pop("cleared_at"))

        journal_alert = cls(
            kind=kind,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            alert_type=alert_type,
            title=title,
            body=body,
            cleared_at=cleared_at,
        )

        journal_alert.additional_properties = d
        return journal_alert

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
