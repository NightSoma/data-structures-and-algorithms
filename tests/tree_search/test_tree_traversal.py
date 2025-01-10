import pytest

from tree_search.binary_node import BinaryNode
from tree_search.tree_traversal import (
    in_order_search,
    post_order_search,
    pre_order_search,
)


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


#        7
#   23      3
# 5    4  18   21


def test_pre_order_search__only_root(head: BinaryNode[int]):
    assert pre_order_search(BinaryNode(5, None, None)) == [5]


def test_pre_order_search(head: BinaryNode[int]):
    assert pre_order_search(head) == [7, 23, 5, 4, 3, 18, 21]


def test_in_order_search(head: BinaryNode[int]):
    assert in_order_search(head) == [5, 23, 4, 7, 18, 3, 21]


def test_post_order_search(head: BinaryNode[int]):
    assert post_order_search(head) == [5, 4, 23, 18, 21, 3, 7]
