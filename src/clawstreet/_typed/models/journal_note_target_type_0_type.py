from enum import StrEnum


class JournalNoteTargetType0Type(StrEnum):
    THOUGHT = "thought"
    TRADE = "trade"

    def __str__(self) -> str:
        return str(self.value)
