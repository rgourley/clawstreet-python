from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_earnings_upcoming_response_200 import (
    GetV1EarningsUpcomingResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/earnings/upcoming",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1EarningsUpcomingResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1EarningsUpcomingResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GetV1EarningsUpcomingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1EarningsUpcomingResponse200]:
    """Earnings calendar

     Earnings reports across the market for a date window, oldest first. With no parameters the window is
    today to 7 days ahead. Set `from` to a past date to get recent reports with actual EPS, actual
    revenue and surprise percentages, for example `?from=2026-09-28&to=2026-10-05`. The window can be at
    most 30 days.

    Args:
        from_ (str | Unset): First date of the window, YYYY-MM-DD. Can be in the past. Defaults to
            today (UTC). Example: 2026-09-28.
        to (str | Unset): Last date of the window, YYYY-MM-DD, inclusive. Defaults to `from` plus
            `days`. At most 30 days after `from`. Example: 2026-10-05.
        days (int | Unset): Window length in days when `to` is not set, 1 to 30. Defaults to 7.
            Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1EarningsUpcomingResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1EarningsUpcomingResponse200 | None:
    """Earnings calendar

     Earnings reports across the market for a date window, oldest first. With no parameters the window is
    today to 7 days ahead. Set `from` to a past date to get recent reports with actual EPS, actual
    revenue and surprise percentages, for example `?from=2026-09-28&to=2026-10-05`. The window can be at
    most 30 days.

    Args:
        from_ (str | Unset): First date of the window, YYYY-MM-DD. Can be in the past. Defaults to
            today (UTC). Example: 2026-09-28.
        to (str | Unset): Last date of the window, YYYY-MM-DD, inclusive. Defaults to `from` plus
            `days`. At most 30 days after `from`. Example: 2026-10-05.
        days (int | Unset): Window length in days when `to` is not set, 1 to 30. Defaults to 7.
            Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1EarningsUpcomingResponse200
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1EarningsUpcomingResponse200]:
    """Earnings calendar

     Earnings reports across the market for a date window, oldest first. With no parameters the window is
    today to 7 days ahead. Set `from` to a past date to get recent reports with actual EPS, actual
    revenue and surprise percentages, for example `?from=2026-09-28&to=2026-10-05`. The window can be at
    most 30 days.

    Args:
        from_ (str | Unset): First date of the window, YYYY-MM-DD. Can be in the past. Defaults to
            today (UTC). Example: 2026-09-28.
        to (str | Unset): Last date of the window, YYYY-MM-DD, inclusive. Defaults to `from` plus
            `days`. At most 30 days after `from`. Example: 2026-10-05.
        days (int | Unset): Window length in days when `to` is not set, 1 to 30. Defaults to 7.
            Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1EarningsUpcomingResponse200]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    days: int | Unset = UNSET,
) -> ErrorEnvelope | GetV1EarningsUpcomingResponse200 | None:
    """Earnings calendar

     Earnings reports across the market for a date window, oldest first. With no parameters the window is
    today to 7 days ahead. Set `from` to a past date to get recent reports with actual EPS, actual
    revenue and surprise percentages, for example `?from=2026-09-28&to=2026-10-05`. The window can be at
    most 30 days.

    Args:
        from_ (str | Unset): First date of the window, YYYY-MM-DD. Can be in the past. Defaults to
            today (UTC). Example: 2026-09-28.
        to (str | Unset): Last date of the window, YYYY-MM-DD, inclusive. Defaults to `from` plus
            `days`. At most 30 days after `from`. Example: 2026-10-05.
        days (int | Unset): Window length in days when `to` is not set, 1 to 30. Defaults to 7.
            Values outside the range are clamped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1EarningsUpcomingResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            days=days,
        )
    ).parsed
