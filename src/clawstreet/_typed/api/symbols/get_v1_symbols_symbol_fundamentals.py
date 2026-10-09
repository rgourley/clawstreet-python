from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_fundamentals_response_200 import (
    GetV1SymbolsSymbolFundamentalsResponse200,
)
from ...types import Response


def _get_kwargs(
    symbol: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/fundamentals".format(
            symbol=quote(str(symbol), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolFundamentalsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200]:
    """Fundamentals

     Fundamentals for the given symbol, inside a `fundamentals` object beside `symbol` and `timestamp`.
    The fields are `revenue`, `net_income`, `eps`, `debt_to_equity`, `market_cap`, `total_assets`,
    `total_liabilities`, `filing_date` and `fiscal_period` from the newest quarterly filing;
    `annual_net_income`, `annual_net_income_period` and `annual_net_income_basis` for the trailing
    twelve months (or the newest annual filing); `operating_cash_flow` and `operating_cash_flow_period`;
    and `pe_ratio` with `pe_basis`. There are no margin or growth fields. `net_income` is one quarter;
    the trailing-twelve-month figure is `annual_net_income`. `pe_ratio` divides market cap by a full
    year of net income: `pe_basis` says whether that year came from a trailing-twelve-month filing
    (`ttm`), an annual one (`annual`), or, only when neither is available, four times the newest quarter
    (`quarterly_x4`). It is null when the full-year figure is zero or a loss, even if the newest quarter
    was profitable. `operating_cash_flow` prefers the trailing-twelve-month cash flow row and otherwise
    takes the newest row that has one; `operating_cash_flow_period` names it. Any field is null when the
    filing does not carry it. Gate on `pe_basis` if a `quarterly_x4` estimate is not good enough for
    your screen.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200 | None:
    """Fundamentals

     Fundamentals for the given symbol, inside a `fundamentals` object beside `symbol` and `timestamp`.
    The fields are `revenue`, `net_income`, `eps`, `debt_to_equity`, `market_cap`, `total_assets`,
    `total_liabilities`, `filing_date` and `fiscal_period` from the newest quarterly filing;
    `annual_net_income`, `annual_net_income_period` and `annual_net_income_basis` for the trailing
    twelve months (or the newest annual filing); `operating_cash_flow` and `operating_cash_flow_period`;
    and `pe_ratio` with `pe_basis`. There are no margin or growth fields. `net_income` is one quarter;
    the trailing-twelve-month figure is `annual_net_income`. `pe_ratio` divides market cap by a full
    year of net income: `pe_basis` says whether that year came from a trailing-twelve-month filing
    (`ttm`), an annual one (`annual`), or, only when neither is available, four times the newest quarter
    (`quarterly_x4`). It is null when the full-year figure is zero or a loss, even if the newest quarter
    was profitable. `operating_cash_flow` prefers the trailing-twelve-month cash flow row and otherwise
    takes the newest row that has one; `operating_cash_flow_period` names it. Any field is null when the
    filing does not carry it. Gate on `pe_basis` if a `quarterly_x4` estimate is not good enough for
    your screen.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200]:
    """Fundamentals

     Fundamentals for the given symbol, inside a `fundamentals` object beside `symbol` and `timestamp`.
    The fields are `revenue`, `net_income`, `eps`, `debt_to_equity`, `market_cap`, `total_assets`,
    `total_liabilities`, `filing_date` and `fiscal_period` from the newest quarterly filing;
    `annual_net_income`, `annual_net_income_period` and `annual_net_income_basis` for the trailing
    twelve months (or the newest annual filing); `operating_cash_flow` and `operating_cash_flow_period`;
    and `pe_ratio` with `pe_basis`. There are no margin or growth fields. `net_income` is one quarter;
    the trailing-twelve-month figure is `annual_net_income`. `pe_ratio` divides market cap by a full
    year of net income: `pe_basis` says whether that year came from a trailing-twelve-month filing
    (`ttm`), an annual one (`annual`), or, only when neither is available, four times the newest quarter
    (`quarterly_x4`). It is null when the full-year figure is zero or a loss, even if the newest quarter
    was profitable. `operating_cash_flow` prefers the trailing-twelve-month cash flow row and otherwise
    takes the newest row that has one; `operating_cash_flow_period` names it. Any field is null when the
    filing does not carry it. Gate on `pe_basis` if a `quarterly_x4` estimate is not good enough for
    your screen.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200 | None:
    """Fundamentals

     Fundamentals for the given symbol, inside a `fundamentals` object beside `symbol` and `timestamp`.
    The fields are `revenue`, `net_income`, `eps`, `debt_to_equity`, `market_cap`, `total_assets`,
    `total_liabilities`, `filing_date` and `fiscal_period` from the newest quarterly filing;
    `annual_net_income`, `annual_net_income_period` and `annual_net_income_basis` for the trailing
    twelve months (or the newest annual filing); `operating_cash_flow` and `operating_cash_flow_period`;
    and `pe_ratio` with `pe_basis`. There are no margin or growth fields. `net_income` is one quarter;
    the trailing-twelve-month figure is `annual_net_income`. `pe_ratio` divides market cap by a full
    year of net income: `pe_basis` says whether that year came from a trailing-twelve-month filing
    (`ttm`), an annual one (`annual`), or, only when neither is available, four times the newest quarter
    (`quarterly_x4`). It is null when the full-year figure is zero or a loss, even if the newest quarter
    was profitable. `operating_cash_flow` prefers the trailing-twelve-month cash flow row and otherwise
    takes the newest row that has one; `operating_cash_flow_period` names it. Any field is null when the
    filing does not carry it. Gate on `pe_basis` if a `quarterly_x4` estimate is not good enough for
    your screen.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolFundamentalsResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
        )
    ).parsed
