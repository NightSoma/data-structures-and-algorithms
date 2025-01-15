import pytest

from tree_search.binary_node import BinaryNode
from tree_search.depth_first_delete import depth_first_delete


@pytest.fixture
def head_full_tree() -> BinaryNode[int]:
    """_______3
        1            5
    0       2    4        7
                        6     8
    """
    return BinaryNode(
        3,
        BinaryNode(
            1,
            BinaryNode(0, None, None),
            BinaryNode(2, None, None),
        ),
        BinaryNode(
            5,
            BinaryNode(4, None, None),
            BinaryNode(
                7,
                BinaryNode(6, None, None),
                BinaryNode(8, None, None),
            ),
        ),
    )


def test_depth_first_delete__head_none():
    assert depth_first_delete(None, 0) is False


def test_depth_first_delete__3_head(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 3) is True
    assert head_full_tree is not None
    assert head_full_tree.value == 4
    assert head_full_tree.left is not None
    assert head_full_tree.right is not None
    assert head_full_tree.left.value == 1
    assert head_full_tree.right.value == 5


def test_depth_first_delete__1(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 1) is True
    assert head_full_tree.left is not None
    assert head_full_tree.left.value == 2
    assert head_full_tree.left.right is None
    assert head_full_tree.left.left is not None
    assert head_full_tree.left.left.value == 0


def test_depth_first_delete__0(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 0) is True
    assert head_full_tree.left is not None
    assert head_full_tree.left.left is None
    assert head_full_tree.left.value == 1


def test_depth_first_delete__2(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 2) is True
    assert head_full_tree.left is not None
    assert head_full_tree.left.left is not None
    assert head_full_tree.left.left.value == 0
    assert head_full_tree.left.right is None


def test_depth_first_delete__needle_not_exist(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 1000) is False


def test_depth_first_delete__5(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 5) is True
    assert head_full_tree.right is not None
    assert head_full_tree.right.value == 6
    assert head_full_tree.right.right is not None
    assert head_full_tree.right.right.left is None


def test_depth_first_delete__4(head_full_tree: BinaryNode[int]):
    assert depth_first_delete(head_full_tree, 4) is True
    assert head_full_tree.right is not None
    assert head_full_tree.right.left is None
    assert head_full_tree.right.value == 5


def test_depth_first_delete__3_replacment_from_left(head_full_tree: BinaryNode[int]):
    head_full_tree.right = None
    assert depth_first_delete(head_full_tree, 3) is True

    assert head_full_tree.value == 2


def test_depth_first_delete__3_replacment_from_left_right(
    head_full_tree: BinaryNode[int],
):
    head_full_tree.right = None
    assert head_full_tree.left is not None
    head_full_tree.left.right = None

    assert depth_first_delete(head_full_tree, 3) is True

    assert head_full_tree.value == 1


def test_depth_first_delete__3_replacment_from_right(
    head_full_tree: BinaryNode[int],
):
    assert head_full_tree.right is not None
    head_full_tree.right.left = None

    assert depth_first_delete(head_full_tree, 3) is True

    assert head_full_tree.value == 5


def test_depth_first_delete__3_head_no_replacment():
    head = BinaryNode(3, None, None)
    assert depth_first_delete(head, 3) is True
    assert head is not None
    assert head.value == 3
