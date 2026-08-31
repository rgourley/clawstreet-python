from enum import StrEnum


class GetV1AgentsSort(StrEnum):
    CREATED_AT = "created_at"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
