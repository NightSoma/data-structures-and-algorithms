import pytest

from tree_search.binary_node import BinaryNode
from tree_search.depth_first_search import depth_first_search


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


def test_depth_fitst_search__single_node_needle_exist():
    assert depth_first_search(BinaryNode(5, None, None), 5) is True


def test_depth_fitst_search__single_node_needle_not_exist():
    assert depth_first_search(BinaryNode(5, None, None), 4) is False


def test_depth_fitst_search__none_head():
    assert depth_first_search(None, 5) is False


def test_depth_fitst_search__large_tree_needle_exist(head_full_tree: BinaryNode[int]):
    assert depth_first_search(head_full_tree, 24) is True


def test_depth_fitst_search__large_tree_needle_not_exist(
    head_full_tree: BinaryNode[int],
):
    assert depth_first_search(head_full_tree, 100) is False
