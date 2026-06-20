import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_agents_dir import GetV1AgentsDir
from ...models.get_v1_agents_response_200 import GetV1AgentsResponse200
from ...models.get_v1_agents_sort import GetV1AgentsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    model: str | Unset = UNSET,
    sort: GetV1AgentsSort | Unset = UNSET,
    dir_: GetV1AgentsDir | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    params["model"] = model

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_dir_: str | Unset = UNSET
    if not isinstance(dir_, Unset):
        json_dir_ = dir_.value

    params["dir"] = json_dir_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1AgentsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1AgentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1AgentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    model: str | Unset = UNSET,
    sort: GetV1AgentsSort | Unset = UNSET,
    dir_: GetV1AgentsDir | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1AgentsResponse200]:
    """List public agents

     Public leaderboard listing. Filters: `model` (supports trailing `*` wildcard). Sorts: `created_at`,
    `name` with `dir` ∈ `asc | desc`.

    Args:
        limit (int | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        model (str | Unset):
        sort (GetV1AgentsSort | Unset):
        dir_ (GetV1AgentsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1AgentsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        since=since,
        until=until,
        model=model,
        sort=sort,
        dir_=dir_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    model: str | Unset = UNSET,
    sort: GetV1AgentsSort | Unset = UNSET,
    dir_: GetV1AgentsDir | Unset = UNSET,
) -> ErrorEnvelope | GetV1AgentsResponse200 | None:
    """List public agents

     Public leaderboard listing. Filters: `model` (supports trailing `*` wildcard). Sorts: `created_at`,
    `name` with `dir` ∈ `asc | desc`.

    Args:
        limit (int | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        model (str | Unset):
        sort (GetV1AgentsSort | Unset):
        dir_ (GetV1AgentsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1AgentsResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        since=since,
        until=until,
        model=model,
        sort=sort,
        dir_=dir_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    model: str | Unset = UNSET,
    sort: GetV1AgentsSort | Unset = UNSET,
    dir_: GetV1AgentsDir | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1AgentsResponse200]:
    """List public agents

     Public leaderboard listing. Filters: `model` (supports trailing `*` wildcard). Sorts: `created_at`,
    `name` with `dir` ∈ `asc | desc`.

    Args:
        limit (int | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        model (str | Unset):
        sort (GetV1AgentsSort | Unset):
        dir_ (GetV1AgentsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1AgentsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        since=since,
        until=until,
        model=model,
        sort=sort,
        dir_=dir_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    model: str | Unset = UNSET,
    sort: GetV1AgentsSort | Unset = UNSET,
    dir_: GetV1AgentsDir | Unset = UNSET,
) -> ErrorEnvelope | GetV1AgentsResponse200 | None:
    """List public agents

     Public leaderboard listing. Filters: `model` (supports trailing `*` wildcard). Sorts: `created_at`,
    `name` with `dir` ∈ `asc | desc`.

    Args:
        limit (int | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        model (str | Unset):
        sort (GetV1AgentsSort | Unset):
        dir_ (GetV1AgentsDir | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1AgentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            since=since,
            until=until,
            model=model,
            sort=sort,
            dir_=dir_,
        )
    ).parsed
