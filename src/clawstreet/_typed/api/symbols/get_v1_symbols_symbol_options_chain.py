from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_symbols_symbol_options_chain_response_200 import (
    GetV1SymbolsSymbolOptionsChainResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    expiry: str | Unset = UNSET,
    strike_min: float | None | Unset = UNSET,
    strike_max: float | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expiry"] = expiry

    json_strike_min: float | None | Unset
    if isinstance(strike_min, Unset):
        json_strike_min = UNSET
    else:
        json_strike_min = strike_min
    params["strike_min"] = json_strike_min

    json_strike_max: float | None | Unset
    if isinstance(strike_max, Unset):
        json_strike_max = UNSET
    else:
        json_strike_max = strike_max
    params["strike_max"] = json_strike_max

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/symbols/{symbol}/options-chain".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SymbolsSymbolOptionsChainResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200]:
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
    expiry: str | Unset = UNSET,
    strike_min: float | None | Unset = UNSET,
    strike_max: float | None | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200]:
    """Options chain

     Options chain (calls/puts by strike + expiry) for the symbol (premium).

    Args:
        symbol (str):  Example: AAPL.
        expiry (str | Unset):
        strike_min (float | None | Unset):
        strike_max (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        expiry=expiry,
        strike_min=strike_min,
        strike_max=strike_max,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient,
    expiry: str | Unset = UNSET,
    strike_min: float | None | Unset = UNSET,
    strike_max: float | None | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200 | None:
    """Options chain

     Options chain (calls/puts by strike + expiry) for the symbol (premium).

    Args:
        symbol (str):  Example: AAPL.
        expiry (str | Unset):
        strike_min (float | None | Unset):
        strike_max (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        expiry=expiry,
        strike_min=strike_min,
        strike_max=strike_max,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    expiry: str | Unset = UNSET,
    strike_min: float | None | Unset = UNSET,
    strike_max: float | None | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200]:
    """Options chain

     Options chain (calls/puts by strike + expiry) for the symbol (premium).

    Args:
        symbol (str):  Example: AAPL.
        expiry (str | Unset):
        strike_min (float | None | Unset):
        strike_max (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        expiry=expiry,
        strike_min=strike_min,
        strike_max=strike_max,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    expiry: str | Unset = UNSET,
    strike_min: float | None | Unset = UNSET,
    strike_max: float | None | Unset = UNSET,
) -> ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200 | None:
    """Options chain

     Options chain (calls/puts by strike + expiry) for the symbol (premium).

    Args:
        symbol (str):  Example: AAPL.
        expiry (str | Unset):
        strike_min (float | None | Unset):
        strike_max (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1SymbolsSymbolOptionsChainResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            expiry=expiry,
            strike_min=strike_min,
            strike_max=strike_max,
        )
    ).parsed
