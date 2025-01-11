import pytest

from tree_search.binary_node import BinaryNode
from tree_search.tree_compare import tree_compare


@pytest.fixture
def head() -> BinaryNode[int]:
    return BinaryNode(
        7,
        BinaryNode(
            23,
            BinaryNode(5, None, None),
            BinaryNode(4, None, None),
        ),
        BinaryNode(
            3,
            BinaryNode(18, None, None),
            BinaryNode(21, None, None),
        ),
    )


@pytest.fixture
def head_diff_structure() -> BinaryNode[int]:
    return BinaryNode(
        7,
        BinaryNode(
            23,
            BinaryNode(5, None, None),
            BinaryNode(4, None, None),
        ),
        BinaryNode(
            3,
            BinaryNode(18, None, None),
            BinaryNode(
                21,
                None,
                BinaryNode(21, None, None),
            ),
        ),
    )


@pytest.fixture
def head_diff_value() -> BinaryNode[int]:
    return BinaryNode(
        7,
        BinaryNode(
            23,
            BinaryNode(5, None, None),
            BinaryNode(4, None, None),
        ),
        BinaryNode(
            3,
            BinaryNode(18, None, None),
            BinaryNode(20, None, None),
        ),
    )


def test_tree_compare__two_nones():
    assert tree_compare(None, None) is True


def test_tree_compare__one_none(head: BinaryNode[int]):
    assert tree_compare(head, None) is False


def test_tree_compare__two_simmiliar(head: BinaryNode[int]):
    assert tree_compare(head, head) is True


def test_tree_compare__two_different_structures(
    head: BinaryNode[int], head_diff_structure: BinaryNode[int]
):
    assert tree_compare(head, head_diff_structure) is False


def test_tree_compare__two_different_values(
    head: BinaryNode[int], head_diff_value: BinaryNode[int]
):
    assert tree_compare(head, head_diff_value) is False
