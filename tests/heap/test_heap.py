import random

import pytest

from heap.heap import MinHeap


def test_push():
    min_heap = MinHeap[int]()
    assert min_heap.push(4) is None
    min_heap.push(1)
    min_heap.push(3)
    min_heap.push(2)
    assert min_heap.heap == [1, 2, 3, 4]


def test_pop():
    min_heap = MinHeap[int]()
    min_heap.heap = [1, 2, 3, 4]
    assert min_heap.pop() == 1
    assert min_heap.pop() == 2
    assert min_heap.pop() == 3
    assert min_heap.pop() == 4
    assert min_heap.heap == []


def test_everything():
    min_heap = MinHeap[int]([453, 724, 323, 734])
    assert min_heap.pop() == 323
    min_heap.push(0)
    assert min_heap.pop() == 0
    min_heap.push(1000)

    assert min_heap.pop() == 453
    assert min_heap.pop() == 724
    assert min_heap.pop() == 734
    assert min_heap.pop() == 1000
    with pytest.raises(ValueError):
        min_heap.pop()


def test_large_amount_of_values():
    ls = [random.randint(-10000, 10000) for _ in range(10000)]
    sorted_container = sorted(ls)

    from_push = MinHeap[int]()
    for val in ls:
        from_push.push(val)
    from_pop = [from_push.pop() for _ in range(10000)]
    assert sorted_container == from_pop

    from_container = MinHeap[int](ls)
    from_pop = [from_container.pop() for _ in range(10000)]
    assert sorted_container == from_pop


def test__init__from_container():
    min_heap = MinHeap[int]([4, 3, 2, 1])
    assert min_heap.heap == [1, 3, 2, 4]


def test__len__():
    min_heap = MinHeap[int]([4, 3, 2, 1])
    assert len(min_heap.heap) == len(min_heap)


def test_pop__empty_heap():
    with pytest.raises(ValueError):
        MinHeap[int]().pop()
