from enum import Enum


class DeleteV1ThoughtsIdResponse403ErrorCode(str, Enum):
    INSUFFICIENT_SCOPE = "INSUFFICIENT_SCOPE"

    def __str__(self) -> str:
        return str(self.value)
