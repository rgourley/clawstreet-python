from enum import StrEnum


class GetV1ScanSort(StrEnum):
    BB_POSITION_ASC = "bb_position_asc"
    BB_POSITION_DESC = "bb_position_desc"
    CHANGE_1D_ASC = "change_1d_asc"
    CHANGE_1D_DESC = "change_1d_desc"
    CHANGE_30D_ASC = "change_30d_asc"
    CHANGE_30D_DESC = "change_30d_desc"
    CHANGE_5D_ASC = "change_5d_asc"
    CHANGE_5D_DESC = "change_5d_desc"
    DAILY_DOLLAR_VOLUME_DESC = "daily_dollar_volume_desc"
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"
    RSI_ASC = "rsi_asc"
    RSI_DESC = "rsi_desc"
    VOLUME_RATIO_ASC = "volume_ratio_asc"
    VOLUME_RATIO_DESC = "volume_ratio_desc"

    def __str__(self) -> str:
        return str(self.value)
