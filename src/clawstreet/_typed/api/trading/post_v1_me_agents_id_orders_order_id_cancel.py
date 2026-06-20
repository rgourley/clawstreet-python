from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_id_orders_order_id_cancel_response_200 import (
    PostV1MeAgentsIdOrdersOrderIdCancelResponse200,
)
from ...types import Response


def _get_kwargs(
    id: UUID,
    order_id: UUID,
    *,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents/{id}/orders/{order_id}/cancel".format(
            id=quote(str(id), safe=""),
            order_id=quote(str(order_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200 | None:
    if response.status_code == 200:
        response_200 = PostV1MeAgentsIdOrdersOrderIdCancelResponse200.from_dict(
            response.json()
        )

        return response_200

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    order_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200]:
    """Cancel an order

     Cancel an open order. Fails with 409 if already filled, canceled, rejected, or expired. Requires
    `Idempotency-Key` header.

    Args:
        id (UUID):
        order_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    order_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200 | None:
    """Cancel an order

     Cancel an open order. Fails with 409 if already filled, canceled, rejected, or expired. Requires
    `Idempotency-Key` header.

    Args:
        id (UUID):
        order_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200
    """

    return sync_detailed(
        id=id,
        order_id=order_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    order_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200]:
    """Cancel an order

     Cancel an open order. Fails with 409 if already filled, canceled, rejected, or expired. Requires
    `Idempotency-Key` header.

    Args:
        id (UUID):
        order_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        order_id=order_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    order_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200 | None:
    """Cancel an order

     Cancel an open order. Fails with 409 if already filled, canceled, rejected, or expired. Requires
    `Idempotency-Key` header.

    Args:
        id (UUID):
        order_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdOrdersOrderIdCancelResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            order_id=order_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
