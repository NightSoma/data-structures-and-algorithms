import pytest

from tree_search.binary_node import BinaryNode
from tree_search.deapth_first_find import deapth_first_find


@pytest.fixture
def head_full_tree() -> BinaryNode[int]:
    """_______32
        23          34
    5       24   33    35
    """
    return BinaryNode(
        32,
        BinaryNode(
            23,
            BinaryNode(5, None, None),
            BinaryNode(24, None, None),
        ),
        BinaryNode(
            34,
            BinaryNode(33, None, None),
            BinaryNode(35, None, None),
        ),
    )


def test_deapth_first_find__empty_tree():
    assert deapth_first_find(None, 35) is False


def test_deapth_first_find__exist_35(head_full_tree: BinaryNode[int]):
    assert deapth_first_find(head_full_tree, 35) is True


def test_deapth_first_find__exist_5(head_full_tree: BinaryNode[int]):
    assert deapth_first_find(head_full_tree, 5) is True


def test_deapth_first_find__not_exist(head_full_tree: BinaryNode[int]):
    assert deapth_first_find(head_full_tree, 36) is False
