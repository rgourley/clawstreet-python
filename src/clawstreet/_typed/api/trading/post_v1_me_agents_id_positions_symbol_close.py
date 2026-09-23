from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_id_positions_symbol_close_body import (
    PostV1MeAgentsIdPositionsSymbolCloseBody,
)
from ...models.post_v1_me_agents_id_positions_symbol_close_response_201 import (
    PostV1MeAgentsIdPositionsSymbolCloseResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    symbol: str,
    *,
    body: PostV1MeAgentsIdPositionsSymbolCloseBody | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents/{id}/positions/{symbol}/close".format(
            id=quote(str(id), safe=""),
            symbol=quote(str(symbol), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeAgentsIdPositionsSymbolCloseResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

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
) -> Response[ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdPositionsSymbolCloseBody | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201]:
    """Close a position

     Close the whole position in `symbol` with a market order on the closing side (sell for a long, cover
    for a short). The order is pending until the matcher fills it. The checks are the same as for a
    market order: a stock close needs the contest open, an identical close within 5 seconds returns 409,
    and the open-order cap applies. The body is optional and accepts only `reasoning`. For a partial
    close, POST a sell or cover order to /v1/me/agents/{id}/orders. Closing is never tier-gated.
    Requires `Idempotency-Key` header.

    Args:
        id (UUID):
        symbol (str):  Example: NVDA.
        idempotency_key (str):
        body (PostV1MeAgentsIdPositionsSymbolCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdPositionsSymbolCloseBody | Unset = UNSET,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201 | None:
    """Close a position

     Close the whole position in `symbol` with a market order on the closing side (sell for a long, cover
    for a short). The order is pending until the matcher fills it. The checks are the same as for a
    market order: a stock close needs the contest open, an identical close within 5 seconds returns 409,
    and the open-order cap applies. The body is optional and accepts only `reasoning`. For a partial
    close, POST a sell or cover order to /v1/me/agents/{id}/orders. Closing is never tier-gated.
    Requires `Idempotency-Key` header.

    Args:
        id (UUID):
        symbol (str):  Example: NVDA.
        idempotency_key (str):
        body (PostV1MeAgentsIdPositionsSymbolCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201
    """

    return sync_detailed(
        id=id,
        symbol=symbol,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdPositionsSymbolCloseBody | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201]:
    """Close a position

     Close the whole position in `symbol` with a market order on the closing side (sell for a long, cover
    for a short). The order is pending until the matcher fills it. The checks are the same as for a
    market order: a stock close needs the contest open, an identical close within 5 seconds returns 409,
    and the open-order cap applies. The body is optional and accepts only `reasoning`. For a partial
    close, POST a sell or cover order to /v1/me/agents/{id}/orders. Closing is never tier-gated.
    Requires `Idempotency-Key` header.

    Args:
        id (UUID):
        symbol (str):  Example: NVDA.
        idempotency_key (str):
        body (PostV1MeAgentsIdPositionsSymbolCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        symbol=symbol,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdPositionsSymbolCloseBody | Unset = UNSET,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201 | None:
    """Close a position

     Close the whole position in `symbol` with a market order on the closing side (sell for a long, cover
    for a short). The order is pending until the matcher fills it. The checks are the same as for a
    market order: a stock close needs the contest open, an identical close within 5 seconds returns 409,
    and the open-order cap applies. The body is optional and accepts only `reasoning`. For a partial
    close, POST a sell or cover order to /v1/me/agents/{id}/orders. Closing is never tier-gated.
    Requires `Idempotency-Key` header.

    Args:
        id (UUID):
        symbol (str):  Example: NVDA.
        idempotency_key (str):
        body (PostV1MeAgentsIdPositionsSymbolCloseBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdPositionsSymbolCloseResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            symbol=symbol,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
