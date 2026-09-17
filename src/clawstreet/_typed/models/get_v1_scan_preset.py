from enum import StrEnum


class GetV1ScanPreset(StrEnum):
    BREAKOUT = "breakout"
    MEAN_REVERSION = "mean_reversion"
    MOMENTUM = "momentum"
    OVERBOUGHT = "overbought"
    OVERSOLD = "oversold"
    OVERSOLD_DIP = "oversold_dip"
    VOLUME_SPIKE = "volume_spike"

    def __str__(self) -> str:
        return str(self.value)
