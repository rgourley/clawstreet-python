from enum import Enum


class GetV1MeAgentsIdEquityCurvePeriod(str, Enum):
    ALL = "ALL"
    VALUE_0 = "1D"
    VALUE_1 = "1W"
    VALUE_2 = "1M"
    VALUE_3 = "3M"

    def __str__(self) -> str:
        return str(self.value)
