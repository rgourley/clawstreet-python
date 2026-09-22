from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_market_response_200 import GetV1MarketResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/market",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MarketResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MarketResponse200.from_dict(response.json())

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
) -> Response[ErrorEnvelope | GetV1MarketResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MarketResponse200]:
    """Market context

     SPY one-day return, SPY-based sentiment, and the one-day return of each SPDR sector ETF. Returns are
    fractions (0.012 is +1.2%). A ticker without a usable price is left out, never reported as flat.
    `asOf` is the oldest reading in the payload and `dataAgeSeconds` is its age. Tiers without real-time
    data get returns from the 15-minute delayed last trade (`delayed: true`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MarketResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MarketResponse200 | None:
    """Market context

     SPY one-day return, SPY-based sentiment, and the one-day return of each SPDR sector ETF. Returns are
    fractions (0.012 is +1.2%). A ticker without a usable price is left out, never reported as flat.
    `asOf` is the oldest reading in the payload and `dataAgeSeconds` is its age. Tiers without real-time
    data get returns from the 15-minute delayed last trade (`delayed: true`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MarketResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MarketResponse200]:
    """Market context

     SPY one-day return, SPY-based sentiment, and the one-day return of each SPDR sector ETF. Returns are
    fractions (0.012 is +1.2%). A ticker without a usable price is left out, never reported as flat.
    `asOf` is the oldest reading in the payload and `dataAgeSeconds` is its age. Tiers without real-time
    data get returns from the 15-minute delayed last trade (`delayed: true`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MarketResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MarketResponse200 | None:
    """Market context

     SPY one-day return, SPY-based sentiment, and the one-day return of each SPDR sector ETF. Returns are
    fractions (0.012 is +1.2%). A ticker without a usable price is left out, never reported as flat.
    `asOf` is the oldest reading in the payload and `dataAgeSeconds` is its age. Tiers without real-time
    data get returns from the 15-minute delayed last trade (`delayed: true`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MarketResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
