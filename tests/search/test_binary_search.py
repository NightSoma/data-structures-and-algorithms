
import pytest

from src.search.binary_search import binary_search


@pytest.mark.parametrize(
    "array, needle, expected",
    [
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 5, 7], 3, 1),
        ([1, 1, 1, 1, 2], 2, 4),
        ([-5, -2, 0, 1], -5, 0),
    ],
)
def test_binary_search(array: list[int], needle: int, expected: int):
    assert expected == binary_search(array, needle)


def test_binary_search_no_element_can_be_found():
    array = [1, 2, 3]
    find_element = 2
    correct_index = 1

    assert correct_index == binary_search(array, find_element)


def test_binary_search_small_array():
    array = [1]
    find_element = 1
    correct_index = 0

    assert correct_index == binary_search(array, find_element)


def test_binary_search_empty_array():
    array: list[int] = []
    find_element = 1
    correct_index = -1

    assert correct_index == binary_search(array, find_element)


def test_binary_search_all_identical_elements():
    array = [5, 5, 5, 5, 5]
    find_element = 5
    correct_index = 2  # Any index from 0 to 4 is correct

    assert correct_index == binary_search(array, find_element)


def test_binary_search_element_smaller_than_all():
    array = [5, 7, 9, 11, 13]
    find_element = 3
    correct_index = -1

    assert correct_index == binary_search(array, find_element)


def test_binary_search_element_larger_than_all():
    array = [1, 3, 5, 7, 9]
    find_element = 10
    correct_index = -1

    assert correct_index == binary_search(array, find_element)
    assert correct_index == binary_search(array, find_element)


def test_binary_search_with_floats():
    array = [-1.5, 0.0, 2.25, 3.75, 5.0]
    find_element = 2.25
    correct_index = 2

    assert correct_index == binary_search(array, find_element)


def test_binary_search_mixed_numbers():
    array = [-10, -5, 0, 5, 10]
    find_element = 5
    correct_index = 3

    assert correct_index == binary_search(array, find_element)
    assert correct_index == binary_search(array, find_element)


def test_binary_search_finds_last_element():
    array = [1, 2, 3, 4, 5]
    find_element = 5
    correct_index = 4

    assert correct_index == binary_search(array, find_element)


def test_binary_search_multiple_occurrences():
    array = [1, 2, 2, 2, 3, 4, 5]
    find_element = 2
    expected_index = 1  # Any index from 1 to 3 is correct

    result = binary_search(array, find_element)
    assert result in [1, 2, 3], f"Expected index 1, 2, or 3, but got {result}"


def test_binary_search_large_list():
    large_list = list(range(1000000))
    find_element = 999999
    correct_index = 999999

    assert correct_index == binary_search(large_list, find_element)


def test_binary_search_high_low_difference_one():
    array = [1, 3, 5, 7]
    find_element = 4
    correct_index = -1

    assert correct_index == binary_search(array, find_element)
    assert correct_index == binary_search(array, find_element)


def test_binary_search_two_elements():
    array = [1, 3]
    assert binary_search(array, 1) == 0
    assert binary_search(array, 3) == 1
    assert binary_search(array, 2) == -1
