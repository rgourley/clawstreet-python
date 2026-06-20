from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyWithSecret")


@_attrs_define
class ApiKeyWithSecret:
    """
    Attributes:
        id (str):
        secret (str): Plaintext API key, shown ONCE on creation or rotation. Store it securely. Example:
            tb_live_abc123def456ghi789jkl012mno345pq.
        label (None | str):
        warning (str):
        scopes (list[str] | Unset):
    """

    id: str
    secret: str
    label: None | str
    warning: str
    scopes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        secret = self.secret

        label: None | str
        label = self.label

        warning = self.warning

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "secret": secret,
                "label": label,
                "warning": warning,
            }
        )
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        secret = d.pop("secret")

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        warning = d.pop("warning")

        scopes = cast(list[str], d.pop("scopes", UNSET))

        api_key_with_secret = cls(
            id=id,
            secret=secret,
            label=label,
            warning=warning,
            scopes=scopes,
        )

        api_key_with_secret.additional_properties = d
        return api_key_with_secret

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
