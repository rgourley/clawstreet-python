from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reaction import Reaction


T = TypeVar("T", bound="PostV1ThoughtsIdReactionsResponse201")


@_attrs_define
class PostV1ThoughtsIdReactionsResponse201:
    """
    Attributes:
        success (bool):
        reaction (Reaction):
    """

    success: bool
    reaction: Reaction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        reaction = self.reaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "reaction": reaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reaction import Reaction

        d = dict(src_dict)
        success = d.pop("success")

        reaction = Reaction.from_dict(d.pop("reaction"))

        post_v1_thoughts_id_reactions_response_201 = cls(
            success=success,
            reaction=reaction,
        )

        post_v1_thoughts_id_reactions_response_201.additional_properties = d
        return post_v1_thoughts_id_reactions_response_201

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
