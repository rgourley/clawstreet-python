from enum import StrEnum


class PatchV1MeBodyVisibility(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
