from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_market_status_response_200 import GetV1MarketStatusResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/market/status",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MarketStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MarketStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1MarketStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MarketStatusResponse200]:
    """Market status

     Whether the US stock market is open, the next open or close, SPY/DIA/QQQ and BTC readings, SPY-based
    sentiment, and the skill version. Poll it at the top of each loop. `sp500`, `dow`, and `nasdaq` are
    the SPY, DIA, and QQQ ETF prices, not index points. Tiers without real-time data get the 15-minute
    delayed last trade for every reading (`delayed: true`, `X-Data-Delay: 15m`). A reading with no price
    is null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MarketStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MarketStatusResponse200 | None:
    """Market status

     Whether the US stock market is open, the next open or close, SPY/DIA/QQQ and BTC readings, SPY-based
    sentiment, and the skill version. Poll it at the top of each loop. `sp500`, `dow`, and `nasdaq` are
    the SPY, DIA, and QQQ ETF prices, not index points. Tiers without real-time data get the 15-minute
    delayed last trade for every reading (`delayed: true`, `X-Data-Delay: 15m`). A reading with no price
    is null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MarketStatusResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MarketStatusResponse200]:
    """Market status

     Whether the US stock market is open, the next open or close, SPY/DIA/QQQ and BTC readings, SPY-based
    sentiment, and the skill version. Poll it at the top of each loop. `sp500`, `dow`, and `nasdaq` are
    the SPY, DIA, and QQQ ETF prices, not index points. Tiers without real-time data get the 15-minute
    delayed last trade for every reading (`delayed: true`, `X-Data-Delay: 15m`). A reading with no price
    is null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MarketStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MarketStatusResponse200 | None:
    """Market status

     Whether the US stock market is open, the next open or close, SPY/DIA/QQQ and BTC readings, SPY-based
    sentiment, and the skill version. Poll it at the top of each loop. `sp500`, `dow`, and `nasdaq` are
    the SPY, DIA, and QQQ ETF prices, not index points. Tiers without real-time data get the 15-minute
    delayed last trade for every reading (`delayed: true`, `X-Data-Delay: 15m`). A reading with no price
    is null.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MarketStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
