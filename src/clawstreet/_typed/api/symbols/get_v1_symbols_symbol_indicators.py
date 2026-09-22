from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_indicators_response_200 import (
    GetV1SymbolsSymbolIndicatorsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    indicators: str,
    window: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["indicators"] = indicators

    params["window"] = window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/indicators".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolIndicatorsResponse200.from_dict(
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

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200]:
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
    indicators: str,
    window: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200]:
    """Technical indicators

     The latest value of each requested indicator. `indicators` is required, comma-separated. Available:
    rsi, rsi7, rsi21, macd, bollingerBands, sma20, sma50, ema9, ema12, ema21, ema26, ema50, atr,
    stochastic, adx, williamsR, vwap, volume, volumeAvg20, mfi, obv, cci, roc, stochRsi, massiveEma,
    massiveSma, massiveMacd. `window` sets the massiveEma and massiveSma lookback. A window above the
    tier's market-history days returns 402 `UPGRADE_REQUIRED`.

    Args:
        symbol (str):  Example: AAPL.
        indicators (str):  Example: rsi,macd,bollingerBands.
        window (int | Unset): Lookback for massiveEma and massiveSma. Default 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        indicators=indicators,
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
    indicators: str,
    window: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200 | None:
    """Technical indicators

     The latest value of each requested indicator. `indicators` is required, comma-separated. Available:
    rsi, rsi7, rsi21, macd, bollingerBands, sma20, sma50, ema9, ema12, ema21, ema26, ema50, atr,
    stochastic, adx, williamsR, vwap, volume, volumeAvg20, mfi, obv, cci, roc, stochRsi, massiveEma,
    massiveSma, massiveMacd. `window` sets the massiveEma and massiveSma lookback. A window above the
    tier's market-history days returns 402 `UPGRADE_REQUIRED`.

    Args:
        symbol (str):  Example: AAPL.
        indicators (str):  Example: rsi,macd,bollingerBands.
        window (int | Unset): Lookback for massiveEma and massiveSma. Default 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        indicators=indicators,
        window=window,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    indicators: str,
    window: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200]:
    """Technical indicators

     The latest value of each requested indicator. `indicators` is required, comma-separated. Available:
    rsi, rsi7, rsi21, macd, bollingerBands, sma20, sma50, ema9, ema12, ema21, ema26, ema50, atr,
    stochastic, adx, williamsR, vwap, volume, volumeAvg20, mfi, obv, cci, roc, stochRsi, massiveEma,
    massiveSma, massiveMacd. `window` sets the massiveEma and massiveSma lookback. A window above the
    tier's market-history days returns 402 `UPGRADE_REQUIRED`.

    Args:
        symbol (str):  Example: AAPL.
        indicators (str):  Example: rsi,macd,bollingerBands.
        window (int | Unset): Lookback for massiveEma and massiveSma. Default 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        indicators=indicators,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    indicators: str,
    window: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200 | None:
    """Technical indicators

     The latest value of each requested indicator. `indicators` is required, comma-separated. Available:
    rsi, rsi7, rsi21, macd, bollingerBands, sma20, sma50, ema9, ema12, ema21, ema26, ema50, atr,
    stochastic, adx, williamsR, vwap, volume, volumeAvg20, mfi, obv, cci, roc, stochRsi, massiveEma,
    massiveSma, massiveMacd. `window` sets the massiveEma and massiveSma lookback. A window above the
    tier's market-history days returns 402 `UPGRADE_REQUIRED`.

    Args:
        symbol (str):  Example: AAPL.
        indicators (str):  Example: rsi,macd,bollingerBands.
        window (int | Unset): Lookback for massiveEma and massiveSma. Default 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolIndicatorsResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            indicators=indicators,
            window=window,
        )
    ).parsed
