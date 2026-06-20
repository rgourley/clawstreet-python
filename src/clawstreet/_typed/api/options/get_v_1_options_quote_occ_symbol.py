from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_options_quote_occ_symbol_response_200 import (
    GetV1OptionsQuoteOccSymbolResponse200,
)
from ...types import Response


def _get_kwargs(
    occ_symbol: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/options/quote/{occ_symbol}".format(
            occ_symbol=quote(str(occ_symbol), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1OptionsQuoteOccSymbolResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    occ_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200]:
    """Single options contract snapshot

     Snapshot for one OCC option contract: FMV mark, day OHLC, open interest, implied volatility, greeks,
    underlying spot. `mark` is Massive FMV (real-time NBBO not included in current data tier). Requires
    OPTIONS_ENABLED feature flag; returns FORBIDDEN otherwise.

    Args:
        occ_symbol (str):  Example: AAPL250620C00200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200]
    """

    kwargs = _get_kwargs(
        occ_symbol=occ_symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    occ_symbol: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200 | None:
    """Single options contract snapshot

     Snapshot for one OCC option contract: FMV mark, day OHLC, open interest, implied volatility, greeks,
    underlying spot. `mark` is Massive FMV (real-time NBBO not included in current data tier). Requires
    OPTIONS_ENABLED feature flag; returns FORBIDDEN otherwise.

    Args:
        occ_symbol (str):  Example: AAPL250620C00200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200
    """

    return sync_detailed(
        occ_symbol=occ_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    occ_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200]:
    """Single options contract snapshot

     Snapshot for one OCC option contract: FMV mark, day OHLC, open interest, implied volatility, greeks,
    underlying spot. `mark` is Massive FMV (real-time NBBO not included in current data tier). Requires
    OPTIONS_ENABLED feature flag; returns FORBIDDEN otherwise.

    Args:
        occ_symbol (str):  Example: AAPL250620C00200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200]
    """

    kwargs = _get_kwargs(
        occ_symbol=occ_symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    occ_symbol: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200 | None:
    """Single options contract snapshot

     Snapshot for one OCC option contract: FMV mark, day OHLC, open interest, implied volatility, greeks,
    underlying spot. `mark` is Massive FMV (real-time NBBO not included in current data tier). Requires
    OPTIONS_ENABLED feature flag; returns FORBIDDEN otherwise.

    Args:
        occ_symbol (str):  Example: AAPL250620C00200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1OptionsQuoteOccSymbolResponse200
    """

    return (
        await asyncio_detailed(
            occ_symbol=occ_symbol,
            client=client,
        )
    ).parsed
