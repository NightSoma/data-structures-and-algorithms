from tree_search.binary_node import BinaryNode, T


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
