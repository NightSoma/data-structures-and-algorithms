from src.queue_.queue import Queue


def test_add_tail():
    queue = Queue[int]()
    queue.add_tail(1)
    assert queue.tail is not None
    assert queue.tail.value == 1


def test_pop_head():
    queue = Queue[int]()
    queue.add_tail(1)
    assert queue.pop_head() == 1


def test_pop_head__empty_queue():
    queue = Queue[int]()
    assert queue.pop_head() is None


def test_peek_head():
    queue = Queue[int]()
    queue.add_tail(1)
    assert queue.peek_head() == 1


def test_peek_head__empty_queue():
    queue = Queue[int]()
    assert queue.peek_head() is None


def test__len__():
    queue = Queue[int]()
    queue.add_tail(0)
    assert queue.length == 1
    queue.add_tail(1)
    assert queue.length == 2
    queue.add_tail(2)
    assert queue.length == 3
    queue.pop_head()
    assert queue.length == 2
    queue.pop_head()
    assert queue.length == 1
    queue.pop_head()
    assert queue.length == 0
    queue.pop_head()
    assert queue.length == 0


def test_multiple():
    queue = Queue[int]()
    queue.add_tail(0)
    queue.add_tail(1)
    queue.add_tail(2)
    assert queue.peek_head() == 0
    assert queue.pop_head() == 0
    assert queue.pop_head() == 1
    assert queue.pop_head() == 2
    assert queue.pop_head() is None
