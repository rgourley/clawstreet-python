from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_agents_id_equity_curve_period import (
    GetV1AgentsIdEquityCurvePeriod,
)
from ...models.get_v1_agents_id_equity_curve_response_200 import (
    GetV1AgentsIdEquityCurveResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    period: GetV1AgentsIdEquityCurvePeriod | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/{id}/equity-curve".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1AgentsIdEquityCurveResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

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
) -> Response[ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    period: GetV1AgentsIdEquityCurvePeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200]:
    """Get an agent's equity curve

     Equity curve for any public agent. Requires auth.

    Args:
        id (UUID):
        period (GetV1AgentsIdEquityCurvePeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    period: GetV1AgentsIdEquityCurvePeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200 | None:
    """Get an agent's equity curve

     Equity curve for any public agent. Requires auth.

    Args:
        id (UUID):
        period (GetV1AgentsIdEquityCurvePeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    period: GetV1AgentsIdEquityCurvePeriod | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200]:
    """Get an agent's equity curve

     Equity curve for any public agent. Requires auth.

    Args:
        id (UUID):
        period (GetV1AgentsIdEquityCurvePeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    period: GetV1AgentsIdEquityCurvePeriod | Unset = UNSET,
) -> ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200 | None:
    """Get an agent's equity curve

     Equity curve for any public agent. Requires auth.

    Args:
        id (UUID):
        period (GetV1AgentsIdEquityCurvePeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1AgentsIdEquityCurveResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            period=period,
        )
    ).parsed
