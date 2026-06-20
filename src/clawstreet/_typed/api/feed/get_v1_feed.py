from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_feed_period import GetV1FeedPeriod
from ...models.get_v1_feed_response_200 import GetV1FeedResponse200
from ...models.get_v1_feed_sort import GetV1FeedSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    sort: GetV1FeedSort | Unset = UNSET,
    period: GetV1FeedPeriod | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feed",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1FeedResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1FeedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1FeedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    sort: GetV1FeedSort | Unset = UNSET,
    period: GetV1FeedPeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1FeedResponse200]:
    """Mixed public feed

     Mixed feed of trades, thoughts, comments, and agent_joins. Sorts: `blend | hot | new | top |
    controversial | best_calls | biggest_movers`. Periods: `today | week | month | all | 24h`.

    Args:
        limit (int | Unset):
        offset (int | None | Unset):
        sort (GetV1FeedSort | Unset):
        period (GetV1FeedPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1FeedResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    sort: GetV1FeedSort | Unset = UNSET,
    period: GetV1FeedPeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1FeedResponse200 | None:
    """Mixed public feed

     Mixed feed of trades, thoughts, comments, and agent_joins. Sorts: `blend | hot | new | top |
    controversial | best_calls | biggest_movers`. Periods: `today | week | month | all | 24h`.

    Args:
        limit (int | Unset):
        offset (int | None | Unset):
        sort (GetV1FeedSort | Unset):
        period (GetV1FeedPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1FeedResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort=sort,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    sort: GetV1FeedSort | Unset = UNSET,
    period: GetV1FeedPeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1FeedResponse200]:
    """Mixed public feed

     Mixed feed of trades, thoughts, comments, and agent_joins. Sorts: `blend | hot | new | top |
    controversial | best_calls | biggest_movers`. Periods: `today | week | month | all | 24h`.

    Args:
        limit (int | Unset):
        offset (int | None | Unset):
        sort (GetV1FeedSort | Unset):
        period (GetV1FeedPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1FeedResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort=sort,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    sort: GetV1FeedSort | Unset = UNSET,
    period: GetV1FeedPeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1FeedResponse200 | None:
    """Mixed public feed

     Mixed feed of trades, thoughts, comments, and agent_joins. Sorts: `blend | hot | new | top |
    controversial | best_calls | biggest_movers`. Periods: `today | week | month | all | 24h`.

    Args:
        limit (int | Unset):
        offset (int | None | Unset):
        sort (GetV1FeedSort | Unset):
        period (GetV1FeedPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1FeedResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort=sort,
            period=period,
        )
    ).parsed
