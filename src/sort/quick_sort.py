from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    """Protocol for types that support comparison."""

    def __lt__(self, __: Any) -> bool: ...

    def __le__(self, __: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


def partition(arr: list[T], low: int, high: int) -> int:
    pivot = arr[high]
    idx = low - 1

    for i in range(low, high):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    idx += 1
    arr[high], arr[idx] = arr[idx], arr[high]
    return idx


def quick_sort(
    arr: list[T],
    low: int,
    high: int,
) -> None:
    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


def quick_sort_in_place(
    arr: list[T],
) -> list[T]:
    if len(arr) <= 1:
        return arr
    quick_sort(arr, 0, len(arr) - 1)
    return arr


def quick_sort_new_arrays(arr: list[T]) -> list[T]:
    length = len(arr)
    if length <= 1:
        return arr
    left: list[T] = []
    right: list[T] = []
    start_pivot_index = length // 2

    for i in range(length):
        if arr[i] < arr[start_pivot_index]:
            left.append(arr[i])
        elif arr[i] > arr[start_pivot_index]:
            right.append(arr[i])

    return [
        *quick_sort_new_arrays(left),
        arr[start_pivot_index],
        *quick_sort_new_arrays(right),
    ]
