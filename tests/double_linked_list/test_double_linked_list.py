import pytest

from doubly_linked_list.double_linked_list import DoubleLinkedList, DoubleNode


@pytest.fixture()
def linked_list() -> DoubleLinkedList[int]:
    return DoubleLinkedList[int]([0, 1, 2, 3])


@pytest.fixture()
def nodes() -> list[DoubleNode[int]]:
    node1 = DoubleNode[int](0)
    node2 = DoubleNode[int](1)
    node3 = DoubleNode[int](2)
    node4 = DoubleNode[int](3)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3

    return [node1, node2, node3, node4]


def test__init__empty():
    linked_list = DoubleLinkedList[int]()

    assert len(linked_list) == 0
    assert linked_list.head is None


def test__init__from_container(
    linked_list: DoubleLinkedList[int], nodes: list[DoubleNode[int]]
):
    assert linked_list.head == nodes[0]
    assert linked_list.tail == nodes[3]


def test__len__(linked_list: DoubleLinkedList[int]):
    assert len(linked_list) == 4


def test__eq__equal():
    assert DoubleLinkedList([0, 1, 2]) == DoubleLinkedList([0, 1, 2])


def test__eq__not_equal():
    assert DoubleLinkedList([0, 1, 2]) != DoubleLinkedList([0, 0, 2])


def test__eq__different_length():
    assert DoubleLinkedList([1, 2, 3]) != DoubleLinkedList([1, 2])
    assert DoubleLinkedList([1, 2, 3]) != DoubleLinkedList([1, 2, 3, 4])


def test__eq__different_type():
    with pytest.raises(NotImplementedError):
        assert DoubleLinkedList([1, 2, 3]) == "str"
    with pytest.raises(NotImplementedError):
        assert DoubleLinkedList([1, 2, 3]) != "str"


def test_iteration(linked_list: DoubleLinkedList[int], nodes: list[DoubleNode[int]]):
    for node, elem in zip(nodes, linked_list, strict=False):
        assert elem == node


def test_iteration__from_tail(
    linked_list: DoubleLinkedList[int], nodes: list[DoubleNode[int]]
):
    for node, elem in zip(reversed(nodes), reversed(linked_list), strict=False):
        assert elem == node


def test_find_closer_iterator__head_closer(
    linked_list: DoubleLinkedList[int], nodes: list[DoubleNode[int]]
):
    for node, elem in zip(nodes, linked_list.find_closer_iterator(1), strict=False):
        assert elem == node


def test_find_closer_iterator__tail_closer(
    linked_list: DoubleLinkedList[int], nodes: list[DoubleNode[int]]
):
    for node, elem in zip(
        reversed(nodes), linked_list.find_closer_iterator(3), strict=False
    ):
        assert elem == node


def test_insert__head(linked_list: DoubleLinkedList[int]):
    linked_list.insert_head(-159)
    assert linked_list.head == DoubleNode(-159, None)


def test_insert_at__head(linked_list: DoubleLinkedList[int]):
    linked_list.insert_at(-159, 0)
    assert linked_list.head == DoubleNode(-159, None)


def test_insert_at__middle(linked_list: DoubleLinkedList[int]):
    linked_list.insert_at(-159, 2)
    assert linked_list.head is not None
    assert linked_list.head.next is not None
    assert linked_list.head.next.next == DoubleNode(-159)


def test_insert_at__before_end(linked_list: DoubleLinkedList[int]):
    linked_list.insert_at(-159, len(linked_list) - 1)
    assert linked_list[-2] == -159


def test_reverse():
    ll = DoubleLinkedList([1, 2, 3])
    ll.reverse()
    assert ll == DoubleLinkedList([3, 2, 1])
    assert ll != DoubleLinkedList([3, 1, 1])


def test_find_item__that_exist():
    assert DoubleLinkedList([1, 2, 3]).find_item_index(3) == 2


def test_find_item__that_not_exist():
    assert DoubleLinkedList([1, 2, 3]).find_item_index(-1) is None


def test_find_item__multiple_matches():
    assert DoubleLinkedList([1, 1, 3]).find_item_index(1) == 0


def test_remove__that_exist():
    ll = DoubleLinkedList([1, 2, 3])
    assert ll.remove(2) == 2
    assert ll.remove(2) is None
    assert ll == DoubleLinkedList([1, 3])


def test_remove__tail():
    ll = DoubleLinkedList([1, 2, 3])
    assert ll.remove(3) == 3
    assert ll.remove(3) is None
    assert ll == DoubleLinkedList([1, 2])


def test_remove__multiple_same_items():
    ll = DoubleLinkedList([1, 1, 1])
    ll.remove(1)
    assert ll == DoubleLinkedList([1, 1])
    ll.remove(1)
    assert ll == DoubleLinkedList([1])
    ll.remove(1)
    assert ll == DoubleLinkedList([])
    assert ll.remove(1) is None


def test_remove_head__once():
    assert DoubleLinkedList([1, 2, 3]).remove_head() == 1


def test_remove_head__multiple_times():
    ll = DoubleLinkedList([1, 2, 3])
    ll.remove_head()
    ll.remove_head()
    ll.remove_head()
    ll.remove_head()
    assert ll == DoubleLinkedList([])


def test_remove_at__that_exist():
    assert DoubleLinkedList([1, 2, 3]).remove_at(1) == 2


def test_remove_at__diffenet_places_untill_empty():
    ll = DoubleLinkedList([1, 2, 3])
    assert ll.remove_at(2) == 3
    assert ll == DoubleLinkedList([1, 2])
    assert ll.remove_at(0) == 1
    assert ll == DoubleLinkedList([2])
    assert ll.remove_at(0) == 2
    assert ll.remove_at(0) is None


def test_append__empty_linked_list():
    linked_list = DoubleLinkedList[int]()
    assert linked_list.head is None
    assert linked_list.tail is None
    linked_list.append(3)
    assert linked_list.head == DoubleNode(3, None)
    assert linked_list.tail == DoubleNode(3, None)
    linked_list.append(4)
    linked_list.append(5)
    assert linked_list.tail == DoubleNode(5, None)


def test_append__tail_restoration():
    linked_list = DoubleLinkedList[int]()
    linked_list.append(3)
    linked_list.tail = None
    linked_list.append(4)
    assert linked_list == DoubleLinkedList[int]([3, 4])
    assert linked_list.tail == DoubleNode(4, None)


def test_get_node__simple_access():
    assert DoubleLinkedList([1, 2, 3, 4]).get_node(3) == DoubleNode(4, None)
    assert DoubleLinkedList([1, 2, 3, 4]).get_node(2) == DoubleNode(3, None)
    assert DoubleLinkedList([1, 2, 3, 4]).get_node(0) == DoubleNode(1, None)


def test_get__simple_access():
    assert DoubleLinkedList([1, 2, 3, 4]).get_item(3) == 4
    assert DoubleLinkedList([1, 2, 3, 4]).get_item(2) == 3
    assert DoubleLinkedList([1, 2, 3, 4]).get_item(0) == 1


def test_get__empty_linked_list():
    linked_list = DoubleLinkedList[int]([])
    assert linked_list.get_item(0) is None


def test__validate_index__above_limit():
    with pytest.raises(ValueError):
        DoubleLinkedList([1, 2, 3]).insert_at(100, 4)


def test__validate_index__under_limit():
    with pytest.raises(ValueError):
        DoubleLinkedList([1, 2, 3]).insert_at(100, -1)


def test_square_brackets_getter__single_value():
    assert DoubleLinkedList([1, 2, 3, 4, 5, 6, 7, 8])[3] == 4


def test_square_brackets_getter__slice():
    assert DoubleLinkedList([1, 2, 3, 4, 5, 6, 7, 8])[:] == [1, 2, 3, 4, 5, 6, 7, 8]


def test_square_brackets_getter__negative_start_stop():
    assert DoubleLinkedList([1, 2, 3, 4])[-3:-1] == [2, 3]


def test_square_brackets_getter__above_len_start_stop_step():
    assert DoubleLinkedList([1, 2, 3, 4])[100:100:100] == []


def test_square_brackets_setter__empty_linked_list():
    ll = DoubleLinkedList[int]()
    ll[0] = 100
    assert ll == DoubleLinkedList([])


def test_square_brackets_setter__single_value():
    ll = DoubleLinkedList[int]([1])
    ll[0] = 100
    assert ll == DoubleLinkedList([100])


def test_square_brackets_setter__single_value_negative_index():
    ll = DoubleLinkedList([1, 5])
    ll[-1] = 100
    assert ll == DoubleLinkedList([1, 100])


def test_square_brackets_setter__slice():
    ll = DoubleLinkedList([1, 2, 3, 4, 5])
    ll[0:5] = 100
    assert ll == DoubleLinkedList([100, 100, 100, 100, 100])


def test__del__single_delete():
    ll = DoubleLinkedList([1, 2, 3, 4, 5])
    del ll[0]
    assert ll == DoubleLinkedList([2, 3, 4, 5])


def test__del__negative_index():
    ll = DoubleLinkedList([2, 3, 4, 5])
    del ll[-1]
    assert ll == DoubleLinkedList([2, 3, 4])


def test__del__slice_delete():
    ll = DoubleLinkedList([1, 2, 3, 4, 5])
    del ll[1:3]
    assert ll == DoubleLinkedList([1, 4, 5])


def test_str_method(linked_list: DoubleLinkedList[int]):
    assert (
        str(linked_list)
        == f"LinkedList(head=[{linked_list.head!s}], tail=[{linked_list.tail!s}], len=[{linked_list.length}])"
    )


def test_repr_method(linked_list: DoubleLinkedList[int]):
    assert (
        repr(linked_list)
        == f"LinkedList(head=[{linked_list.head!r}], tail=[{linked_list.tail!r}], len=[{linked_list.length}])"
    )
