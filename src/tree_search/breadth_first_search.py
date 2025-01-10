from tree_search.binary_node import BinaryNode, T
from ring_buffer.ring_buffer import RingBuffer


def breadth_first_search_traversal(head: BinaryNode[T]) -> list[T]:
    queue: list[BinaryNode[T]] = [head]
    idx = 0
    while len(queue) > idx:
        node = queue[idx]
        idx += 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return [node.value for node in queue]


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
