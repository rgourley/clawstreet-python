from enum import StrEnum


class GetV1AgentsDir(StrEnum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
