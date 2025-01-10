import pytest

from src.search.linear_search import linear_search, linear_search_bool


@pytest.mark.parametrize(
    "array, needle, expected",
    [
        ([1, 8, 5, 7, 2], 1, 0),
        ([1, 3, 5, 5, 1], 3, 1),
        ([9, 4, 2, 4, 2], 2, 2),
        ([-1, -5, 0, 2], -5, 1),
        ([1, 1, 1, 1], 1, 0),
    ],
)
def test_linear_search(array: list[int], needle: int, expected: int):
    assert expected == linear_search(array, needle)


def test_linear_search_no_element_can_be_found():
    array = [1, 3, 4]
    find_element = 2
    correct_index = -1

    assert correct_index == linear_search(array, find_element)


def test_linear_search_small_array():
    array = [1]
    find_element = 1
    correct_index = 0

    assert correct_index == linear_search(array, find_element)


def test_linear_search_empty_array():
    array: list[int] = []
    find_element = 1
    correct_index = -1

    assert correct_index == linear_search(array, find_element)


@pytest.mark.parametrize(
    "array, needle, expected",
    [
        ([1, 8, 5, 7, 2], 1, True),
        ([1, 3, 5, 5, 1], 3, True),
        ([9, 4, 2, 4, 2], 2, True),
        ([-1, -5, 0, 2], -5, True),
        ([1, 1, 1, 1], 1, True),
    ],
)
def test_linear_search_bool(array: list[int], needle: int, expected: bool):
    assert expected == linear_search_bool(array, needle)


def test_linear_search_bool_no_element_can_be_found():
    array = [1, 3, 4]
    find_element = 2
    correct_result = False

    assert correct_result == linear_search_bool(array, find_element)


def test_linear_search_bool_small_array():
    array = [1]
    find_element = 1
    correct_result = True

    assert correct_result == linear_search_bool(array, find_element)


def test_linear_search_bool_empty_array():
    array: list[int] = []
    find_element = 1
    correct_result = False

    assert correct_result == linear_search_bool(array, find_element)
