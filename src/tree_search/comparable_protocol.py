from typing import Any, Protocol


class Comparable(Protocol):
    """Protocol for types that support comparison."""

    def __lt__(self, __: Any) -> bool: ...

    def __le__(self, __: Any) -> bool: ...
