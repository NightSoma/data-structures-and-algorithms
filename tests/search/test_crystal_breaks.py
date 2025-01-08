import pytest

from src.search.crystal_breaks import crystal_break_at, crystal_break_at_isqrt


@pytest.mark.parametrize(
    "array, expected",
    [
        ([False, False, False, False, True], 4),
        ([False, True, True, True, True], 1),
        ([False, False, False, True, True], 3),
    ],
)
def test_crystal_break_at(array: list[bool], expected: int):
    assert expected == crystal_break_at(array)


def test_crystal_break__len_1():
    array = [False]
    correct_index = -1

    assert correct_index == crystal_break_at(array)


def test_crystal_break_at_it_not_break():
    array = [False, False, False]
    correct_index = -1

    assert correct_index == crystal_break_at(array)


def test_crystal_break_at_small_array():
    array = [True] * 3
    correct_index = 0

    assert correct_index == crystal_break_at(array)


def test_crystal_break_at_empty_array():
    array: list[bool] = []
    correct_index = -1

    assert correct_index == crystal_break_at(array)


def test_crystal_break_at_large_list():
    large_list = [False] * 100050 + [True] * 100000
    correct_index = 100050

    assert correct_index == crystal_break_at(large_list)


@pytest.mark.parametrize(
    "array, expected",
    [
        ([False, False, False, False, True], 4),
        ([False, True, True, True, True], 1),
        ([False, False, False, True, True], 3),
    ],
)
def test_crystal_break_at_isqrt(array: list[bool], expected: int):
    assert expected == crystal_break_at_isqrt(array)


def test_crystal_break_at_isqrt_it_not_break():
    array = [False, False, False]
    correct_index = -1

    assert correct_index == crystal_break_at_isqrt(array)


def test_crystal_break_at_isqrt_small_array():
    array = [True] * 3
    correct_index = 0

    assert correct_index == crystal_break_at_isqrt(array)


def test_crystal_break_at_isqrt_empty_array():
    array: list[bool] = []
    correct_index = -1

    assert correct_index == crystal_break_at_isqrt(array)


def test_crystal_break_at_isqrt_large_list():
    large_list = [False] * 100050 + [True] * 100000
    correct_index = 100050

    assert correct_index == crystal_break_at_isqrt(large_list)
