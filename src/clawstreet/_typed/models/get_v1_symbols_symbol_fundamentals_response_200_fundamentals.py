from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_v1_symbols_symbol_fundamentals_response_200_fundamentals_annual_net_income_basis import (
    GetV1SymbolsSymbolFundamentalsResponse200FundamentalsAnnualNetIncomeBasis,
)
from ..models.get_v1_symbols_symbol_fundamentals_response_200_fundamentals_pe_basis import (
    GetV1SymbolsSymbolFundamentalsResponse200FundamentalsPeBasis,
)

T = TypeVar("T", bound="GetV1SymbolsSymbolFundamentalsResponse200Fundamentals")


@_attrs_define
class GetV1SymbolsSymbolFundamentalsResponse200Fundamentals:
    """
    Attributes:
        ticker (str):
        revenue (float | None):
        net_income (float | None): Net income for the newest quarter only.
        eps (float | None):
        pe_ratio (float | None):
        pe_basis (GetV1SymbolsSymbolFundamentalsResponse200FundamentalsPeBasis):
        debt_to_equity (float | None):
        market_cap (float | None):
        operating_cash_flow (float | None):
        operating_cash_flow_period (None | str):
        total_assets (float | None):
        total_liabilities (float | None):
        filing_date (None | str):
        fiscal_period (None | str):
        annual_net_income (float | None): Trailing-twelve-month net income, or the newest annual filing's.
        annual_net_income_period (None | str):
        annual_net_income_basis (GetV1SymbolsSymbolFundamentalsResponse200FundamentalsAnnualNetIncomeBasis):
    """

    ticker: str
    revenue: float | None
    net_income: float | None
    eps: float | None
    pe_ratio: float | None
    pe_basis: GetV1SymbolsSymbolFundamentalsResponse200FundamentalsPeBasis
    debt_to_equity: float | None
    market_cap: float | None
    operating_cash_flow: float | None
    operating_cash_flow_period: None | str
    total_assets: float | None
    total_liabilities: float | None
    filing_date: None | str
    fiscal_period: None | str
    annual_net_income: float | None
    annual_net_income_period: None | str
    annual_net_income_basis: (
        GetV1SymbolsSymbolFundamentalsResponse200FundamentalsAnnualNetIncomeBasis
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        revenue: float | None
        revenue = self.revenue

        net_income: float | None
        net_income = self.net_income

        eps: float | None
        eps = self.eps

        pe_ratio: float | None
        pe_ratio = self.pe_ratio

        pe_basis = self.pe_basis.value

        debt_to_equity: float | None
        debt_to_equity = self.debt_to_equity

        market_cap: float | None
        market_cap = self.market_cap

        operating_cash_flow: float | None
        operating_cash_flow = self.operating_cash_flow

        operating_cash_flow_period: None | str
        operating_cash_flow_period = self.operating_cash_flow_period

        total_assets: float | None
        total_assets = self.total_assets

        total_liabilities: float | None
        total_liabilities = self.total_liabilities

        filing_date: None | str
        filing_date = self.filing_date

        fiscal_period: None | str
        fiscal_period = self.fiscal_period

        annual_net_income: float | None
        annual_net_income = self.annual_net_income

        annual_net_income_period: None | str
        annual_net_income_period = self.annual_net_income_period

        annual_net_income_basis = self.annual_net_income_basis.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "revenue": revenue,
                "net_income": net_income,
                "eps": eps,
                "pe_ratio": pe_ratio,
                "pe_basis": pe_basis,
                "debt_to_equity": debt_to_equity,
                "market_cap": market_cap,
                "operating_cash_flow": operating_cash_flow,
                "operating_cash_flow_period": operating_cash_flow_period,
                "total_assets": total_assets,
                "total_liabilities": total_liabilities,
                "filing_date": filing_date,
                "fiscal_period": fiscal_period,
                "annual_net_income": annual_net_income,
                "annual_net_income_period": annual_net_income_period,
                "annual_net_income_basis": annual_net_income_basis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        def _parse_revenue(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        revenue = _parse_revenue(d.pop("revenue"))

        def _parse_net_income(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        net_income = _parse_net_income(d.pop("net_income"))

        def _parse_eps(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        eps = _parse_eps(d.pop("eps"))

        def _parse_pe_ratio(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        pe_ratio = _parse_pe_ratio(d.pop("pe_ratio"))

        pe_basis = GetV1SymbolsSymbolFundamentalsResponse200FundamentalsPeBasis(
            d.pop("pe_basis")
        )

        def _parse_debt_to_equity(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        debt_to_equity = _parse_debt_to_equity(d.pop("debt_to_equity"))

        def _parse_market_cap(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        market_cap = _parse_market_cap(d.pop("market_cap"))

        def _parse_operating_cash_flow(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        operating_cash_flow = _parse_operating_cash_flow(d.pop("operating_cash_flow"))

        def _parse_operating_cash_flow_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operating_cash_flow_period = _parse_operating_cash_flow_period(
            d.pop("operating_cash_flow_period")
        )

        def _parse_total_assets(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total_assets = _parse_total_assets(d.pop("total_assets"))

        def _parse_total_liabilities(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        total_liabilities = _parse_total_liabilities(d.pop("total_liabilities"))

        def _parse_filing_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        filing_date = _parse_filing_date(d.pop("filing_date"))

        def _parse_fiscal_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fiscal_period = _parse_fiscal_period(d.pop("fiscal_period"))

        def _parse_annual_net_income(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        annual_net_income = _parse_annual_net_income(d.pop("annual_net_income"))

        def _parse_annual_net_income_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annual_net_income_period = _parse_annual_net_income_period(
            d.pop("annual_net_income_period")
        )

        annual_net_income_basis = (
            GetV1SymbolsSymbolFundamentalsResponse200FundamentalsAnnualNetIncomeBasis(
                d.pop("annual_net_income_basis")
            )
        )

        get_v1_symbols_symbol_fundamentals_response_200_fundamentals = cls(
            ticker=ticker,
            revenue=revenue,
            net_income=net_income,
            eps=eps,
            pe_ratio=pe_ratio,
            pe_basis=pe_basis,
            debt_to_equity=debt_to_equity,
            market_cap=market_cap,
            operating_cash_flow=operating_cash_flow,
            operating_cash_flow_period=operating_cash_flow_period,
            total_assets=total_assets,
            total_liabilities=total_liabilities,
            filing_date=filing_date,
            fiscal_period=fiscal_period,
            annual_net_income=annual_net_income,
            annual_net_income_period=annual_net_income_period,
            annual_net_income_basis=annual_net_income_basis,
        )

        get_v1_symbols_symbol_fundamentals_response_200_fundamentals.additional_properties = d
        return get_v1_symbols_symbol_fundamentals_response_200_fundamentals

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
