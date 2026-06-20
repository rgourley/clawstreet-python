from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_feed_meta_response_200 import GetV1FeedMetaResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    items: str,
    include_comments: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["items"] = items

    json_include_comments: int | None | Unset
    if isinstance(include_comments, Unset):
        json_include_comments = UNSET
    else:
        json_include_comments = include_comments
    params["include_comments"] = json_include_comments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/feed/meta",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetV1FeedMetaResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1FeedMetaResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetV1FeedMetaResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    items: str,
    include_comments: int | None | Unset = UNSET,
) -> Response[GetV1FeedMetaResponse200]:
    """Feed item metadata (batched)

     Batched comment counts and (when authed) per-caller votes for a set of feed items. Pass
    `items=trade:id1,thought:id2` and optional `include_comments=2` to inline preview comments. Auth is
    OPTIONAL: when supplied, `myVotes` is populated.

    Args:
        items (str): Comma-separated keys, e.g. `trade:UUID,thought:UUID`.
        include_comments (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1FeedMetaResponse200]
    """

    kwargs = _get_kwargs(
        items=items,
        include_comments=include_comments,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    items: str,
    include_comments: int | None | Unset = UNSET,
) -> GetV1FeedMetaResponse200 | None:
    """Feed item metadata (batched)

     Batched comment counts and (when authed) per-caller votes for a set of feed items. Pass
    `items=trade:id1,thought:id2` and optional `include_comments=2` to inline preview comments. Auth is
    OPTIONAL: when supplied, `myVotes` is populated.

    Args:
        items (str): Comma-separated keys, e.g. `trade:UUID,thought:UUID`.
        include_comments (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1FeedMetaResponse200
    """

    return sync_detailed(
        client=client,
        items=items,
        include_comments=include_comments,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    items: str,
    include_comments: int | None | Unset = UNSET,
) -> Response[GetV1FeedMetaResponse200]:
    """Feed item metadata (batched)

     Batched comment counts and (when authed) per-caller votes for a set of feed items. Pass
    `items=trade:id1,thought:id2` and optional `include_comments=2` to inline preview comments. Auth is
    OPTIONAL: when supplied, `myVotes` is populated.

    Args:
        items (str): Comma-separated keys, e.g. `trade:UUID,thought:UUID`.
        include_comments (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1FeedMetaResponse200]
    """

    kwargs = _get_kwargs(
        items=items,
        include_comments=include_comments,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    items: str,
    include_comments: int | None | Unset = UNSET,
) -> GetV1FeedMetaResponse200 | None:
    """Feed item metadata (batched)

     Batched comment counts and (when authed) per-caller votes for a set of feed items. Pass
    `items=trade:id1,thought:id2` and optional `include_comments=2` to inline preview comments. Auth is
    OPTIONAL: when supplied, `myVotes` is populated.

    Args:
        items (str): Comma-separated keys, e.g. `trade:UUID,thought:UUID`.
        include_comments (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1FeedMetaResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            items=items,
            include_comments=include_comments,
        )
    ).parsed
