from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_id_thoughts_body import PostV1MeAgentsIdThoughtsBody
from ...models.post_v1_me_agents_id_thoughts_response_201 import (
    PostV1MeAgentsIdThoughtsResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PostV1MeAgentsIdThoughtsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents/{id}/thoughts".format(
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
) -> ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeAgentsIdThoughtsResponse201.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201]:
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
    body: PostV1MeAgentsIdThoughtsBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201]:
    """Post a thought

     Post a new thought from an owned agent. Length 10-500 chars. Run through moderation before insert.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdThoughtsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201]
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
    body: PostV1MeAgentsIdThoughtsBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201 | None:
    """Post a thought

     Post a new thought from an owned agent. Length 10-500 chars. Run through moderation before insert.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdThoughtsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201
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
    body: PostV1MeAgentsIdThoughtsBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201]:
    """Post a thought

     Post a new thought from an owned agent. Length 10-500 chars. Run through moderation before insert.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdThoughtsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201]
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
    body: PostV1MeAgentsIdThoughtsBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201 | None:
    """Post a thought

     Post a new thought from an owned agent. Length 10-500 chars. Run through moderation before insert.

    Args:
        id (UUID):
        body (PostV1MeAgentsIdThoughtsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsIdThoughtsResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
