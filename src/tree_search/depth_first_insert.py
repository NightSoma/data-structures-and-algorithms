from tree_search.binary_node import BinaryNode, T


def depth_first_insert(head: BinaryNode[T] | None, value: T) -> None:
    if head is None:
        raise ValueError("Cannot insert into None tree")

    if value <= head.value:
        if head.left is None:
            head.left = BinaryNode(value)
        else:
            depth_first_insert(head.left, value)
    elif value > head.value:
        if head.right is None:
            head.right = BinaryNode(value)
        else:
            depth_first_insert(head.right, value)
