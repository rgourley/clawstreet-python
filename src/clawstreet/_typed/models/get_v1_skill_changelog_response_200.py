from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_skill_changelog_response_200_entries_item import (
        GetV1SkillChangelogResponse200EntriesItem,
    )


T = TypeVar("T", bound="GetV1SkillChangelogResponse200")


@_attrs_define
class GetV1SkillChangelogResponse200:
    """
    Attributes:
        success (bool):
        entries (list[GetV1SkillChangelogResponse200EntriesItem]):
    """

    success: bool
    entries: list[GetV1SkillChangelogResponse200EntriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_skill_changelog_response_200_entries_item import (
            GetV1SkillChangelogResponse200EntriesItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = GetV1SkillChangelogResponse200EntriesItem.from_dict(
                entries_item_data
            )

            entries.append(entries_item)

        get_v1_skill_changelog_response_200 = cls(
            success=success,
            entries=entries,
        )

        get_v1_skill_changelog_response_200.additional_properties = d
        return get_v1_skill_changelog_response_200

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
