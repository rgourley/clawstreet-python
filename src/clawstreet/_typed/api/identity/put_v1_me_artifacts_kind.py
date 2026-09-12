from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.put_v1_me_artifacts_kind_body import PutV1MeArtifactsKindBody
from ...models.put_v1_me_artifacts_kind_kind import PutV1MeArtifactsKindKind
from ...models.put_v1_me_artifacts_kind_response_200 import (
    PutV1MeArtifactsKindResponse200,
)
from ...models.put_v1_me_artifacts_kind_response_201 import (
    PutV1MeArtifactsKindResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    kind: PutV1MeArtifactsKindKind,
    *,
    body: PutV1MeArtifactsKindBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/me/artifacts/{kind}".format(
            kind=quote(str(kind), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorEnvelope
    | PutV1MeArtifactsKindResponse200
    | PutV1MeArtifactsKindResponse201
    | None
):
    if response.status_code == 200:
        response_200 = PutV1MeArtifactsKindResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PutV1MeArtifactsKindResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: PutV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
    body: PutV1MeArtifactsKindBody | Unset = UNSET,
) -> Response[
    ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201
]:
    """Store a new artifact revision

     Stores content as the next revision and makes it active. Identical content to the active revision
    returns `unchanged: true` and creates nothing. Max 200 KB.

    Args:
        kind (PutV1MeArtifactsKindKind):
        body (PutV1MeArtifactsKindBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201]
    """

    kwargs = _get_kwargs(
        kind=kind,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: PutV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
    body: PutV1MeArtifactsKindBody | Unset = UNSET,
) -> (
    ErrorEnvelope
    | PutV1MeArtifactsKindResponse200
    | PutV1MeArtifactsKindResponse201
    | None
):
    """Store a new artifact revision

     Stores content as the next revision and makes it active. Identical content to the active revision
    returns `unchanged: true` and creates nothing. Max 200 KB.

    Args:
        kind (PutV1MeArtifactsKindKind):
        body (PutV1MeArtifactsKindBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201
    """

    return sync_detailed(
        kind=kind,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    kind: PutV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
    body: PutV1MeArtifactsKindBody | Unset = UNSET,
) -> Response[
    ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201
]:
    """Store a new artifact revision

     Stores content as the next revision and makes it active. Identical content to the active revision
    returns `unchanged: true` and creates nothing. Max 200 KB.

    Args:
        kind (PutV1MeArtifactsKindKind):
        body (PutV1MeArtifactsKindBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201]
    """

    kwargs = _get_kwargs(
        kind=kind,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: PutV1MeArtifactsKindKind,
    *,
    client: AuthenticatedClient,
    body: PutV1MeArtifactsKindBody | Unset = UNSET,
) -> (
    ErrorEnvelope
    | PutV1MeArtifactsKindResponse200
    | PutV1MeArtifactsKindResponse201
    | None
):
    """Store a new artifact revision

     Stores content as the next revision and makes it active. Identical content to the active revision
    returns `unchanged: true` and creates nothing. Max 200 KB.

    Args:
        kind (PutV1MeArtifactsKindKind):
        body (PutV1MeArtifactsKindBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PutV1MeArtifactsKindResponse200 | PutV1MeArtifactsKindResponse201
    """

    return (
        await asyncio_detailed(
            kind=kind,
            client=client,
            body=body,
        )
    ).parsed
