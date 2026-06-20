from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_skill_changelog_response_200 import GetV1SkillChangelogResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/skill/changelog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetV1SkillChangelogResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1SkillChangelogResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetV1SkillChangelogResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
) -> Response[GetV1SkillChangelogResponse200]:
    """SKILL.md changelog

     Returns the changelog entries for SKILL.md. Accepts `?since=<version>` to filter to entries newer
    than a given semver.

    Args:
        since (str | Unset):  Example: 1.20.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1SkillChangelogResponse200]
    """

    kwargs = _get_kwargs(
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
) -> GetV1SkillChangelogResponse200 | None:
    """SKILL.md changelog

     Returns the changelog entries for SKILL.md. Accepts `?since=<version>` to filter to entries newer
    than a given semver.

    Args:
        since (str | Unset):  Example: 1.20.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1SkillChangelogResponse200
    """

    return sync_detailed(
        client=client,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
) -> Response[GetV1SkillChangelogResponse200]:
    """SKILL.md changelog

     Returns the changelog entries for SKILL.md. Accepts `?since=<version>` to filter to entries newer
    than a given semver.

    Args:
        since (str | Unset):  Example: 1.20.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1SkillChangelogResponse200]
    """

    kwargs = _get_kwargs(
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    since: str | Unset = UNSET,
) -> GetV1SkillChangelogResponse200 | None:
    """SKILL.md changelog

     Returns the changelog entries for SKILL.md. Accepts `?since=<version>` to filter to entries newer
    than a given semver.

    Args:
        since (str | Unset):  Example: 1.20.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1SkillChangelogResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
        )
    ).parsed
