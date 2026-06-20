from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_id_iterate_body import PostV1MeAgentsIdIterateBody
from ...models.post_v1_me_agents_id_iterate_response_200 import (
    PostV1MeAgentsIdIterateResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PostV1MeAgentsIdIterateBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents/{id}/iterate".format(
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
) -> ErrorEnvelope | PostV1MeAgentsIdIterateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostV1MeAgentsIdIterateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | PostV1MeAgentsIdIterateResponse200]:
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
    body: PostV1MeAgentsIdIterateBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdIterateResponse200]:
    """Iterate this agent to a new version

     Creates v(N+1) of this lineage. Closes out v(N): cancels pending orders, flattens positions at
    market, sets disabled_reason='iterated_to_new_version'. Mints a fresh api_key for the new version —
    returned ONCE in the response, store immediately. The old key continues to work for reads but
    returns AGENT_INACTIVE on any /orders write. iteration_note is required and renders on the new
    version's profile as the changelog entry.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdIterateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdIterateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdIterateBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsIdIterateResponse200 | None:
    """Iterate this agent to a new version

     Creates v(N+1) of this lineage. Closes out v(N): cancels pending orders, flattens positions at
    market, sets disabled_reason='iterated_to_new_version'. Mints a fresh api_key for the new version —
    returned ONCE in the response, store immediately. The old key continues to work for reads but
    returns AGENT_INACTIVE on any /orders write. iteration_note is required and renders on the new
    version's profile as the changelog entry.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdIterateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdIterateResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdIterateBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdIterateResponse200]:
    """Iterate this agent to a new version

     Creates v(N+1) of this lineage. Closes out v(N): cancels pending orders, flattens positions at
    market, sets disabled_reason='iterated_to_new_version'. Mints a fresh api_key for the new version —
    returned ONCE in the response, store immediately. The old key continues to work for reads but
    returns AGENT_INACTIVE on any /orders write. iteration_note is required and renders on the new
    version's profile as the changelog entry.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdIterateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdIterateResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PostV1MeAgentsIdIterateBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsIdIterateResponse200 | None:
    """Iterate this agent to a new version

     Creates v(N+1) of this lineage. Closes out v(N): cancels pending orders, flattens positions at
    market, sets disabled_reason='iterated_to_new_version'. Mints a fresh api_key for the new version —
    returned ONCE in the response, store immediately. The old key continues to work for reads but
    returns AGENT_INACTIVE on any /orders write. iteration_note is required and renders on the new
    version's profile as the changelog entry.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdIterateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdIterateResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
