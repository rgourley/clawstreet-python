from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_quotes_response_200_errors import GetV1QuotesResponse200Errors
    from ..models.get_v1_quotes_response_200_quotes import GetV1QuotesResponse200Quotes


T = TypeVar("T", bound="GetV1QuotesResponse200")


@_attrs_define
class GetV1QuotesResponse200:
    """
    Attributes:
        success (bool):
        quotes (GetV1QuotesResponse200Quotes):
        timestamp (datetime.datetime):
        data_timestamp (datetime.datetime):
        errors (GetV1QuotesResponse200Errors | Unset):
    """

    success: bool
    quotes: GetV1QuotesResponse200Quotes
    timestamp: datetime.datetime
    data_timestamp: datetime.datetime
    errors: GetV1QuotesResponse200Errors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        quotes = self.quotes.to_dict()

        timestamp = self.timestamp.isoformat()

        data_timestamp = self.data_timestamp.isoformat()

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "quotes": quotes,
                "timestamp": timestamp,
                "dataTimestamp": data_timestamp,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_quotes_response_200_errors import (
            GetV1QuotesResponse200Errors,
        )
        from ..models.get_v1_quotes_response_200_quotes import (
            GetV1QuotesResponse200Quotes,
        )

        d = dict(src_dict)
        success = d.pop("success")

        quotes = GetV1QuotesResponse200Quotes.from_dict(d.pop("quotes"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        data_timestamp = datetime.datetime.fromisoformat(d.pop("dataTimestamp"))

        _errors = d.pop("errors", UNSET)
        errors: GetV1QuotesResponse200Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = GetV1QuotesResponse200Errors.from_dict(_errors)

        get_v1_quotes_response_200 = cls(
            success=success,
            quotes=quotes,
            timestamp=timestamp,
            data_timestamp=data_timestamp,
            errors=errors,
        )

        get_v1_quotes_response_200.additional_properties = d
        return get_v1_quotes_response_200

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
