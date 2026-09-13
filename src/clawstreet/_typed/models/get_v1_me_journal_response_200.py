from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.journal_alert import JournalAlert
    from ..models.journal_note import JournalNote
    from ..models.journal_review import JournalReview


T = TypeVar("T", bound="GetV1MeJournalResponse200")


@_attrs_define
class GetV1MeJournalResponse200:
    """
    Attributes:
        success (bool):
        data (list[JournalAlert | JournalNote | JournalReview]):
        count (float):
        has_more (bool):
    """

    success: bool
    data: list[JournalAlert | JournalNote | JournalReview]
    count: float
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.journal_alert import JournalAlert
        from ..models.journal_note import JournalNote

        success = self.success

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, JournalNote) or isinstance(
                data_item_data, JournalAlert
            ):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)

        count = self.count

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "data": data,
                "count": count,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.journal_alert import JournalAlert
        from ..models.journal_note import JournalNote
        from ..models.journal_review import JournalReview

        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:

            def _parse_data_item(
                data: object,
            ) -> JournalAlert | JournalNote | JournalReview:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_journal_item_type_0 = JournalNote.from_dict(data)

                    return componentsschemas_journal_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_journal_item_type_1 = JournalAlert.from_dict(data)

                    return componentsschemas_journal_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_journal_item_type_2 = JournalReview.from_dict(data)

                return componentsschemas_journal_item_type_2

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)

        count = d.pop("count")

        has_more = d.pop("has_more")

        get_v1_me_journal_response_200 = cls(
            success=success,
            data=data,
            count=count,
            has_more=has_more,
        )

        get_v1_me_journal_response_200.additional_properties = d
        return get_v1_me_journal_response_200

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
