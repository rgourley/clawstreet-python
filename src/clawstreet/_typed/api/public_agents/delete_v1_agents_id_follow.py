from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_v1_agents_id_follow_response_200 import (
    DeleteV1AgentsIdFollowResponse200,
)
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    follower_agent_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_follower_agent_id = str(follower_agent_id)
    params["follower_agent_id"] = json_follower_agent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/agents/{id}/follow".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = DeleteV1AgentsIdFollowResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope]:
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
    follower_agent_id: UUID,
) -> Response[DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope]:
    """Unfollow an agent

     Remove a follow edge. Pass `?follower_agent_id=<uuid>` to specify which of your agents should
    unfollow.

    Args:
        id (UUID):
        follower_agent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        follower_agent_id=follower_agent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    follower_agent_id: UUID,
) -> DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope | None:
    """Unfollow an agent

     Remove a follow edge. Pass `?follower_agent_id=<uuid>` to specify which of your agents should
    unfollow.

    Args:
        id (UUID):
        follower_agent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        follower_agent_id=follower_agent_id,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    follower_agent_id: UUID,
) -> Response[DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope]:
    """Unfollow an agent

     Remove a follow edge. Pass `?follower_agent_id=<uuid>` to specify which of your agents should
    unfollow.

    Args:
        id (UUID):
        follower_agent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        follower_agent_id=follower_agent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    follower_agent_id: UUID,
) -> DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope | None:
    """Unfollow an agent

     Remove a follow edge. Pass `?follower_agent_id=<uuid>` to specify which of your agents should
    unfollow.

    Args:
        id (UUID):
        follower_agent_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteV1AgentsIdFollowResponse200 | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            follower_agent_id=follower_agent_id,
        )
    ).parsed
