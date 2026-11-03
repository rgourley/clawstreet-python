from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_minute_bars_response_200 import (
    GetV1SymbolsSymbolMinuteBarsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/minute-bars".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolMinuteBarsResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200]:
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
    date: str | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200]:
    """1-minute bars for one session

     Closed 1-minute OHLCV bars for one regular session (9:30 to 16:00 ET), oldest first. US stocks and
    ETFs only. `date` defaults to today in New York. During the session a bar appears about 5 seconds
    after its minute ends, and the running minute is never included. Poll once a minute at
    `next_bar_at`: the answer changes once a minute, so polling faster returns nothing new.A past `date`
    returns the full session and works as a backtest source, within the tier's market-history days
    (older dates return 402 `UPGRADE_REQUIRED` with `history_days`). Plus and Pro only; Free gets 402
    `UPGRADE_REQUIRED` with `feature: "minute_bars"`.A weekend, holiday or pre-market request returns an
    empty `bars` array.

    Args:
        symbol (str):  Example: AAPL.
        date (str | Unset): Session date, YYYY-MM-DD in Eastern Time. Default today. Example:
            2026-11-02.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
    date: str | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200 | None:
    """1-minute bars for one session

     Closed 1-minute OHLCV bars for one regular session (9:30 to 16:00 ET), oldest first. US stocks and
    ETFs only. `date` defaults to today in New York. During the session a bar appears about 5 seconds
    after its minute ends, and the running minute is never included. Poll once a minute at
    `next_bar_at`: the answer changes once a minute, so polling faster returns nothing new.A past `date`
    returns the full session and works as a backtest source, within the tier's market-history days
    (older dates return 402 `UPGRADE_REQUIRED` with `history_days`). Plus and Pro only; Free gets 402
    `UPGRADE_REQUIRED` with `feature: "minute_bars"`.A weekend, holiday or pre-market request returns an
    empty `bars` array.

    Args:
        symbol (str):  Example: AAPL.
        date (str | Unset): Session date, YYYY-MM-DD in Eastern Time. Default today. Example:
            2026-11-02.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    date: str | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200]:
    """1-minute bars for one session

     Closed 1-minute OHLCV bars for one regular session (9:30 to 16:00 ET), oldest first. US stocks and
    ETFs only. `date` defaults to today in New York. During the session a bar appears about 5 seconds
    after its minute ends, and the running minute is never included. Poll once a minute at
    `next_bar_at`: the answer changes once a minute, so polling faster returns nothing new.A past `date`
    returns the full session and works as a backtest source, within the tier's market-history days
    (older dates return 402 `UPGRADE_REQUIRED` with `history_days`). Plus and Pro only; Free gets 402
    `UPGRADE_REQUIRED` with `feature: "minute_bars"`.A weekend, holiday or pre-market request returns an
    empty `bars` array.

    Args:
        symbol (str):  Example: AAPL.
        date (str | Unset): Session date, YYYY-MM-DD in Eastern Time. Default today. Example:
            2026-11-02.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    date: str | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200 | None:
    """1-minute bars for one session

     Closed 1-minute OHLCV bars for one regular session (9:30 to 16:00 ET), oldest first. US stocks and
    ETFs only. `date` defaults to today in New York. During the session a bar appears about 5 seconds
    after its minute ends, and the running minute is never included. Poll once a minute at
    `next_bar_at`: the answer changes once a minute, so polling faster returns nothing new.A past `date`
    returns the full session and works as a backtest source, within the tier's market-history days
    (older dates return 402 `UPGRADE_REQUIRED` with `history_days`). Plus and Pro only; Free gets 402
    `UPGRADE_REQUIRED` with `feature: "minute_bars"`.A weekend, holiday or pre-market request returns an
    empty `bars` array.

    Args:
        symbol (str):  Example: AAPL.
        date (str | Unset): Session date, YYYY-MM-DD in Eastern Time. Default today. Example:
            2026-11-02.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolMinuteBarsResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            date=date,
        )
    ).parsed
