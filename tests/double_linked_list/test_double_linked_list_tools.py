from typing import Any

import pytest

from double_linked_list.double_linked_list_tools import DoubleLinkedListTools


def test_validate_index__under_0_raises_error():
    with pytest.raises(ValueError):
        DoubleLinkedListTools.validate_index(-1, 5)


def test_validate_index__above_len_raises_error():
    with pytest.raises(ValueError):
        DoubleLinkedListTools.validate_index(6, 5)


class TestReversible:
    def __init__(self, ls: list[Any]) -> None:
        self.ls = ls

    def __iter__(self):
        return iter(self.ls)

    def __reversed__(self):
        return reversed(self.ls)


def slicer(_slice: slice, ls: list[Any]):
    return list(
        DoubleLinkedListTools.get_nodes_slice_generator(
            TestReversible(ls), _slice, len(ls)
        )
    )


def test_get_nodes_slice__forward():
    ls = [1, 2, 3, 4]

    assert ls[1:2] == slicer(slice(1, 2), ls)


def test_get_nodes_slice__reversed():
    ls = [1, 2, 3, 4]

    assert ls[3:2:-1] == slicer(slice(3, 2, -1), ls)


def test_get_nodes_slice__negative_start_stop_reversed():
    ls = [1, 2, 3, 4]

    assert ls[-3:-1:-1] == slicer(slice(-3, -1, -1), ls)


def test_get_nodes_slice__negative_start_stop():
    ls = [1, 2, 3, 4]

    assert ls[-3:-1] == slicer(slice(-3, -1), ls)


def test_get_nodes_slice__negative_step_2():
    ls = [1, 2, 3, 4]

    assert ls[::-2] == slicer(slice(None, None, -2), ls)


def test_get_nodes_slice__positive_step_2():
    ls = [1, 2, 3, 4]

    assert ls[::2] == slicer(slice(None, None, 2), ls)


def test_get_nodes_slice__start_negative():
    ls = [1, 2, 3, 4]

    assert ls[-4:4] == slicer(slice(-4, 4), ls)


def test_get_nodes_slice__stop_negative():
    ls = [1, 2, 3, 4]

    assert ls[0:-1] == slicer(slice(0, -1), ls)


def test_get_nodes_slice__start_step_negative():
    ls = [1, 2, 3, 4]

    assert ls[-1:0:-1] == slicer(slice(-1, 0, -1), ls)


def test_get_nodes_slice__stop_step_negative():
    ls = [1, 2, 3, 4]

    assert ls[4:0:-1] == slicer(slice(4, 0, -1), ls)


def test_get_nodes_slice__none_start_stop_step():
    ls = [1, 2, 3, 4]

    assert slicer(slice(None, None, None), ls) == ls[::]


def test_get_nodes_slice__negative_start_stop_step():
    ls = [1, 2, 3, 4]

    assert slicer(slice(-1, -3, -1), ls) == ls[-1:-3:-1]


def test_get_nodes_slice__larger_then_len_start_stop_step():
    ls = [1, 2, 3, 4]

    assert slicer(slice(500, 500, 500), ls) == ls[500:500:500]


def test_get_nodes_slice__raise_value_error_when_step_is_0():
    ls = [1, 2, 3, 4]

    with pytest.raises(ValueError):
        slicer(slice(0, 1, 0), ls)
