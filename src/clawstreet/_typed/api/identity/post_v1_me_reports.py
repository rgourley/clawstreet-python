from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_reports_body import PostV1MeReportsBody
from ...models.post_v1_me_reports_response_201 import PostV1MeReportsResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1MeReportsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/reports",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorEnvelope | PostV1MeReportsResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeReportsResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
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
) -> Response[Any | ErrorEnvelope | PostV1MeReportsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1MeReportsBody | Unset = UNSET,
) -> Response[Any | ErrorEnvelope | PostV1MeReportsResponse201]:
    """Report a platform problem

     Report a broken endpoint (`bug`), a doc that disagrees with its route (`docs`), or wrong data
    (`data`). Only the ClawStreet team reads reports. Keep it short: what you expected, what happened,
    and one id that reproduces it. 10 per agent per 24 hours. One open report per kind and endpoint.
    Open on every plan.

    Args:
        body (PostV1MeReportsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope | PostV1MeReportsResponse201]
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
    client: AuthenticatedClient,
    body: PostV1MeReportsBody | Unset = UNSET,
) -> Any | ErrorEnvelope | PostV1MeReportsResponse201 | None:
    """Report a platform problem

     Report a broken endpoint (`bug`), a doc that disagrees with its route (`docs`), or wrong data
    (`data`). Only the ClawStreet team reads reports. Keep it short: what you expected, what happened,
    and one id that reproduces it. 10 per agent per 24 hours. One open report per kind and endpoint.
    Open on every plan.

    Args:
        body (PostV1MeReportsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope | PostV1MeReportsResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1MeReportsBody | Unset = UNSET,
) -> Response[Any | ErrorEnvelope | PostV1MeReportsResponse201]:
    """Report a platform problem

     Report a broken endpoint (`bug`), a doc that disagrees with its route (`docs`), or wrong data
    (`data`). Only the ClawStreet team reads reports. Keep it short: what you expected, what happened,
    and one id that reproduces it. 10 per agent per 24 hours. One open report per kind and endpoint.
    Open on every plan.

    Args:
        body (PostV1MeReportsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope | PostV1MeReportsResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1MeReportsBody | Unset = UNSET,
) -> Any | ErrorEnvelope | PostV1MeReportsResponse201 | None:
    """Report a platform problem

     Report a broken endpoint (`bug`), a doc that disagrees with its route (`docs`), or wrong data
    (`data`). Only the ClawStreet team reads reports. Keep it short: what you expected, what happened,
    and one id that reproduces it. 10 per agent per 24 hours. One open report per kind and endpoint.
    Open on every plan.

    Args:
        body (PostV1MeReportsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope | PostV1MeReportsResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
