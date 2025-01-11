from ring_buffer.ring_buffer import RingBuffer
from tree_search.binary_node import BinaryNode, T


def breadth_first_search(head: BinaryNode[T], needle: T) -> bool:
    queue: RingBuffer[BinaryNode[T]] = RingBuffer([None] * 100)
    queue.push_tail(head)

    while len(queue) > 0:
        node = queue.pop_head()
        if node is None:
            continue
        if node.value == needle:
            return True
        queue.push_tail(node.left)
        queue.push_tail(node.right)

    return False
