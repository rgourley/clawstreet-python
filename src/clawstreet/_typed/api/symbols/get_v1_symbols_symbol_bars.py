from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_bars_response_200 import (
    GetV1SymbolsSymbolBarsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    periods: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["periods"] = periods

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/bars".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolBarsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200]:
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
    periods: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200]:
    """Historical daily bars

     Daily OHLC bars for a symbol, newest last. `periods` sets how many trading days come back (1 to 100,
    default 30). A tier sees at most its market-history days: asking for more returns 402
    `UPGRADE_REQUIRED` with `history_days` in the details. A tier without real-time data does not get
    the running bar, because its close is the live price. That bar arrives 15 minutes after the session
    ends, and the response says `delayed: true`.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Trading days of bars. Default 30. Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        periods=periods,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
    periods: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200 | None:
    """Historical daily bars

     Daily OHLC bars for a symbol, newest last. `periods` sets how many trading days come back (1 to 100,
    default 30). A tier sees at most its market-history days: asking for more returns 402
    `UPGRADE_REQUIRED` with `history_days` in the details. A tier without real-time data does not get
    the running bar, because its close is the live price. That bar arrives 15 minutes after the session
    ends, and the response says `delayed: true`.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Trading days of bars. Default 30. Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        periods=periods,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    periods: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200]:
    """Historical daily bars

     Daily OHLC bars for a symbol, newest last. `periods` sets how many trading days come back (1 to 100,
    default 30). A tier sees at most its market-history days: asking for more returns 402
    `UPGRADE_REQUIRED` with `history_days` in the details. A tier without real-time data does not get
    the running bar, because its close is the live price. That bar arrives 15 minutes after the session
    ends, and the response says `delayed: true`.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Trading days of bars. Default 30. Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        periods=periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    periods: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200 | None:
    """Historical daily bars

     Daily OHLC bars for a symbol, newest last. `periods` sets how many trading days come back (1 to 100,
    default 30). A tier sees at most its market-history days: asking for more returns 402
    `UPGRADE_REQUIRED` with `history_days` in the details. A tier without real-time data does not get
    the running bar, because its close is the live price. That bar arrives 15 minutes after the session
    ends, and the response says `delayed: true`.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Trading days of bars. Default 30. Example: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolBarsResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            periods=periods,
        )
    ).parsed
