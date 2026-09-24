from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_history_refresh import (
    GetV1SymbolsSymbolHistoryRefresh,
)
from ...models.get_v1_symbols_symbol_history_response_200 import (
    GetV1SymbolsSymbolHistoryResponse200,
)
from ...models.get_v1_symbols_symbol_history_timespan import (
    GetV1SymbolsSymbolHistoryTimespan,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    periods: int | Unset = UNSET,
    timespan: GetV1SymbolsSymbolHistoryTimespan | Unset = UNSET,
    refresh: GetV1SymbolsSymbolHistoryRefresh | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["periods"] = periods

    json_timespan: str | Unset = UNSET
    if not isinstance(timespan, Unset):
        json_timespan = timespan.value

    params["timespan"] = json_timespan

    json_refresh: str | Unset = UNSET
    if not isinstance(refresh, Unset):
        json_refresh = refresh.value

    params["refresh"] = json_refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/history".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolHistoryResponse200.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200]:
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
    timespan: GetV1SymbolsSymbolHistoryTimespan | Unset = UNSET,
    refresh: GetV1SymbolsSymbolHistoryRefresh | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200]:
    """Price history with RSI and derived fields

     The last `periods` bars as arrays, oldest first: `open`, `high`, `low`, `prices` (close), `volumes`,
    and `rsi` (RSI 14 per bar). Also `current_price` and `derived` (price_change_1d, price_change_5d,
    volume_ratio, rsi_trend, bb_position, distance_from_sma50). `timespan=hour` returns hourly bars
    (stocks). For plain daily OHLCV use /v1/symbols/{symbol}/bars. A lookback above the tier's market-
    history days returns 402 `UPGRADE_REQUIRED`. Tiers without real-time data get the delayed last trade
    as `current_price` (`delayed: true`), and the running bar is left out of every series.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Bars to return. Default 20. Example: 20.
        timespan (GetV1SymbolsSymbolHistoryTimespan | Unset): Bar size. Default day.
        refresh (GetV1SymbolsSymbolHistoryRefresh | Unset): Skip the server bar cache.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        periods=periods,
        timespan=timespan,
        refresh=refresh,
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
    timespan: GetV1SymbolsSymbolHistoryTimespan | Unset = UNSET,
    refresh: GetV1SymbolsSymbolHistoryRefresh | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200 | None:
    """Price history with RSI and derived fields

     The last `periods` bars as arrays, oldest first: `open`, `high`, `low`, `prices` (close), `volumes`,
    and `rsi` (RSI 14 per bar). Also `current_price` and `derived` (price_change_1d, price_change_5d,
    volume_ratio, rsi_trend, bb_position, distance_from_sma50). `timespan=hour` returns hourly bars
    (stocks). For plain daily OHLCV use /v1/symbols/{symbol}/bars. A lookback above the tier's market-
    history days returns 402 `UPGRADE_REQUIRED`. Tiers without real-time data get the delayed last trade
    as `current_price` (`delayed: true`), and the running bar is left out of every series.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Bars to return. Default 20. Example: 20.
        timespan (GetV1SymbolsSymbolHistoryTimespan | Unset): Bar size. Default day.
        refresh (GetV1SymbolsSymbolHistoryRefresh | Unset): Skip the server bar cache.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        periods=periods,
        timespan=timespan,
        refresh=refresh,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    periods: int | Unset = UNSET,
    timespan: GetV1SymbolsSymbolHistoryTimespan | Unset = UNSET,
    refresh: GetV1SymbolsSymbolHistoryRefresh | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200]:
    """Price history with RSI and derived fields

     The last `periods` bars as arrays, oldest first: `open`, `high`, `low`, `prices` (close), `volumes`,
    and `rsi` (RSI 14 per bar). Also `current_price` and `derived` (price_change_1d, price_change_5d,
    volume_ratio, rsi_trend, bb_position, distance_from_sma50). `timespan=hour` returns hourly bars
    (stocks). For plain daily OHLCV use /v1/symbols/{symbol}/bars. A lookback above the tier's market-
    history days returns 402 `UPGRADE_REQUIRED`. Tiers without real-time data get the delayed last trade
    as `current_price` (`delayed: true`), and the running bar is left out of every series.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Bars to return. Default 20. Example: 20.
        timespan (GetV1SymbolsSymbolHistoryTimespan | Unset): Bar size. Default day.
        refresh (GetV1SymbolsSymbolHistoryRefresh | Unset): Skip the server bar cache.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        periods=periods,
        timespan=timespan,
        refresh=refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    periods: int | Unset = UNSET,
    timespan: GetV1SymbolsSymbolHistoryTimespan | Unset = UNSET,
    refresh: GetV1SymbolsSymbolHistoryRefresh | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200 | None:
    """Price history with RSI and derived fields

     The last `periods` bars as arrays, oldest first: `open`, `high`, `low`, `prices` (close), `volumes`,
    and `rsi` (RSI 14 per bar). Also `current_price` and `derived` (price_change_1d, price_change_5d,
    volume_ratio, rsi_trend, bb_position, distance_from_sma50). `timespan=hour` returns hourly bars
    (stocks). For plain daily OHLCV use /v1/symbols/{symbol}/bars. A lookback above the tier's market-
    history days returns 402 `UPGRADE_REQUIRED`. Tiers without real-time data get the delayed last trade
    as `current_price` (`delayed: true`), and the running bar is left out of every series.

    Args:
        symbol (str):  Example: AAPL.
        periods (int | Unset): Bars to return. Default 20. Example: 20.
        timespan (GetV1SymbolsSymbolHistoryTimespan | Unset): Bar size. Default day.
        refresh (GetV1SymbolsSymbolHistoryRefresh | Unset): Skip the server bar cache.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolHistoryResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            periods=periods,
            timespan=timespan,
            refresh=refresh,
        )
    ).parsed
