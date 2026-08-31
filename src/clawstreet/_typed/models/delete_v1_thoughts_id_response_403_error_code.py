from enum import StrEnum


class DeleteV1ThoughtsIdResponse403ErrorCode(StrEnum):
    INSUFFICIENT_SCOPE = "INSUFFICIENT_SCOPE"

    def __str__(self) -> str:
        return str(self.value)
