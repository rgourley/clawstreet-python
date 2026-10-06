from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_earnings_response_200 import (
    GetV1SymbolsSymbolEarningsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    days: int | Unset = UNSET,
    past: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    json_past: int | None | Unset
    if isinstance(past, Unset):
        json_past = UNSET
    else:
        json_past = past
    params["past"] = json_past

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/earnings".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolEarningsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200]:
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
    days: int | Unset = UNSET,
    past: int | None | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200]:
    """Symbol earnings history

     Past and upcoming earnings reports for one symbol, oldest first. The list has the last `past`
    reports before today (actual EPS, actual revenue and surprise percentages) and the reports from
    today to `days` ahead. Read `status` to tell them apart: `reported` or `no_data` for past reports,
    `upcoming` for the next one.

    Args:
        symbol (str):  Example: AAPL.
        days (int | Unset): Days ahead to cover for upcoming reports, 1 to 90. Defaults to 30.
            Values outside the range are clamped.
        past (int | None | Unset): Number of past reports to include, 0 to 20. Defaults to 0, so a
            request with only `days` returns upcoming reports. Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        days=days,
        past=past,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    past: int | None | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200 | None:
    """Symbol earnings history

     Past and upcoming earnings reports for one symbol, oldest first. The list has the last `past`
    reports before today (actual EPS, actual revenue and surprise percentages) and the reports from
    today to `days` ahead. Read `status` to tell them apart: `reported` or `no_data` for past reports,
    `upcoming` for the next one.

    Args:
        symbol (str):  Example: AAPL.
        days (int | Unset): Days ahead to cover for upcoming reports, 1 to 90. Defaults to 30.
            Values outside the range are clamped.
        past (int | None | Unset): Number of past reports to include, 0 to 20. Defaults to 0, so a
            request with only `days` returns upcoming reports. Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        days=days,
        past=past,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    past: int | None | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200]:
    """Symbol earnings history

     Past and upcoming earnings reports for one symbol, oldest first. The list has the last `past`
    reports before today (actual EPS, actual revenue and surprise percentages) and the reports from
    today to `days` ahead. Read `status` to tell them apart: `reported` or `no_data` for past reports,
    `upcoming` for the next one.

    Args:
        symbol (str):  Example: AAPL.
        days (int | Unset): Days ahead to cover for upcoming reports, 1 to 90. Defaults to 30.
            Values outside the range are clamped.
        past (int | None | Unset): Number of past reports to include, 0 to 20. Defaults to 0, so a
            request with only `days` returns upcoming reports. Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        days=days,
        past=past,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    past: int | None | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200 | None:
    """Symbol earnings history

     Past and upcoming earnings reports for one symbol, oldest first. The list has the last `past`
    reports before today (actual EPS, actual revenue and surprise percentages) and the reports from
    today to `days` ahead. Read `status` to tell them apart: `reported` or `no_data` for past reports,
    `upcoming` for the next one.

    Args:
        symbol (str):  Example: AAPL.
        days (int | Unset): Days ahead to cover for upcoming reports, 1 to 90. Defaults to 30.
            Values outside the range are clamped.
        past (int | None | Unset): Number of past reports to include, 0 to 20. Defaults to 0, so a
            request with only `days` returns upcoming reports. Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolEarningsResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            days=days,
            past=past,
        )
    ).parsed
