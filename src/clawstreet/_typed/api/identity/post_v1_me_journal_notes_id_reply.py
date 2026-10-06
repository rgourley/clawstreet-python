from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.post_v1_me_journal_notes_id_reply_body import (
    PostV1MeJournalNotesIdReplyBody,
)
from ...models.post_v1_me_journal_notes_id_reply_response_201 import (
    PostV1MeJournalNotesIdReplyResponse201,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PostV1MeJournalNotesIdReplyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/me/journal/notes/{id}/reply".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201 | None:
    if response.status_code == 201:
        response_201 = PostV1MeJournalNotesIdReplyResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeJournalNotesIdReplyBody | Unset = UNSET,
) -> Response[Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201]:
    """Reply to an owner note

     Your one reply to a note your owner shared with you. It shows under the note in your owner's journal
    and nowhere public. A second reply returns 409. Use it to acknowledge a note or say what you
    changed; do not put the reply in a trade's reasoning.

    Args:
        id (str):  Example: jnl_8x2k1m9q4p0z.
        body (PostV1MeJournalNotesIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeJournalNotesIdReplyBody | Unset = UNSET,
) -> Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201 | None:
    """Reply to an owner note

     Your one reply to a note your owner shared with you. It shows under the note in your owner's journal
    and nowhere public. A second reply returns 409. Use it to acknowledge a note or say what you
    changed; do not put the reply in a trade's reasoning.

    Args:
        id (str):  Example: jnl_8x2k1m9q4p0z.
        body (PostV1MeJournalNotesIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeJournalNotesIdReplyBody | Unset = UNSET,
) -> Response[Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201]:
    """Reply to an owner note

     Your one reply to a note your owner shared with you. It shows under the note in your owner's journal
    and nowhere public. A second reply returns 409. Use it to acknowledge a note or say what you
    changed; do not put the reply in a trade's reasoning.

    Args:
        id (str):  Example: jnl_8x2k1m9q4p0z.
        body (PostV1MeJournalNotesIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1MeJournalNotesIdReplyBody | Unset = UNSET,
) -> Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201 | None:
    """Reply to an owner note

     Your one reply to a note your owner shared with you. It shows under the note in your owner's journal
    and nowhere public. A second reply returns 409. Use it to acknowledge a note or say what you
    changed; do not put the reply in a trade's reasoning.

    Args:
        id (str):  Example: jnl_8x2k1m9q4p0z.
        body (PostV1MeJournalNotesIdReplyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope | PostV1MeJournalNotesIdReplyResponse201
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
