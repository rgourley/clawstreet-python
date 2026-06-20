from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_quotes_response_200 import GetV1QuotesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    symbols: str,
    fresh: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["symbols"] = symbols

    params["fresh"] = fresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/quotes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1QuotesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1QuotesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

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
) -> Response[ErrorEnvelope | GetV1QuotesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    symbols: str,
    fresh: str | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1QuotesResponse200]:
    """Batched quotes

     Latest price + previous close for up to 20 symbols. Pass `?symbols=AAPL,MSFT,BTC-USD`. `?fresh=1`
    disables caching.

    Args:
        symbols (str):
        fresh (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1QuotesResponse200]
    """

    kwargs = _get_kwargs(
        symbols=symbols,
        fresh=fresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    symbols: str,
    fresh: str | Unset = UNSET,
) -> ErrorEnvelope | GetV1QuotesResponse200 | None:
    """Batched quotes

     Latest price + previous close for up to 20 symbols. Pass `?symbols=AAPL,MSFT,BTC-USD`. `?fresh=1`
    disables caching.

    Args:
        symbols (str):
        fresh (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1QuotesResponse200
    """

    return sync_detailed(
        client=client,
        symbols=symbols,
        fresh=fresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    symbols: str,
    fresh: str | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1QuotesResponse200]:
    """Batched quotes

     Latest price + previous close for up to 20 symbols. Pass `?symbols=AAPL,MSFT,BTC-USD`. `?fresh=1`
    disables caching.

    Args:
        symbols (str):
        fresh (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1QuotesResponse200]
    """

    kwargs = _get_kwargs(
        symbols=symbols,
        fresh=fresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    symbols: str,
    fresh: str | Unset = UNSET,
) -> ErrorEnvelope | GetV1QuotesResponse200 | None:
    """Batched quotes

     Latest price + previous close for up to 20 symbols. Pass `?symbols=AAPL,MSFT,BTC-USD`. `?fresh=1`
    disables caching.

    Args:
        symbols (str):
        fresh (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1QuotesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            symbols=symbols,
            fresh=fresh,
        )
    ).parsed
