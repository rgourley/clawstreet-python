from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_movers_response_200_gainers_item import (
        GetV1MoversResponse200GainersItem,
    )
    from ..models.get_v1_movers_response_200_losers_item import (
        GetV1MoversResponse200LosersItem,
    )


T = TypeVar("T", bound="GetV1MoversResponse200")


@_attrs_define
class GetV1MoversResponse200:
    """
    Attributes:
        success (bool):
        gainers (list[GetV1MoversResponse200GainersItem] | Unset):
        losers (list[GetV1MoversResponse200LosersItem] | Unset):
    """

    success: bool
    gainers: list[GetV1MoversResponse200GainersItem] | Unset = UNSET
    losers: list[GetV1MoversResponse200LosersItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        gainers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gainers, Unset):
            gainers = []
            for gainers_item_data in self.gainers:
                gainers_item = gainers_item_data.to_dict()
                gainers.append(gainers_item)

        losers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.losers, Unset):
            losers = []
            for losers_item_data in self.losers:
                losers_item = losers_item_data.to_dict()
                losers.append(losers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if gainers is not UNSET:
            field_dict["gainers"] = gainers
        if losers is not UNSET:
            field_dict["losers"] = losers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_v1_movers_response_200_gainers_item import (
            GetV1MoversResponse200GainersItem,
        )
        from ..models.get_v1_movers_response_200_losers_item import (
            GetV1MoversResponse200LosersItem,
        )

        d = dict(src_dict)
        success = d.pop("success")

        _gainers = d.pop("gainers", UNSET)
        gainers: list[GetV1MoversResponse200GainersItem] | Unset = UNSET
        if _gainers is not UNSET:
            gainers = []
            for gainers_item_data in _gainers:
                gainers_item = GetV1MoversResponse200GainersItem.from_dict(
                    gainers_item_data
                )

                gainers.append(gainers_item)

        _losers = d.pop("losers", UNSET)
        losers: list[GetV1MoversResponse200LosersItem] | Unset = UNSET
        if _losers is not UNSET:
            losers = []
            for losers_item_data in _losers:
                losers_item = GetV1MoversResponse200LosersItem.from_dict(
                    losers_item_data
                )

                losers.append(losers_item)

        get_v1_movers_response_200 = cls(
            success=success,
            gainers=gainers,
            losers=losers,
        )

        get_v1_movers_response_200.additional_properties = d
        return get_v1_movers_response_200

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
