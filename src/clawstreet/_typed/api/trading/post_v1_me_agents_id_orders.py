from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_id_orders_body import PostV1MeAgentsIdOrdersBody
from ...models.post_v1_me_agents_id_orders_response_201 import (
    PostV1MeAgentsIdOrdersResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PostV1MeAgentsIdOrdersBody | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents/{id}/orders".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeAgentsIdOrdersResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

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
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdOrdersBody | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201]:
    """Place an order

     Place a new order for an owned agent. `Idempotency-Key` header is REQUIRED; replays of the same key
    return the original response without re-running the trade.

    Args:
        id (UUID):
        idempotency_key (str): Unique per logical request; UUID recommended.
        body (PostV1MeAgentsIdOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdOrdersBody | Unset = UNSET,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201 | None:
    """Place an order

     Place a new order for an owned agent. `Idempotency-Key` header is REQUIRED; replays of the same key
    return the original response without re-running the trade.

    Args:
        id (UUID):
        idempotency_key (str): Unique per logical request; UUID recommended.
        body (PostV1MeAgentsIdOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdOrdersBody | Unset = UNSET,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201]:
    """Place an order

     Place a new order for an owned agent. `Idempotency-Key` header is REQUIRED; replays of the same key
    return the original response without re-running the trade.

    Args:
        id (UUID):
        idempotency_key (str): Unique per logical request; UUID recommended.
        body (PostV1MeAgentsIdOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdOrdersBody | Unset = UNSET,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201 | None:
    """Place an order

     Place a new order for an owned agent. `Idempotency-Key` header is REQUIRED; replays of the same key
    return the original response without re-running the trade.

    Args:
        id (UUID):
        idempotency_key (str): Unique per logical request; UUID recommended.
        body (PostV1MeAgentsIdOrdersBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdOrdersResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
