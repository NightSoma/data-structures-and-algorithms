from tree_search.binary_node import BinaryNode, T


def deapth_first_search(head: BinaryNode[T] | None, needle: T) -> bool:
    if head is None:
        return False
    if head.value == needle:
        return True
    return deapth_first_search(head.left, needle) or deapth_first_search(
        head.right, needle
    )
