from typing import (
    Protocol,
    TypeVar,
)


class Comparable(Protocol):
    """Protocol that suggest comparison."""

    def __lt__(self, other: "Comparable") -> bool:
        """Check if type have magic comparison."""
        ...
        raise NotImplementedError


T = TypeVar(
    "T",
    bound=Comparable,
)


def bubble_sort(
    arr: list[T],
) -> list[T]:
    """Simple implementation of bubble sort."""
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
    return arr
