import pytest

from tree_search.binary_node import BinaryNode
from tree_search.depth_first_insert import depth_first_insert
from tree_search.tree_compare import tree_compare


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


def test_depth_first_insert__insert_into_none_tree():
    with pytest.raises(ValueError):
        depth_first_insert(None, 23)


def test_depth_first_insert__insert_23():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)
    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__insert_24():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    assert correct_tree.left is not None
    correct_tree.left.right = BinaryNode(24)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__insert_34():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    correct_tree.left.right = BinaryNode(24)

    depth_first_insert(insert_tree, 34)
    correct_tree.right = BinaryNode(34)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__insert_35():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    correct_tree.left.right = BinaryNode(24)

    depth_first_insert(insert_tree, 34)
    correct_tree.right = BinaryNode(34)

    depth_first_insert(insert_tree, 35)
    correct_tree.right.right = BinaryNode(35)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__insert_33():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    correct_tree.left.right = BinaryNode(24)

    depth_first_insert(insert_tree, 34)
    correct_tree.right = BinaryNode(34)

    depth_first_insert(insert_tree, 35)
    correct_tree.right.right = BinaryNode(35)

    depth_first_insert(insert_tree, 33)
    correct_tree.right.left = BinaryNode(33)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__insert_5():
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    correct_tree.left.right = BinaryNode(24)

    depth_first_insert(insert_tree, 34)
    correct_tree.right = BinaryNode(34)

    depth_first_insert(insert_tree, 35)
    correct_tree.right.right = BinaryNode(35)

    depth_first_insert(insert_tree, 33)
    correct_tree.right.left = BinaryNode(33)

    depth_first_insert(insert_tree, 5)
    correct_tree.left.left = BinaryNode(5)

    assert tree_compare(insert_tree, correct_tree) is True


def test_depth_first_insert__comapare_in_full(head_full_tree: BinaryNode[int]):
    correct_tree = BinaryNode(32)
    insert_tree = BinaryNode(32)

    depth_first_insert(insert_tree, 23)
    correct_tree.left = BinaryNode(23)

    depth_first_insert(insert_tree, 24)
    correct_tree.left.right = BinaryNode(24)

    depth_first_insert(insert_tree, 34)
    correct_tree.right = BinaryNode(34)

    depth_first_insert(insert_tree, 35)
    correct_tree.right.right = BinaryNode(35)

    depth_first_insert(insert_tree, 33)
    correct_tree.right.left = BinaryNode(33)

    depth_first_insert(insert_tree, 5)
    correct_tree.left.left = BinaryNode(5)

    assert tree_compare(insert_tree, head_full_tree) is True
    assert tree_compare(correct_tree, head_full_tree) is True
