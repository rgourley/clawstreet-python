from enum import Enum


class MarginEventEventType(str, Enum):
    FORCED_LIQUIDATION = "forced_liquidation"
    MARGIN_CALL = "margin_call"
    MARGIN_RESTORED = "margin_restored"

    def __str__(self) -> str:
        return str(self.value)
