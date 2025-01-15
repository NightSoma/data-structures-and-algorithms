from tree_search.binary_node import BinaryNode, T


def depth_first_search(head: BinaryNode[T] | None, needle: T) -> bool:
    if head is None:
        return False
    if head.value == needle:
        return True
    return depth_first_search(head.left, needle) or depth_first_search(
        head.right, needle
    )
