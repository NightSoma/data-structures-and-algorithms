import pytest

from ring_buffer.ring_buffer import RingBuffer


def test_ring_buffer__pop_empty_buffer_error():
    with pytest.raises(ValueError):
        ring_buffer = RingBuffer[int]()
        ring_buffer.pop_head()


def test_ring_buffer__max_capacity_error():
    with pytest.raises(ValueError):
        ring_buffer = RingBuffer[int]()
        assert ring_buffer.push_tail(0)


def test_ring_buffer__tail_behind_head():
    ring_buffer = RingBuffer[int]([None] * 3)
    ring_buffer.push_tail(0)
    ring_buffer.push_tail(1)
    ring_buffer.push_tail(2)
    assert ring_buffer.pop_head() == 0
    assert ring_buffer.pop_head() == 1
    ring_buffer.push_tail(3)
    assert ring_buffer.pop_head() == 2
    assert ring_buffer.pop_head() == 3
