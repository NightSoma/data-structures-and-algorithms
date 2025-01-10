from tree_search.binary_node import BinaryNode, T


def walk_pre(curr: BinaryNode[T] | None, path: list[T]) -> None:
    if curr is None:
        return
    path.append(curr.value)
    walk_pre(curr.left, path)
    walk_pre(curr.right, path)


def pre_order_search(head: BinaryNode[T]) -> list[T]:
    path: list[T] = []
    walk_pre(head, path)
    return path


def walk_in(curr: BinaryNode[T] | None, path: list[T]) -> None:
    if curr is None:
        return

    walk_in(curr.left, path)
    path.append(curr.value)
    walk_in(curr.right, path)


def in_order_search(head: BinaryNode[T]) -> list[T]:
    path: list[T] = []
    walk_in(head, path)
    return path


def walk_post(curr: BinaryNode[T] | None, path: list[T]) -> None:
    if curr is None:
        return
    walk_post(curr.left, path)
    walk_post(curr.right, path)
    path.append(curr.value)


def post_order_search(head: BinaryNode[T]) -> list[T]:
    path: list[T] = []
    walk_post(head, path)
    return path
