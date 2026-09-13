from enum import StrEnum


class JournalNoteKind(StrEnum):
    NOTE = "note"

    def __str__(self) -> str:
        return str(self.value)
