import pytest

from tree_search.binary_node import BinaryNode
from tree_search.breadth_first_search import (
    breadth_first_search,
    breadth_first_search_traversal,
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
            8,
            BinaryNode(21, None, None),
            BinaryNode(15, None, None),
        ),
    )


#        7
#   23       8
# 5    4  21   15


def test_breadth_first_traversal(head: BinaryNode[int]):
    assert breadth_first_search_traversal(head) == [7, 23, 8, 5, 4, 21, 15]


def test_breadth_first_search__needle_exist(head: BinaryNode[int]):
    assert breadth_first_search(head, 15) is True


def test_breadth_first_search__needle_not_exist(head: BinaryNode[int]):
    assert breadth_first_search(head, 0) is False
