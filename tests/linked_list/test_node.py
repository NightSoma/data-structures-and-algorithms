import pytest

from linked_lists.forward_linked_list.linked_list import Node


@pytest.fixture()
def node() -> Node[int]:
    return Node[int](5, None)


def test_creation(node: Node[int]):
    assert isinstance(node, Node)
    assert node.next is None
    assert node.item == 5


def test_magic_eq(node: Node[int]):
    assert node == Node[int](5, None)
    assert node != Node[str]("5", None)
    assert node == Node[int](5, Node[int](0, None))
    assert node != Node[int](4, None)
    with pytest.raises(NotImplementedError):
        assert Node[int](4, None) == "str"
    with pytest.raises(NotImplementedError):
        assert Node[int](4, None) != "str"


def test_str_method(node: Node[int]):
    assert str(node) == f"Node(item=[{node.item}], next=[{node.next!r}])"


def test_repr_method(node: Node[int]):
    assert repr(node) == f"Node(item=[{node.item}], next=[{bool(node.next)}])"
