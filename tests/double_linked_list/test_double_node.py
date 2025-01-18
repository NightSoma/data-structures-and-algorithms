import pytest

from doubly_linked_list.double_node import DoubleNode


@pytest.fixture()
def nodes() -> list[DoubleNode[int]]:
    node0 = DoubleNode[int](0)
    node2 = DoubleNode[int](2)

    node1 = DoubleNode[int](1, prev_node=node0, next_node=node2)

    node0.next = node1
    node2.prev = node1

    return [node0, node1, node2]


def test__init__(nodes: list[DoubleNode[int]]):
    assert isinstance(nodes[1], DoubleNode)
    assert nodes[1].prev is nodes[0]
    assert nodes[1].next is nodes[2]
    assert nodes[1].item == 1


def test__eq__(nodes: list[DoubleNode[int]]):
    assert DoubleNode[int](1) == DoubleNode[int](1)
    assert DoubleNode[int](1) != DoubleNode[str]("1")
    assert DoubleNode[int](1) == DoubleNode[int](1, DoubleNode[int](0))
    assert DoubleNode[int](3) != DoubleNode[int](4)


def test__eq__raise_not_implemented_error_for_wrong_types(nodes: list[DoubleNode[int]]):
    with pytest.raises(NotImplementedError):
        assert DoubleNode[int](4) == "str"
    with pytest.raises(NotImplementedError):
        assert DoubleNode[int](4) != "str"


def test__str__(nodes: list[DoubleNode[int]]):
    assert str(nodes[1]) == f"Node(item=[1], prev=[{True}], next=[{True}])"


def test__repr__(nodes: list[DoubleNode[int]]):
    _prev = f"Node(item=[0], prev=[{False}], next=[{True}])"
    _next = f"Node(item=[2], prev=[{True}], next=[{False}])"
    assert repr(nodes[1]) == f"Node(item=[1], prev=[{_prev}], next=[{_next}])"
