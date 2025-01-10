from tree_search.binary_node import BinaryNode, T


def tree_compare(
    tree_1_node: BinaryNode[T] | None, tree_2_node: BinaryNode[T] | None
) -> bool:
    if tree_1_node is None and tree_2_node is None:
        return True
    if tree_1_node is None or tree_2_node is None:
        return False
    if tree_1_node.value != tree_2_node.value:
        return False

    return tree_compare(tree_1_node.left, tree_2_node.left) and tree_compare(
        tree_1_node.right, tree_2_node.right
    )
