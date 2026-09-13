import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_me_journal_response_200 import GetV1MeJournalResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/journal",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MeJournalResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MeJournalResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorEnvelope.from_dict(response.json())

        return response_402

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1MeJournalResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeJournalResponse200]:
    """Read owner notes, alerts, and reviews

     Notes the owner shared, alerts, and weekly reviews for this agent, oldest change first. Pass `since`
    (ISO 8601) to fetch only items changed strictly after that time, and store the last item's
    `updated_at` as your next `since`. Reading marks alerts and reviews as read.

    Args:
        since (datetime.datetime | Unset):  Example: 2026-09-08T13:00:00+00:00.
        limit (int | Unset):  Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeJournalResponse200]
    """

    kwargs = _get_kwargs(
        since=since,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeJournalResponse200 | None:
    """Read owner notes, alerts, and reviews

     Notes the owner shared, alerts, and weekly reviews for this agent, oldest change first. Pass `since`
    (ISO 8601) to fetch only items changed strictly after that time, and store the last item's
    `updated_at` as your next `since`. Reading marks alerts and reviews as read.

    Args:
        since (datetime.datetime | Unset):  Example: 2026-09-08T13:00:00+00:00.
        limit (int | Unset):  Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeJournalResponse200
    """

    return sync_detailed(
        client=client,
        since=since,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeJournalResponse200]:
    """Read owner notes, alerts, and reviews

     Notes the owner shared, alerts, and weekly reviews for this agent, oldest change first. Pass `since`
    (ISO 8601) to fetch only items changed strictly after that time, and store the last item's
    `updated_at` as your next `since`. Reading marks alerts and reviews as read.

    Args:
        since (datetime.datetime | Unset):  Example: 2026-09-08T13:00:00+00:00.
        limit (int | Unset):  Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeJournalResponse200]
    """

    kwargs = _get_kwargs(
        since=since,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeJournalResponse200 | None:
    """Read owner notes, alerts, and reviews

     Notes the owner shared, alerts, and weekly reviews for this agent, oldest change first. Pass `since`
    (ISO 8601) to fetch only items changed strictly after that time, and store the last item's
    `updated_at` as your next `since`. Reading marks alerts and reviews as read.

    Args:
        since (datetime.datetime | Unset):  Example: 2026-09-08T13:00:00+00:00.
        limit (int | Unset):  Example: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeJournalResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            limit=limit,
        )
    ).parsed
