from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.portfolio_limits import PortfolioLimits
    from ..models.portfolio_margin import PortfolioMargin
    from ..models.position import Position


T = TypeVar("T", bound="Portfolio")


@_attrs_define
class Portfolio:
    """
    Attributes:
        success (bool):
        cash (float):
        equity (float):
        buying_power (float): Cash the agent can still deploy, after short collateral and the leverage cap.
        gross_exposure (float): Sum of position values, longs and shorts alike.
        leverage (float): gross_exposure / equity.
        total_return_pct (float):
        unrealized_pl (float):
        margin (PortfolioMargin):
        positions (list[Position]):
        limits (PortfolioLimits):
        initial_balance (float):
    """

    success: bool
    cash: float
    equity: float
    buying_power: float
    gross_exposure: float
    leverage: float
    total_return_pct: float
    unrealized_pl: float
    margin: PortfolioMargin
    positions: list[Position]
    limits: PortfolioLimits
    initial_balance: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        cash = self.cash

        equity = self.equity

        buying_power = self.buying_power

        gross_exposure = self.gross_exposure

        leverage = self.leverage

        total_return_pct = self.total_return_pct

        unrealized_pl = self.unrealized_pl

        margin = self.margin.to_dict()

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        limits = self.limits.to_dict()

        initial_balance = self.initial_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "cash": cash,
                "equity": equity,
                "buying_power": buying_power,
                "gross_exposure": gross_exposure,
                "leverage": leverage,
                "total_return_pct": total_return_pct,
                "unrealized_pl": unrealized_pl,
                "margin": margin,
                "positions": positions,
                "limits": limits,
                "initial_balance": initial_balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.portfolio_limits import PortfolioLimits
        from ..models.portfolio_margin import PortfolioMargin
        from ..models.position import Position

        d = dict(src_dict)
        success = d.pop("success")

        cash = d.pop("cash")

        equity = d.pop("equity")

        buying_power = d.pop("buying_power")

        gross_exposure = d.pop("gross_exposure")

        leverage = d.pop("leverage")

        total_return_pct = d.pop("total_return_pct")

        unrealized_pl = d.pop("unrealized_pl")

        margin = PortfolioMargin.from_dict(d.pop("margin"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        limits = PortfolioLimits.from_dict(d.pop("limits"))

        initial_balance = d.pop("initial_balance")

        portfolio = cls(
            success=success,
            cash=cash,
            equity=equity,
            buying_power=buying_power,
            gross_exposure=gross_exposure,
            leverage=leverage,
            total_return_pct=total_return_pct,
            unrealized_pl=unrealized_pl,
            margin=margin,
            positions=positions,
            limits=limits,
            initial_balance=initial_balance,
        )

        portfolio.additional_properties = d
        return portfolio

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
