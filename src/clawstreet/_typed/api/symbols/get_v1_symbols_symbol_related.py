from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_related_response_200 import (
    GetV1SymbolsSymbolRelatedResponse200,
)
from ...types import Response


def _get_kwargs(
    symbol: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/related".format(
            symbol=quote(str(symbol), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolRelatedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200]:
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
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200]:
    """Related symbols

     Peers and correlated tickers for the given symbol.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200]
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
) -> ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200 | None:
    """Related symbols

     Peers and correlated tickers for the given symbol.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200]:
    """Related symbols

     Peers and correlated tickers for the given symbol.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200]
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
) -> ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200 | None:
    """Related symbols

     Peers and correlated tickers for the given symbol.

    Args:
        symbol (str):  Example: AAPL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolRelatedResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
        )
    ).parsed
