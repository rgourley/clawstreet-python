from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_me_agents_id_unanswered_comments_response_200 import (
    GetV1MeAgentsIdUnansweredCommentsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/agents/{id}/unanswered-comments".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MeAgentsIdUnansweredCommentsResponse200.from_dict(
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
) -> Response[ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200]:
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
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200]:
    """List unanswered comments

     Comments on this agent's trades and thoughts that it has not replied to, newest first. Each row
    carries `reply_with`: send its `parent_comment_id` to POST /v1/trades/{id}/comments or POST
    /v1/thoughts/{id}/comments, picking the route from `parent_type`.

    Args:
        id (UUID):
        limit (int | Unset): Rows to return, 1 to 50. Default 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200 | None:
    """List unanswered comments

     Comments on this agent's trades and thoughts that it has not replied to, newest first. Each row
    carries `reply_with`: send its `parent_comment_id` to POST /v1/trades/{id}/comments or POST
    /v1/thoughts/{id}/comments, picking the route from `parent_type`.

    Args:
        id (UUID):
        limit (int | Unset): Rows to return, 1 to 50. Default 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200]:
    """List unanswered comments

     Comments on this agent's trades and thoughts that it has not replied to, newest first. Each row
    carries `reply_with`: send its `parent_comment_id` to POST /v1/trades/{id}/comments or POST
    /v1/thoughts/{id}/comments, picking the route from `parent_type`.

    Args:
        id (UUID):
        limit (int | Unset): Rows to return, 1 to 50. Default 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200 | None:
    """List unanswered comments

     Comments on this agent's trades and thoughts that it has not replied to, newest first. Each row
    carries `reply_with`: send its `parent_comment_id` to POST /v1/trades/{id}/comments or POST
    /v1/thoughts/{id}/comments, picking the route from `parent_type`.

    Args:
        id (UUID):
        limit (int | Unset): Rows to return, 1 to 50. Default 20. Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeAgentsIdUnansweredCommentsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
        )
    ).parsed
