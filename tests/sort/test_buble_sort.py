import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.sort.buble_sort import Comparable, bubble_sort

SortableType = int | float | str


def test_bubble_sort() -> None:
    test_cases: list[tuple[list[SortableType], list[SortableType]]] = [
        ([1, 5, 2, 8, 3], [1, 2, 3, 5, 8]),
        ([1.5, 2.3, 1.1], [1.1, 1.5, 2.3]),
        (["c", "a", "b"], ["a", "b", "c"]),
        ([], []),
    ]

    for input_arr, expected in test_cases:
        result = bubble_sort(input_arr.copy())  # type: ignore
        assert result == expected


@given(st.lists(st.integers()))
def test_list_always_sorted(lst: list[int]) -> None:
    result = bubble_sort(lst.copy())  # type: ignore
    assert result == sorted(lst)


def test_comparable_protocol():
    with pytest.raises(NotImplementedError):
        Comparable.__lt__(None, None) # type: ignore
