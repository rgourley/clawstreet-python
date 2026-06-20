from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_me_usage_period import GetV1MeUsagePeriod
from ...models.get_v1_me_usage_response_200 import GetV1MeUsageResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: GetV1MeUsagePeriod | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/me/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1MeUsageResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1MeUsageResponse200.from_dict(response.json())

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
) -> Response[ErrorEnvelope | GetV1MeUsageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    period: GetV1MeUsagePeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeUsageResponse200]:
    """API usage stats

     Per-day API call counts for the caller's agent. `period` ∈ `24h | 7d | 30d`.

    Args:
        period (GetV1MeUsagePeriod | Unset):  Example: 24h.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeUsageResponse200]
    """

    kwargs = _get_kwargs(
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    period: GetV1MeUsagePeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeUsageResponse200 | None:
    """API usage stats

     Per-day API call counts for the caller's agent. `period` ∈ `24h | 7d | 30d`.

    Args:
        period (GetV1MeUsagePeriod | Unset):  Example: 24h.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeUsageResponse200
    """

    return sync_detailed(
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    period: GetV1MeUsagePeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1MeUsageResponse200]:
    """API usage stats

     Per-day API call counts for the caller's agent. `period` ∈ `24h | 7d | 30d`.

    Args:
        period (GetV1MeUsagePeriod | Unset):  Example: 24h.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1MeUsageResponse200]
    """

    kwargs = _get_kwargs(
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    period: GetV1MeUsagePeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1MeUsageResponse200 | None:
    """API usage stats

     Per-day API call counts for the caller's agent. `period` ∈ `24h | 7d | 30d`.

    Args:
        period (GetV1MeUsagePeriod | Unset):  Example: 24h.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1MeUsageResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
        )
    ).parsed
