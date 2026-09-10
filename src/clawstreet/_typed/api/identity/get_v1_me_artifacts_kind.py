from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_me_artifacts_kind_kind import GetV1MeArtifactsKindKind
from ...models.get_v1_me_artifacts_kind_response_200 import (
    GetV1MeArtifactsKindResponse200,
)
from ...types import Response


def _get_kwargs(
    kind: GetV1MeArtifactsKindKind,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/artifacts/{kind}".format(
            kind=quote(str(kind), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MeArtifactsKindResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MeArtifactsKindResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

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
) -> Response[ErrorEnvelope | GetV1MeArtifactsKindResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: GetV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MeArtifactsKindResponse200]:
    """Get an artifact

     Active version with content, plus the version history without content.

    Args:
        kind (GetV1MeArtifactsKindKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeArtifactsKindResponse200]
    """

    kwargs = _get_kwargs(
        kind=kind,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: GetV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MeArtifactsKindResponse200 | None:
    """Get an artifact

     Active version with content, plus the version history without content.

    Args:
        kind (GetV1MeArtifactsKindKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeArtifactsKindResponse200
    """

    return sync_detailed(
        kind=kind,
        client=client,
    ).parsed


async def asyncio_detailed(
    kind: GetV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | GetV1MeArtifactsKindResponse200]:
    """Get an artifact

     Active version with content, plus the version history without content.

    Args:
        kind (GetV1MeArtifactsKindKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeArtifactsKindResponse200]
    """

    kwargs = _get_kwargs(
        kind=kind,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: GetV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | GetV1MeArtifactsKindResponse200 | None:
    """Get an artifact

     Active version with content, plus the version history without content.

    Args:
        kind (GetV1MeArtifactsKindKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeArtifactsKindResponse200
    """

    return (
        await asyncio_detailed(
            kind=kind,
            client=client,
        )
    ).parsed
