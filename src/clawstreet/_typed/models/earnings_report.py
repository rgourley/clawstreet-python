from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.earnings_report_date_status import EarningsReportDateStatus
from ..models.earnings_report_status import EarningsReportStatus
from ..models.earnings_report_timing import EarningsReportTiming

T = TypeVar("T", bound="EarningsReport")


@_attrs_define
class EarningsReport:
    """
    Attributes:
        symbol (str):  Example: NKE.
        date (str): Report date, YYYY-MM-DD. Example: 2026-10-01.
        timing (EarningsReportTiming): BMO: before 09:30 ET. AMC: 16:00 ET or later. unknown: no time, or a time during
            the session.
        status (EarningsReportStatus): reported: actual EPS or revenue is published. upcoming: no actuals yet and the
            date is today or later. no_data: the date is past but the source has no actuals.
        date_status (EarningsReportDateStatus):
        fiscal_period (None | str):  Example: Q1.
        fiscal_year (int | None):  Example: 2027.
        eps_actual (float | None):  Example: 0.48.
        eps_estimate (float | None): Consensus EPS estimate. Example: 0.44.
        eps_surprise_pct (float | None): (epsActual - epsEstimate) / |epsEstimate| x 100, rounded to 2 decimals. Null
            when either value is missing or the estimate is 0. Example: 9.09.
        revenue_actual (float | None):  Example: 11213000000.
        revenue_estimate (float | None):  Example: 11345709144.
        revenue_surprise_pct (float | None): Same formula as epsSurprisePct, on revenue. Null when either value is
            missing or the estimate is 0. Example: -1.17.
        eps_method (None | str): How the source counts EPS: gaap or adj (adjusted). Example: gaap.
    """

    symbol: str
    date: str
    timing: EarningsReportTiming
    status: EarningsReportStatus
    date_status: EarningsReportDateStatus
    fiscal_period: None | str
    fiscal_year: int | None
    eps_actual: float | None
    eps_estimate: float | None
    eps_surprise_pct: float | None
    revenue_actual: float | None
    revenue_estimate: float | None
    revenue_surprise_pct: float | None
    eps_method: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        date = self.date

        timing = self.timing.value

        status = self.status.value

        date_status = self.date_status.value

        fiscal_period: None | str
        fiscal_period = self.fiscal_period

        fiscal_year: int | None
        fiscal_year = self.fiscal_year

        eps_actual: float | None
        eps_actual = self.eps_actual

        eps_estimate: float | None
        eps_estimate = self.eps_estimate

        eps_surprise_pct: float | None
        eps_surprise_pct = self.eps_surprise_pct

        revenue_actual: float | None
        revenue_actual = self.revenue_actual

        revenue_estimate: float | None
        revenue_estimate = self.revenue_estimate

        revenue_surprise_pct: float | None
        revenue_surprise_pct = self.revenue_surprise_pct

        eps_method: None | str
        eps_method = self.eps_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "date": date,
                "timing": timing,
                "status": status,
                "dateStatus": date_status,
                "fiscalPeriod": fiscal_period,
                "fiscalYear": fiscal_year,
                "epsActual": eps_actual,
                "epsEstimate": eps_estimate,
                "epsSurprisePct": eps_surprise_pct,
                "revenueActual": revenue_actual,
                "revenueEstimate": revenue_estimate,
                "revenueSurprisePct": revenue_surprise_pct,
                "epsMethod": eps_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        date = d.pop("date")

        timing = EarningsReportTiming(d.pop("timing"))

        status = EarningsReportStatus(d.pop("status"))

        date_status = EarningsReportDateStatus(d.pop("dateStatus"))

        def _parse_fiscal_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fiscal_period = _parse_fiscal_period(d.pop("fiscalPeriod"))

        def _parse_fiscal_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        fiscal_year = _parse_fiscal_year(d.pop("fiscalYear"))

        def _parse_eps_actual(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        eps_actual = _parse_eps_actual(d.pop("epsActual"))

        def _parse_eps_estimate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        eps_estimate = _parse_eps_estimate(d.pop("epsEstimate"))

        def _parse_eps_surprise_pct(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        eps_surprise_pct = _parse_eps_surprise_pct(d.pop("epsSurprisePct"))

        def _parse_revenue_actual(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        revenue_actual = _parse_revenue_actual(d.pop("revenueActual"))

        def _parse_revenue_estimate(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        revenue_estimate = _parse_revenue_estimate(d.pop("revenueEstimate"))

        def _parse_revenue_surprise_pct(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        revenue_surprise_pct = _parse_revenue_surprise_pct(d.pop("revenueSurprisePct"))

        def _parse_eps_method(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        eps_method = _parse_eps_method(d.pop("epsMethod"))

        earnings_report = cls(
            symbol=symbol,
            date=date,
            timing=timing,
            status=status,
            date_status=date_status,
            fiscal_period=fiscal_period,
            fiscal_year=fiscal_year,
            eps_actual=eps_actual,
            eps_estimate=eps_estimate,
            eps_surprise_pct=eps_surprise_pct,
            revenue_actual=revenue_actual,
            revenue_estimate=revenue_estimate,
            revenue_surprise_pct=revenue_surprise_pct,
            eps_method=eps_method,
        )

        earnings_report.additional_properties = d
        return earnings_report

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
