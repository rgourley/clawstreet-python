from enum import StrEnum


class GetV1MeAgentsIdEquityCurvePeriod(StrEnum):
    ALL = "ALL"
    VALUE_0 = "1D"
    VALUE_1 = "1W"
    VALUE_2 = "1M"
    VALUE_3 = "3M"

    def __str__(self) -> str:
        return str(self.value)
