from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_movers_direction import GetV1MoversDirection
from ...models.get_v1_movers_response_200 import GetV1MoversResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    direction: GetV1MoversDirection | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/movers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MoversResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MoversResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1MoversResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    direction: GetV1MoversDirection | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MoversResponse200]:
    """Top movers

     Top gainers/losers by percent change. `?direction=up` returns gainers only, `?direction=down`
    returns losers only, omitted returns both.

    Args:
        direction (GetV1MoversDirection | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MoversResponse200]
    """

    kwargs = _get_kwargs(
        direction=direction,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    direction: GetV1MoversDirection | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MoversResponse200 | None:
    """Top movers

     Top gainers/losers by percent change. `?direction=up` returns gainers only, `?direction=down`
    returns losers only, omitted returns both.

    Args:
        direction (GetV1MoversDirection | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MoversResponse200
    """

    return sync_detailed(
        client=client,
        direction=direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    direction: GetV1MoversDirection | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MoversResponse200]:
    """Top movers

     Top gainers/losers by percent change. `?direction=up` returns gainers only, `?direction=down`
    returns losers only, omitted returns both.

    Args:
        direction (GetV1MoversDirection | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MoversResponse200]
    """

    kwargs = _get_kwargs(
        direction=direction,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    direction: GetV1MoversDirection | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MoversResponse200 | None:
    """Top movers

     Top gainers/losers by percent change. `?direction=up` returns gainers only, `?direction=down`
    returns losers only, omitted returns both.

    Args:
        direction (GetV1MoversDirection | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MoversResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            direction=direction,
            limit=limit,
        )
    ).parsed
