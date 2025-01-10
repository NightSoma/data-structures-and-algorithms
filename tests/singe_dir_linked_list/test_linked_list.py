import pytest

from single_dir_linked_list.linked_list import LinkedList, Node


@pytest.fixture()
def linked_list() -> LinkedList[int]:
    return LinkedList[int]([0, 1, 2, 3])


@pytest.fixture()
def nodes() -> list[Node[int]]:
    node1 = Node[int](0, None)
    node2 = Node[int](1, None)
    node3 = Node[int](2, None)
    node4 = Node[int](3, None)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    return [node1, node2, node3, node4]


def test__init__empty():
    linked_list = LinkedList[int]()

    assert len(linked_list) == 0
    assert linked_list.head is None


def test__init__from_container(linked_list: LinkedList[int], nodes: list[Node[int]]):
    assert linked_list.head == nodes[0]
    assert linked_list.tail == nodes[3]


def test__len__(linked_list: LinkedList[int]):
    assert len(linked_list) == 4


def test__eq__equal():
    assert LinkedList([0, 1, 2]) == LinkedList([0, 1, 2])


def test__eq__not_equal():
    assert LinkedList([0, 1, 2]) != LinkedList([0, 0, 2])


def test__eq__different_length():
    assert LinkedList([1, 2, 3]) != LinkedList([1, 2])
    assert LinkedList([1, 2, 3]) != LinkedList([1, 2, 3, 4])


def test__eq__different_type():
    with pytest.raises(NotImplementedError):
        assert LinkedList([1, 2, 3]) == "str"
    with pytest.raises(NotImplementedError):
        assert LinkedList([1, 2, 3]) != "str"


def test_iteration(linked_list: LinkedList[int], nodes: list[Node[int]]):
    for node, elem in zip(nodes, linked_list, strict=False):
        assert elem == node


def test_insert__head(linked_list: LinkedList[int]):
    linked_list.insert_at_head(-159)
    assert linked_list.head == Node(-159, None)


def test_insert_at__head(linked_list: LinkedList[int]):
    linked_list.insert_at(-159, 0)
    assert linked_list.head == Node(-159, None)


def test_insert_at__middle(linked_list: LinkedList[int]):
    linked_list.insert_at(-159, 2)
    assert linked_list.head is not None
    assert linked_list.head.next is not None
    assert linked_list.head.next.next == Node(-159, None)


def test_insert_at__before_end(linked_list: LinkedList[int]):
    linked_list.insert_at(-159, len(linked_list) - 1)
    assert linked_list[-2] == -159


def test_reverse():
    assert LinkedList([1, 2, 3]).reverse() == LinkedList([3, 2, 1])
    assert LinkedList([1, 2, 3]).reverse() != LinkedList([3, 1, 1])


def test_find_item__that_exist():
    assert LinkedList([1, 2, 3]).find_item_index(3) == 2


def test_find_item__that_not_exist():
    assert LinkedList([1, 2, 3]).find_item_index(-1) is None


def test_find_item__multiple_matches():
    assert LinkedList([1, 1, 3]).find_item_index(1) == 0


def test_remove__that_exist():
    ll = LinkedList([1, 2, 3])
    assert ll.remove(2) == 2
    assert ll.remove(2) is None
    assert ll == LinkedList([1, 3])


def test_remove__tail():
    ll = LinkedList([1, 2, 3])
    assert ll.remove(3) == 3
    assert ll.remove(3) is None
    assert ll == LinkedList([1, 2])


def test_remove__multiple_same_items():
    ll = LinkedList([1, 1, 1])
    ll.remove(1)
    assert ll == LinkedList([1, 1])
    ll.remove(1)
    assert ll == LinkedList([1])
    ll.remove(1)
    assert ll == LinkedList([])
    assert ll.remove(1) is None


def test_remove_head__once():
    assert LinkedList([1, 2, 3]).remove_head() == 1


def test_remove_head__multiple_times():
    ll = LinkedList([1, 2, 3])
    ll.remove_head()
    ll.remove_head()
    ll.remove_head()
    ll.remove_head()
    assert ll == LinkedList([])


def test_remove_at__that_exist():
    assert LinkedList([1, 2, 3]).remove_at(1) == 2


def test_remove_at__diffenet_places_untill_empty():
    ll = LinkedList([1, 2, 3])
    assert ll.remove_at(2) == 3
    assert ll == LinkedList([1, 2])
    assert ll.remove_at(0) == 1
    assert ll == LinkedList([2])
    assert ll.remove_at(0) == 2
    assert ll.remove_at(0) is None


def test_append__empty_linked_list():
    linked_list = LinkedList[int]()
    assert linked_list.head is None
    assert linked_list.tail is None
    linked_list.append(3)
    assert linked_list.head == Node(3, None)
    assert linked_list.tail == Node(3, None)
    linked_list.append(4)
    linked_list.append(5)
    assert linked_list.tail == Node(5, None)


def test_append__tail_restoration():
    linked_list = LinkedList[int]()
    linked_list.append(3)
    linked_list.tail = None
    linked_list.append(4)
    assert linked_list == LinkedList[int]([3, 4])
    assert linked_list.tail == Node(4, None)


def test_get_node__simple_access():
    assert LinkedList([1, 2, 3, 4]).get_node(3) == Node(4, None)
    assert LinkedList([1, 2, 3, 4]).get_node(2) == Node(3, None)
    assert LinkedList([1, 2, 3, 4]).get_node(0) == Node(1, None)


def test_get__simple_access():
    assert LinkedList([1, 2, 3, 4]).get(3) == 4
    assert LinkedList([1, 2, 3, 4]).get(2) == 3
    assert LinkedList([1, 2, 3, 4]).get(0) == 1


def test_get__empty_linked_list():
    linked_list = LinkedList[int]([])
    assert linked_list.get(0) is None


def test__validate_index__above_limit():
    with pytest.raises(ValueError):
        LinkedList([1, 2, 3]).insert_at(100, 4)


def test__validate_index__under_limit():
    with pytest.raises(ValueError):
        LinkedList([1, 2, 3]).insert_at(100, -1)


def test_square_brackets_getter__single_value():
    assert LinkedList([1, 2, 3, 4, 5, 6, 7, 8])[3] == 4


def test_square_brackets_getter__slice():
    assert LinkedList([1, 2, 3, 4, 5, 6, 7, 8])[:] == [1, 2, 3, 4, 5, 6, 7, 8]


def test_square_brackets_getter__error_expensive_backword_iteration():
    with pytest.raises(ValueError):
        LinkedList([1, 2, 3, 4, 5, 6, 7, 8])[3:0:1]


def test_square_brackets_getter__negative_step():
    with pytest.raises(ValueError):
        assert LinkedList([1, 2, 3, 4])[-3:-1:-1] == [2, 3, 4]


def test_square_brackets_getter__zero_step():
    with pytest.raises(ValueError):
        assert LinkedList([1, 2, 3, 4])[-3:-1:0] == [2, 3, 4]


def test_square_brackets_getter__negative_start_stop():
    assert LinkedList([1, 2, 3, 4])[-3:-1] == [2, 3, 4]


def test_square_brackets_getter__above_len_start_stop_step():
    assert LinkedList([1, 2, 3, 4])[100:100:100] == []


def test_square_brackets_setter__empty_linked_list():
    ll = LinkedList[int]()
    ll[0] = 100
    assert ll == LinkedList([])


def test_square_brackets_setter__single_value():
    ll = LinkedList[int]([1])
    ll[0] = 100
    assert ll == LinkedList([100])


def test_square_brackets_setter__single_value_negative_index():
    ll = LinkedList([1, 5])
    ll[-1] = 100
    assert ll == LinkedList([1, 100])


def test_square_brackets_setter__slice():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll[0:5] = 100
    assert ll == LinkedList([100, 100, 100, 100, 100])


def test__del__single_delete():
    ll = LinkedList([1, 2, 3, 4, 5])
    del ll[0]
    assert ll == LinkedList([2, 3, 4, 5])


def test__del__negative_index():
    ll = LinkedList([2, 3, 4, 5])
    del ll[-1]
    assert ll == LinkedList([2, 3, 4])


def test__del__slice_delete():
    ll = LinkedList([1, 2, 3, 4, 5])
    del ll[1:3]
    assert ll == LinkedList([1, 4, 5])


def test_str_method(linked_list: LinkedList[int]):
    assert (
        str(linked_list)
        == f"LinkedList(head=[{linked_list.head!s}], tail=[{linked_list.tail!s}], len=[{linked_list.length}])"
    )


def test_repr_method(linked_list: LinkedList[int]):
    assert (
        repr(linked_list)
        == f"LinkedList(head=[{linked_list.head!s}], tail=[{linked_list.tail!s}], len=[{linked_list.length}])"
    )
