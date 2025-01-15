from lru.lru import LRU


def test__update__adding_values():
    lru = LRU[str, int](3)

    lru.update("five", 5)
    assert lru.head is not None
    assert lru.head.value == 5
    lru.update("four", 4)
    lru.update("three", 3)
    assert lru.head is not None
    assert lru.head.value == 3
    lru.update("two", 2)

    assert lru.head is not None
    assert lru.head.value == 2
    assert lru.tail is not None
    assert lru.tail.value == 4


def test__update__max_size_limit():
    lru = LRU[str, int](3)

    lru.update("five", 5)
    lru.update("four", 4)
    lru.update("three", 3)
    lru.update("two", 2)

    assert len(lru) == 3


def test__update__updating_values():
    lru = LRU[str, int](3)

    lru.update("apple", 5)
    lru.update("banana", 6)
    lru.update("pineapple", 4)
    lru.update("strawberry", 1)
    lru.update("banana", 1)
    lru.update("strawberry", 2)
    lru.update("strawberry", 2)

    assert len(lru) == 3
    assert lru.head is not None
    assert lru.head.value == 2
    assert lru.tail is not None
    assert lru.tail.value == 4


def test__get__key_exist():
    lru = LRU[str, int](3)

    lru.update("apple", 5)
    lru.update("banana", 6)
    lru.update("pineapple", 4)

    assert lru.get("apple") == 5
    assert lru.head is not None
    assert lru.head.value == 5
    assert lru.tail is not None
    assert lru.tail.value == 6

    assert lru.get("apple") == 5
    assert lru.head is not None
    assert lru.head.value == 5
    assert lru.tail is not None
    assert lru.tail.value == 6


def test__get__key_not_exist():
    lru = LRU[str, int](3)

    lru.update("apple", 5)

    assert lru.get("water") is None
