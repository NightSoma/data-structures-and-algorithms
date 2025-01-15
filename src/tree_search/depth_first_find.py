from tree_search.binary_node import BinaryNode, T


def depth_first_find(head: BinaryNode[T] | None, needle: T) -> bool:
    if head is None:
        return False

    if needle == head.value:
        return True

    if needle < head.value:
        return depth_first_find(head.left, needle)

    return depth_first_find(head.right, needle)
