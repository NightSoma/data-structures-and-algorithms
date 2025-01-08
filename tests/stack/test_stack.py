from src.stack.stack import Stack


def test_add_tail():
    stack = Stack[int]()
    stack.add_head(1)
    assert stack.head is not None
    assert stack.head.value == 1


def test_pop_head():
    stack = Stack[int]()
    stack.add_head(1)
    assert stack.pop_head() == 1


def test_pop_head__empty_stack():
    stack = Stack[int]()
    assert stack.pop_head() is None


def test_peek_head():
    stack = Stack[int]()
    stack.add_head(1)
    assert stack.peek_head() == 1


def test_peek_head__empty_stack():
    stack = Stack[int]()
    assert stack.peek_head() is None


def test__len__():
    stack = Stack[int]()
    stack.add_head(0)
    assert stack.length == 1
    stack.add_head(1)
    assert stack.length == 2
    stack.add_head(2)
    assert stack.length == 3
    stack.pop_head()
    assert stack.length == 2
    stack.pop_head()
    assert stack.length == 1
    stack.pop_head()
    assert stack.length == 0
    stack.pop_head()
    assert stack.length == 0


def test_multiple():
    stack = Stack[int]()
    stack.add_head(0)
    stack.add_head(1)
    stack.add_head(2)
    assert stack.peek_head() == 2
    assert stack.pop_head() == 2
    assert stack.pop_head() == 1
    assert stack.pop_head() == 0
    assert stack.pop_head() is None
