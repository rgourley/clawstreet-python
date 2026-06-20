from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_v1_response_200_rate_limit import GetV1Response200RateLimit


T = TypeVar("T", bound="GetV1Response200")


@_attrs_define
class GetV1Response200:
    """
    Attributes:
        success (bool):
        version (str):
        sunset_date (None | str):
        rate_limit (GetV1Response200RateLimit):
        docs_url (str):
        openapi_url (str):
        status (str):
        generated_at (datetime.datetime):
    """

    success: bool
    version: str
    sunset_date: None | str
    rate_limit: GetV1Response200RateLimit
    docs_url: str
    openapi_url: str
    status: str
    generated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        version = self.version

        sunset_date: None | str
        sunset_date = self.sunset_date

        rate_limit = self.rate_limit.to_dict()

        docs_url = self.docs_url

        openapi_url = self.openapi_url

        status = self.status

        generated_at = self.generated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "version": version,
                "sunset_date": sunset_date,
                "rate_limit": rate_limit,
                "docs_url": docs_url,
                "openapi_url": openapi_url,
                "status": status,
                "generated_at": generated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_response_200_rate_limit import GetV1Response200RateLimit

        d = dict(src_dict)
        success = d.pop("success")

        version = d.pop("version")

        def _parse_sunset_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sunset_date = _parse_sunset_date(d.pop("sunset_date"))

        rate_limit = GetV1Response200RateLimit.from_dict(d.pop("rate_limit"))

        docs_url = d.pop("docs_url")

        openapi_url = d.pop("openapi_url")

        status = d.pop("status")

        generated_at = datetime.datetime.fromisoformat(d.pop("generated_at"))

        get_v1_response_200 = cls(
            success=success,
            version=version,
            sunset_date=sunset_date,
            rate_limit=rate_limit,
            docs_url=docs_url,
            openapi_url=openapi_url,
            status=status,
            generated_at=generated_at,
        )

        get_v1_response_200.additional_properties = d
        return get_v1_response_200

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
