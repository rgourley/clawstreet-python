from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_v1_scan_include_leveraged import GetV1ScanIncludeLeveraged
from ...models.get_v1_scan_preset import GetV1ScanPreset
from ...models.get_v1_scan_refresh import GetV1ScanRefresh
from ...models.get_v1_scan_response_200 import GetV1ScanResponse200
from ...models.get_v1_scan_sort import GetV1ScanSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    preset: GetV1ScanPreset | Unset = UNSET,
    sector: str | Unset = UNSET,
    symbols: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: GetV1ScanSort | Unset = UNSET,
    min_rsi: float | None | Unset = UNSET,
    max_rsi: float | None | Unset = UNSET,
    min_bb_position: float | None | Unset = UNSET,
    max_bb_position: float | None | Unset = UNSET,
    min_change_1d: float | None | Unset = UNSET,
    max_change_1d: float | None | Unset = UNSET,
    min_change_5d: float | None | Unset = UNSET,
    max_change_5d: float | None | Unset = UNSET,
    min_change_30d: float | None | Unset = UNSET,
    max_change_30d: float | None | Unset = UNSET,
    min_volume_ratio: float | None | Unset = UNSET,
    min_price: float | None | Unset = UNSET,
    max_price: float | None | Unset = UNSET,
    min_daily_dollar_volume: float | None | Unset = UNSET,
    include_leveraged: GetV1ScanIncludeLeveraged | Unset = UNSET,
    refresh: GetV1ScanRefresh | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_preset: str | Unset = UNSET
    if not isinstance(preset, Unset):
        json_preset = preset.value

    params["preset"] = json_preset

    params["sector"] = sector

    params["symbols"] = symbols

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_min_rsi: float | None | Unset
    if isinstance(min_rsi, Unset):
        json_min_rsi = UNSET
    else:
        json_min_rsi = min_rsi
    params["min_rsi"] = json_min_rsi

    json_max_rsi: float | None | Unset
    if isinstance(max_rsi, Unset):
        json_max_rsi = UNSET
    else:
        json_max_rsi = max_rsi
    params["max_rsi"] = json_max_rsi

    json_min_bb_position: float | None | Unset
    if isinstance(min_bb_position, Unset):
        json_min_bb_position = UNSET
    else:
        json_min_bb_position = min_bb_position
    params["min_bb_position"] = json_min_bb_position

    json_max_bb_position: float | None | Unset
    if isinstance(max_bb_position, Unset):
        json_max_bb_position = UNSET
    else:
        json_max_bb_position = max_bb_position
    params["max_bb_position"] = json_max_bb_position

    json_min_change_1d: float | None | Unset
    if isinstance(min_change_1d, Unset):
        json_min_change_1d = UNSET
    else:
        json_min_change_1d = min_change_1d
    params["min_change_1d"] = json_min_change_1d

    json_max_change_1d: float | None | Unset
    if isinstance(max_change_1d, Unset):
        json_max_change_1d = UNSET
    else:
        json_max_change_1d = max_change_1d
    params["max_change_1d"] = json_max_change_1d

    json_min_change_5d: float | None | Unset
    if isinstance(min_change_5d, Unset):
        json_min_change_5d = UNSET
    else:
        json_min_change_5d = min_change_5d
    params["min_change_5d"] = json_min_change_5d

    json_max_change_5d: float | None | Unset
    if isinstance(max_change_5d, Unset):
        json_max_change_5d = UNSET
    else:
        json_max_change_5d = max_change_5d
    params["max_change_5d"] = json_max_change_5d

    json_min_change_30d: float | None | Unset
    if isinstance(min_change_30d, Unset):
        json_min_change_30d = UNSET
    else:
        json_min_change_30d = min_change_30d
    params["min_change_30d"] = json_min_change_30d

    json_max_change_30d: float | None | Unset
    if isinstance(max_change_30d, Unset):
        json_max_change_30d = UNSET
    else:
        json_max_change_30d = max_change_30d
    params["max_change_30d"] = json_max_change_30d

    json_min_volume_ratio: float | None | Unset
    if isinstance(min_volume_ratio, Unset):
        json_min_volume_ratio = UNSET
    else:
        json_min_volume_ratio = min_volume_ratio
    params["min_volume_ratio"] = json_min_volume_ratio

    json_min_price: float | None | Unset
    if isinstance(min_price, Unset):
        json_min_price = UNSET
    else:
        json_min_price = min_price
    params["min_price"] = json_min_price

    json_max_price: float | None | Unset
    if isinstance(max_price, Unset):
        json_max_price = UNSET
    else:
        json_max_price = max_price
    params["max_price"] = json_max_price

    json_min_daily_dollar_volume: float | None | Unset
    if isinstance(min_daily_dollar_volume, Unset):
        json_min_daily_dollar_volume = UNSET
    else:
        json_min_daily_dollar_volume = min_daily_dollar_volume
    params["min_daily_dollar_volume"] = json_min_daily_dollar_volume

    json_include_leveraged: str | Unset = UNSET
    if not isinstance(include_leveraged, Unset):
        json_include_leveraged = include_leveraged.value

    params["include_leveraged"] = json_include_leveraged

    json_refresh: str | Unset = UNSET
    if not isinstance(refresh, Unset):
        json_refresh = refresh.value

    params["refresh"] = json_refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/scan",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | GetV1ScanResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1ScanResponse200.from_dict(response.json())

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
) -> Response[ErrorEnvelope | GetV1ScanResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    preset: GetV1ScanPreset | Unset = UNSET,
    sector: str | Unset = UNSET,
    symbols: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: GetV1ScanSort | Unset = UNSET,
    min_rsi: float | None | Unset = UNSET,
    max_rsi: float | None | Unset = UNSET,
    min_bb_position: float | None | Unset = UNSET,
    max_bb_position: float | None | Unset = UNSET,
    min_change_1d: float | None | Unset = UNSET,
    max_change_1d: float | None | Unset = UNSET,
    min_change_5d: float | None | Unset = UNSET,
    max_change_5d: float | None | Unset = UNSET,
    min_change_30d: float | None | Unset = UNSET,
    max_change_30d: float | None | Unset = UNSET,
    min_volume_ratio: float | None | Unset = UNSET,
    min_price: float | None | Unset = UNSET,
    max_price: float | None | Unset = UNSET,
    min_daily_dollar_volume: float | None | Unset = UNSET,
    include_leveraged: GetV1ScanIncludeLeveraged | Unset = UNSET,
    refresh: GetV1ScanRefresh | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1ScanResponse200]:
    """Screener / scan

     Screener endpoint with presets, composable filters, and sorts. Inherits all query params from the
    legacy /api/data/scan endpoint. `mode` tells where the rows come from: `precomputed` (daily preset
    snapshot, used while it is less than 6 hours old), `live` (preset computed on request; can take
    20-30s), or `filter` (any min_/max_ param; reads the daily indicator cache). In `precomputed` and
    `filter` modes, price and change fields are from the last completed daily bar: check
    `dataAgeSeconds`. Without `sector` or `symbols`, filter mode reads at most 1000 cache rows, so some
    tradeable symbols can be missing. Row keys mix camelCase (`bbPosition`, `volumeRatio`) and
    snake_case (`change_5d`, `max_1d_drop`). With no preset, indicator, or filter param, the response is
    a help object.

    Args:
        preset (GetV1ScanPreset | Unset):
        sector (str | Unset): Comma-separated sectors. Crypto includes every crypto pair. Example:
            Tech,Crypto.
        symbols (str | Unset): Comma-separated symbols. Overrides sector. Example: AAPL,X:BTCUSD.
        limit (int | Unset): Default 50.
        sort (GetV1ScanSort | Unset):
        min_rsi (float | None | Unset):
        max_rsi (float | None | Unset):
        min_bb_position (float | None | Unset):
        max_bb_position (float | None | Unset):
        min_change_1d (float | None | Unset):
        max_change_1d (float | None | Unset):
        min_change_5d (float | None | Unset):
        max_change_5d (float | None | Unset):
        min_change_30d (float | None | Unset):
        max_change_30d (float | None | Unset):
        min_volume_ratio (float | None | Unset):
        min_price (float | None | Unset):
        max_price (float | None | Unset):
        min_daily_dollar_volume (float | None | Unset):
        include_leveraged (GetV1ScanIncludeLeveraged | Unset):
        refresh (GetV1ScanRefresh | Unset): Bypass the market data cache. Applies to live presets
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1ScanResponse200]
    """

    kwargs = _get_kwargs(
        preset=preset,
        sector=sector,
        symbols=symbols,
        limit=limit,
        sort=sort,
        min_rsi=min_rsi,
        max_rsi=max_rsi,
        min_bb_position=min_bb_position,
        max_bb_position=max_bb_position,
        min_change_1d=min_change_1d,
        max_change_1d=max_change_1d,
        min_change_5d=min_change_5d,
        max_change_5d=max_change_5d,
        min_change_30d=min_change_30d,
        max_change_30d=max_change_30d,
        min_volume_ratio=min_volume_ratio,
        min_price=min_price,
        max_price=max_price,
        min_daily_dollar_volume=min_daily_dollar_volume,
        include_leveraged=include_leveraged,
        refresh=refresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    preset: GetV1ScanPreset | Unset = UNSET,
    sector: str | Unset = UNSET,
    symbols: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: GetV1ScanSort | Unset = UNSET,
    min_rsi: float | None | Unset = UNSET,
    max_rsi: float | None | Unset = UNSET,
    min_bb_position: float | None | Unset = UNSET,
    max_bb_position: float | None | Unset = UNSET,
    min_change_1d: float | None | Unset = UNSET,
    max_change_1d: float | None | Unset = UNSET,
    min_change_5d: float | None | Unset = UNSET,
    max_change_5d: float | None | Unset = UNSET,
    min_change_30d: float | None | Unset = UNSET,
    max_change_30d: float | None | Unset = UNSET,
    min_volume_ratio: float | None | Unset = UNSET,
    min_price: float | None | Unset = UNSET,
    max_price: float | None | Unset = UNSET,
    min_daily_dollar_volume: float | None | Unset = UNSET,
    include_leveraged: GetV1ScanIncludeLeveraged | Unset = UNSET,
    refresh: GetV1ScanRefresh | Unset = UNSET,
) -> ErrorEnvelope | GetV1ScanResponse200 | None:
    """Screener / scan

     Screener endpoint with presets, composable filters, and sorts. Inherits all query params from the
    legacy /api/data/scan endpoint. `mode` tells where the rows come from: `precomputed` (daily preset
    snapshot, used while it is less than 6 hours old), `live` (preset computed on request; can take
    20-30s), or `filter` (any min_/max_ param; reads the daily indicator cache). In `precomputed` and
    `filter` modes, price and change fields are from the last completed daily bar: check
    `dataAgeSeconds`. Without `sector` or `symbols`, filter mode reads at most 1000 cache rows, so some
    tradeable symbols can be missing. Row keys mix camelCase (`bbPosition`, `volumeRatio`) and
    snake_case (`change_5d`, `max_1d_drop`). With no preset, indicator, or filter param, the response is
    a help object.

    Args:
        preset (GetV1ScanPreset | Unset):
        sector (str | Unset): Comma-separated sectors. Crypto includes every crypto pair. Example:
            Tech,Crypto.
        symbols (str | Unset): Comma-separated symbols. Overrides sector. Example: AAPL,X:BTCUSD.
        limit (int | Unset): Default 50.
        sort (GetV1ScanSort | Unset):
        min_rsi (float | None | Unset):
        max_rsi (float | None | Unset):
        min_bb_position (float | None | Unset):
        max_bb_position (float | None | Unset):
        min_change_1d (float | None | Unset):
        max_change_1d (float | None | Unset):
        min_change_5d (float | None | Unset):
        max_change_5d (float | None | Unset):
        min_change_30d (float | None | Unset):
        max_change_30d (float | None | Unset):
        min_volume_ratio (float | None | Unset):
        min_price (float | None | Unset):
        max_price (float | None | Unset):
        min_daily_dollar_volume (float | None | Unset):
        include_leveraged (GetV1ScanIncludeLeveraged | Unset):
        refresh (GetV1ScanRefresh | Unset): Bypass the market data cache. Applies to live presets
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1ScanResponse200
    """

    return sync_detailed(
        client=client,
        preset=preset,
        sector=sector,
        symbols=symbols,
        limit=limit,
        sort=sort,
        min_rsi=min_rsi,
        max_rsi=max_rsi,
        min_bb_position=min_bb_position,
        max_bb_position=max_bb_position,
        min_change_1d=min_change_1d,
        max_change_1d=max_change_1d,
        min_change_5d=min_change_5d,
        max_change_5d=max_change_5d,
        min_change_30d=min_change_30d,
        max_change_30d=max_change_30d,
        min_volume_ratio=min_volume_ratio,
        min_price=min_price,
        max_price=max_price,
        min_daily_dollar_volume=min_daily_dollar_volume,
        include_leveraged=include_leveraged,
        refresh=refresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    preset: GetV1ScanPreset | Unset = UNSET,
    sector: str | Unset = UNSET,
    symbols: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: GetV1ScanSort | Unset = UNSET,
    min_rsi: float | None | Unset = UNSET,
    max_rsi: float | None | Unset = UNSET,
    min_bb_position: float | None | Unset = UNSET,
    max_bb_position: float | None | Unset = UNSET,
    min_change_1d: float | None | Unset = UNSET,
    max_change_1d: float | None | Unset = UNSET,
    min_change_5d: float | None | Unset = UNSET,
    max_change_5d: float | None | Unset = UNSET,
    min_change_30d: float | None | Unset = UNSET,
    max_change_30d: float | None | Unset = UNSET,
    min_volume_ratio: float | None | Unset = UNSET,
    min_price: float | None | Unset = UNSET,
    max_price: float | None | Unset = UNSET,
    min_daily_dollar_volume: float | None | Unset = UNSET,
    include_leveraged: GetV1ScanIncludeLeveraged | Unset = UNSET,
    refresh: GetV1ScanRefresh | Unset = UNSET,
) -> Response[ErrorEnvelope | GetV1ScanResponse200]:
    """Screener / scan

     Screener endpoint with presets, composable filters, and sorts. Inherits all query params from the
    legacy /api/data/scan endpoint. `mode` tells where the rows come from: `precomputed` (daily preset
    snapshot, used while it is less than 6 hours old), `live` (preset computed on request; can take
    20-30s), or `filter` (any min_/max_ param; reads the daily indicator cache). In `precomputed` and
    `filter` modes, price and change fields are from the last completed daily bar: check
    `dataAgeSeconds`. Without `sector` or `symbols`, filter mode reads at most 1000 cache rows, so some
    tradeable symbols can be missing. Row keys mix camelCase (`bbPosition`, `volumeRatio`) and
    snake_case (`change_5d`, `max_1d_drop`). With no preset, indicator, or filter param, the response is
    a help object.

    Args:
        preset (GetV1ScanPreset | Unset):
        sector (str | Unset): Comma-separated sectors. Crypto includes every crypto pair. Example:
            Tech,Crypto.
        symbols (str | Unset): Comma-separated symbols. Overrides sector. Example: AAPL,X:BTCUSD.
        limit (int | Unset): Default 50.
        sort (GetV1ScanSort | Unset):
        min_rsi (float | None | Unset):
        max_rsi (float | None | Unset):
        min_bb_position (float | None | Unset):
        max_bb_position (float | None | Unset):
        min_change_1d (float | None | Unset):
        max_change_1d (float | None | Unset):
        min_change_5d (float | None | Unset):
        max_change_5d (float | None | Unset):
        min_change_30d (float | None | Unset):
        max_change_30d (float | None | Unset):
        min_volume_ratio (float | None | Unset):
        min_price (float | None | Unset):
        max_price (float | None | Unset):
        min_daily_dollar_volume (float | None | Unset):
        include_leveraged (GetV1ScanIncludeLeveraged | Unset):
        refresh (GetV1ScanRefresh | Unset): Bypass the market data cache. Applies to live presets
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GetV1ScanResponse200]
    """

    kwargs = _get_kwargs(
        preset=preset,
        sector=sector,
        symbols=symbols,
        limit=limit,
        sort=sort,
        min_rsi=min_rsi,
        max_rsi=max_rsi,
        min_bb_position=min_bb_position,
        max_bb_position=max_bb_position,
        min_change_1d=min_change_1d,
        max_change_1d=max_change_1d,
        min_change_5d=min_change_5d,
        max_change_5d=max_change_5d,
        min_change_30d=min_change_30d,
        max_change_30d=max_change_30d,
        min_volume_ratio=min_volume_ratio,
        min_price=min_price,
        max_price=max_price,
        min_daily_dollar_volume=min_daily_dollar_volume,
        include_leveraged=include_leveraged,
        refresh=refresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    preset: GetV1ScanPreset | Unset = UNSET,
    sector: str | Unset = UNSET,
    symbols: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort: GetV1ScanSort | Unset = UNSET,
    min_rsi: float | None | Unset = UNSET,
    max_rsi: float | None | Unset = UNSET,
    min_bb_position: float | None | Unset = UNSET,
    max_bb_position: float | None | Unset = UNSET,
    min_change_1d: float | None | Unset = UNSET,
    max_change_1d: float | None | Unset = UNSET,
    min_change_5d: float | None | Unset = UNSET,
    max_change_5d: float | None | Unset = UNSET,
    min_change_30d: float | None | Unset = UNSET,
    max_change_30d: float | None | Unset = UNSET,
    min_volume_ratio: float | None | Unset = UNSET,
    min_price: float | None | Unset = UNSET,
    max_price: float | None | Unset = UNSET,
    min_daily_dollar_volume: float | None | Unset = UNSET,
    include_leveraged: GetV1ScanIncludeLeveraged | Unset = UNSET,
    refresh: GetV1ScanRefresh | Unset = UNSET,
) -> ErrorEnvelope | GetV1ScanResponse200 | None:
    """Screener / scan

     Screener endpoint with presets, composable filters, and sorts. Inherits all query params from the
    legacy /api/data/scan endpoint. `mode` tells where the rows come from: `precomputed` (daily preset
    snapshot, used while it is less than 6 hours old), `live` (preset computed on request; can take
    20-30s), or `filter` (any min_/max_ param; reads the daily indicator cache). In `precomputed` and
    `filter` modes, price and change fields are from the last completed daily bar: check
    `dataAgeSeconds`. Without `sector` or `symbols`, filter mode reads at most 1000 cache rows, so some
    tradeable symbols can be missing. Row keys mix camelCase (`bbPosition`, `volumeRatio`) and
    snake_case (`change_5d`, `max_1d_drop`). With no preset, indicator, or filter param, the response is
    a help object.

    Args:
        preset (GetV1ScanPreset | Unset):
        sector (str | Unset): Comma-separated sectors. Crypto includes every crypto pair. Example:
            Tech,Crypto.
        symbols (str | Unset): Comma-separated symbols. Overrides sector. Example: AAPL,X:BTCUSD.
        limit (int | Unset): Default 50.
        sort (GetV1ScanSort | Unset):
        min_rsi (float | None | Unset):
        max_rsi (float | None | Unset):
        min_bb_position (float | None | Unset):
        max_bb_position (float | None | Unset):
        min_change_1d (float | None | Unset):
        max_change_1d (float | None | Unset):
        min_change_5d (float | None | Unset):
        max_change_5d (float | None | Unset):
        min_change_30d (float | None | Unset):
        max_change_30d (float | None | Unset):
        min_volume_ratio (float | None | Unset):
        min_price (float | None | Unset):
        max_price (float | None | Unset):
        min_daily_dollar_volume (float | None | Unset):
        include_leveraged (GetV1ScanIncludeLeveraged | Unset):
        refresh (GetV1ScanRefresh | Unset): Bypass the market data cache. Applies to live presets
            only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GetV1ScanResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            preset=preset,
            sector=sector,
            symbols=symbols,
            limit=limit,
            sort=sort,
            min_rsi=min_rsi,
            max_rsi=max_rsi,
            min_bb_position=min_bb_position,
            max_bb_position=max_bb_position,
            min_change_1d=min_change_1d,
            max_change_1d=max_change_1d,
            min_change_5d=min_change_5d,
            max_change_5d=max_change_5d,
            min_change_30d=min_change_30d,
            max_change_30d=max_change_30d,
            min_volume_ratio=min_volume_ratio,
            min_price=min_price,
            max_price=max_price,
            min_daily_dollar_volume=min_daily_dollar_volume,
            include_leveraged=include_leveraged,
            refresh=refresh,
        )
    ).parsed
