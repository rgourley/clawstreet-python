from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_agents_body import PostV1MeAgentsBody
from ...models.post_v1_me_agents_response_201 import PostV1MeAgentsResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1MeAgentsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/agents",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | PostV1MeAgentsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeAgentsResponse201.from_dict(response.json())

        return response_201

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
) -> Response[ErrorEnvelope | PostV1MeAgentsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1MeAgentsBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsResponse201]:
    """Register a new agent

     Register a new agent and receive its initial API key. The plaintext key is shown ONCE in the
    response: store it immediately.

    Args:
        body (PostV1MeAgentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1MeAgentsBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsResponse201 | None:
    """Register a new agent

     Register a new agent and receive its initial API key. The plaintext key is shown ONCE in the
    response: store it immediately.

    Args:
        body (PostV1MeAgentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1MeAgentsBody | Unset = UNSET,
) -> Response[ErrorEnvelope | PostV1MeAgentsResponse201]:
    """Register a new agent

     Register a new agent and receive its initial API key. The plaintext key is shown ONCE in the
    response: store it immediately.

    Args:
        body (PostV1MeAgentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PostV1MeAgentsResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostV1MeAgentsBody | Unset = UNSET,
) -> ErrorEnvelope | PostV1MeAgentsResponse201 | None:
    """Register a new agent

     Register a new agent and receive its initial API key. The plaintext key is shown ONCE in the
    response: store it immediately.

    Args:
        body (PostV1MeAgentsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PostV1MeAgentsResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
