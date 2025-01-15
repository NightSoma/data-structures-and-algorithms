from tree_search.binary_node import BinaryNode, T


# Iteration 5
def depth_first_delete(head: BinaryNode[T] | None, needle: T) -> bool:
    if head is None:
        return False

    if head.value == needle:
        replacement_node = find_replacement(head)
        if replacement_node is not None:
            head.value = replacement_node.value
        del head
        return True

    node_to_delete, parent_of_deleted = find_node_to_delete(head, needle, parent=None)
    if node_to_delete is None or parent_of_deleted is None:
        return False

    replacement_node = find_replacement(node_to_delete)

    if parent_of_deleted.right is node_to_delete:
        parent_of_deleted.right = replacement_node
    elif parent_of_deleted.left is node_to_delete:
        parent_of_deleted.left = replacement_node

    if replacement_node is not None:
        if node_to_delete.left is not replacement_node:
            replacement_node.left = node_to_delete.left
        if node_to_delete.right is not replacement_node:
            replacement_node.right = node_to_delete.right

    del node_to_delete
    return True


def find_node_to_delete(
    head: BinaryNode[T] | None, needle: T, parent: BinaryNode[T] | None
) -> tuple[BinaryNode[T] | None, BinaryNode[T] | None]:
    if head is None:
        return None, None

    if needle < head.value:
        return find_node_to_delete(head.left, needle, head)
    if needle > head.value:
        return find_node_to_delete(head.right, needle, head)

    return head, parent


def find_replacement(node_to_delete: BinaryNode[T]) -> BinaryNode[T] | None:
    replacement_node = None

    if node_to_delete.right is not None:
        replacement_node, _ = find_replacement_move_left(
            node_to_delete.right, node_to_delete
        )
    elif node_to_delete.left is not None:
        replacement_node, _ = find_replacement_move_right(
            node_to_delete.left, node_to_delete
        )

    return replacement_node


def find_replacement_move_left(
    head: BinaryNode[T], parent: BinaryNode[T]
) -> tuple[BinaryNode[T], BinaryNode[T]]:
    if head.left is not None:
        return find_replacement_move_left(head.left, head)

    if head.right is not None:
        parent.left = head.right
    elif parent.left is head:
        parent.left = None

    return head, parent


def find_replacement_move_right(
    head: BinaryNode[T], parent: BinaryNode[T]
) -> tuple[BinaryNode[T], BinaryNode[T]]:
    if head.right is not None:
        return find_replacement_move_right(head.right, head)

    if head.left is not None:
        parent.right = head.left
    elif parent.right is head:
        parent.right = None

    return head, parent


# Iteration 4
# def depth_first_delete(head: BinaryNode[T] | None, needle: T) -> bool:
#     if head is None:
#         return False

#     if head.value == needle:
#         replacement_node = find_replacement(head)
#         if replacement_node is not None:
#             head.value = replacement_node.value
#         del head
#         return True

#     node_to_delete, parent_of_deleted = find_node_to_delete(head, needle, parent=None)
#     if node_to_delete is None or parent_of_deleted is None:
#         return False

#     replacement_node = find_replacement(node_to_delete)

#     attach_replacement_to_parent_of_deleted(
#         node_to_delete, parent_of_deleted, replacement_node
#     )

#     if replacement_node is not None:
#         if node_to_delete.left is not replacement_node:
#             replacement_node.left = node_to_delete.left
#         if node_to_delete.right is not replacement_node:
#             replacement_node.right = node_to_delete.right

#     del node_to_delete
#     return True


# def attach_replacement_to_parent_of_deleted(
#     node_to_delete: BinaryNode[T],
#     parent_of_deleted: BinaryNode[T],
#     replacement_node: BinaryNode[T] | None,
# ) -> None:
#     if (
#         parent_of_deleted.right is not None
#         and parent_of_deleted.right is node_to_delete
#     ):
#         parent_of_deleted.right = replacement_node
#     elif (
#         parent_of_deleted.left is not None and parent_of_deleted.left is node_to_delete
#     ):
#         parent_of_deleted.left = replacement_node


# def find_node_to_delete(
#     head: BinaryNode[T] | None, needle: T, parent: BinaryNode[T] | None
# ) -> tuple[BinaryNode[T] | None, BinaryNode[T] | None]:
#     if head is None:
#         return None, None

#     if head.value == needle:
#         return head, parent

#     node, parent = find_node_to_delete(head.left, needle, head)

#     if node is None:
#         node, parent = find_node_to_delete(head.right, needle, head)

#     return node, parent


# def find_replacement(node_to_delete: BinaryNode[T]) -> BinaryNode[T] | None:
#     replacement_node = None

#     if node_to_delete.right is not None:
#         replacement_node, _ = find_replacement_move_left(
#             node_to_delete.right, node_to_delete
#         )
#     elif node_to_delete.left is not None:
#         replacement_node, _ = find_replacement_move_right(
#             node_to_delete.left, node_to_delete
#         )

#     return replacement_node


# def find_replacement_move_left(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> tuple[BinaryNode[T], BinaryNode[T]]:
#     if head.left is not None:
#         return find_replacement_move_left(head.left, head)

#     if head.right is not None:
#         parent.left = head.right
#     elif parent.left is head:
#         parent.left = None

#     return head, parent


# def find_replacement_move_right(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> tuple[BinaryNode[T], BinaryNode[T]]:
#     if head.right is not None:
#         return find_replacement_move_right(head.right, head)

#     if head.left is not None:
#         parent.right = head.left
#     elif parent.right is head:
#         parent.right = None

#     return head, parent


# Iteration 3
# def depth_first_delete(head: BinaryNode[T] | None, needle: T) -> bool:
#     if head is None:
#         return False

#     if head.value == needle:
#         node_to_delete = head
#         delete_parent = None
#     else:
#         node_to_delete, delete_parent = find_node_to_delete(head, needle, parent=None)
#         if node_to_delete is None:
#             return False

#     if node_to_delete.right is not None:
#         replacement_node = find_replacement_move_left(
#             node_to_delete.right, node_to_delete
#         )
#     elif node_to_delete.left is not None:
#         replacement_node = find_replacement_move_right(
#             node_to_delete.left, node_to_delete
#         )
#     else:
#         replacement_node = None

#     if delete_parent is not None:
#         if delete_parent.right is not None and delete_parent.right is node_to_delete:
#             delete_parent.right = replacement_node
#         elif delete_parent.left is not None and delete_parent.left is node_to_delete:
#             delete_parent.left = replacement_node

#     if replacement_node is None:
#         del node_to_delete
#         return True

#     if node_to_delete is head:
#         node_to_delete.value = replacement_node.value
#         return True

#     if node_to_delete.left is not replacement_node:
#         replacement_node.left = node_to_delete.left
#     if node_to_delete.right is not replacement_node:
#         replacement_node.right = node_to_delete.right

#     del node_to_delete

#     return True


# def find_node_to_delete(
#     head: BinaryNode[T], needle: T, parent: BinaryNode[T] | None
# ) -> tuple[BinaryNode[T] | None, BinaryNode[T] | None]:
#     if head.value == needle:
#         return head, parent

#     if head.left is not None:
#         node, parent = find_node_to_delete(head.left, needle, head)
#         if node is not None:
#             return node, parent
#     if head.right is not None:
#         node, parent = find_node_to_delete(head.right, needle, head)
#         if node is not None:
#             return node, parent

#     return None, None


# def find_replacement_move_right(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> BinaryNode[T]:
#     if head.right is not None:
#         return find_replacement_move_right(head.right, head)
#     if head.left is not None:
#         parent.right = head.left
#     if parent.right is head:
#         parent.right = None
#     else:
#         parent.left = None
#     return head


# def find_replacement_move_left(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> BinaryNode[T]:
#     if head.left is not None:
#         return find_replacement_move_left(head.left, head)
#     if head.right is not None:
#         parent.left = head.right
#     if parent.right is head:
#         parent.right = None
#     else:
#         parent.left = None
#     return head


# Iteration 2
# def depth_first_delete(head: BinaryNode[T] | None, needle: T) -> bool:
#     if head is None:
#         return False

#     if head.value == needle:
#         node_to_delete = head
#         delete_parent = None
#     else:
#         node_to_delete, delete_parent = find_node_to_delete(head, needle, parent=None)
#         if node_to_delete is None:
#             return False

#     if node_to_delete.right is not None:
#         replacement_node = find_replacement_move_left(
#             node_to_delete.right, node_to_delete
#         )
#     elif node_to_delete.left is not None:
#         replacement_node = find_replacement_move_right(
#             node_to_delete.left, node_to_delete
#         )
#     else:
#         replacement_node = None

#     if delete_parent is not None:
#         if delete_parent.right is not None and delete_parent.right is node_to_delete:
#             delete_parent.right = replacement_node
#         elif delete_parent.left is not None and delete_parent.left is node_to_delete:
#             delete_parent.left = replacement_node

#     if replacement_node is None:
#         del node_to_delete
#         return True

#     if node_to_delete is head:
#         node_to_delete.value = replacement_node.value
#         return True

#     if node_to_delete.left is not replacement_node:
#         replacement_node.left = node_to_delete.left
#     if node_to_delete.right is not replacement_node:
#         replacement_node.right = node_to_delete.right

#     del node_to_delete

#     return True


# def find_node_to_delete(
#     head: BinaryNode[T], needle: T, parent: BinaryNode[T] | None
# ) -> tuple[BinaryNode[T] | None, BinaryNode[T] | None]:
#     if head.value == needle:
#         return head, parent

#     if head.left is not None:
#         node, parent = find_node_to_delete(head.left, needle, head)
#         if node is not None:
#             return node, parent
#     if head.right is not None:
#         node, parent = find_node_to_delete(head.right, needle, head)
#         if node is not None:
#             return node, parent

#     return None, None


# def find_replacement_move_right(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> BinaryNode[T]:
#     if head.right is not None:
#         return find_replacement_move_right(head.right, head)
#     if head.left is not None:
#         parent.right = head.left
#     if parent.right is head:
#         parent.right = None
#     else:
#         parent.left = None
#     return head


# def find_replacement_move_left(
#     head: BinaryNode[T], parent: BinaryNode[T]
# ) -> BinaryNode[T]:
#     if head.left is not None:
#         return find_replacement_move_left(head.left, head)
#     if head.right is not None:
#         parent.left = head.right
#     if parent.right is head:
#         parent.right = None
#     else:
#         parent.left = None
#     return head


# Iteration 1
# def depth_first_delete(head: BinaryNode[T] | None, needle: T) -> bool:
#     if head is None:
#         return False

#     node_to_delete, delete_parent, side = find_node_to_delete(
#         head, needle, parent=None, side="None"
#     )
#     if node_to_delete is None:
#         return False

#     if node_to_delete.right is not None:
#         replacement_node = find_replacement(node_to_delete.right, False, node_to_delete)
#     elif node_to_delete.left is not None:
#         replacement_node = find_replacement(node_to_delete.left, True, node_to_delete)
#     else:
#         if delete_parent is not None:
#             if side == "left":
#                 delete_parent.left = None
#             elif side == "right":
#                 delete_parent.right = None
#         del node_to_delete
#         return True
#     if node_to_delete is head:
#         node_to_delete.value = replacement_node.value
#         return True

#     if delete_parent is not None:
#         if delete_parent.right is not None and delete_parent.right is node_to_delete:
#             delete_parent.right = replacement_node
#         elif delete_parent.left is not None and delete_parent.left is node_to_delete:
#             delete_parent.left = replacement_node

#     if node_to_delete.left is not replacement_node:
#         replacement_node.left = node_to_delete.left
#     if node_to_delete.right is not replacement_node:
#         replacement_node.right = node_to_delete.right

#     del node_to_delete

#     return True


# def find_node_to_delete(
#     head: BinaryNode[T], needle: T, parent: BinaryNode[T] | None, side: str
# ) -> tuple[BinaryNode[T] | None, BinaryNode[T] | None, str]:
#     if head.value == needle:
#         return head, parent, side

#     if head.left is not None:
#         node, parent, side = find_node_to_delete(head.left, needle, head, side="left")
#         if node is not None:
#             return node, parent, side
#     if head.right is not None:
#         node, parent, side = find_node_to_delete(head.right, needle, head, side="right")
#         if node is not None:
#             return node, parent, side

#     return None, None, "none"


# def find_replacement(
#     head: BinaryNode[T], move_right: bool, parent: BinaryNode[T]
# ) -> BinaryNode[T]:
#     if move_right:
#         if head.right is not None:
#             return find_replacement(head.right, move_right, head)
#         if head.left is not None:
#             parent.right = head.left
#         return head

#     if head.left is not None:
#         return find_replacement(head.left, move_right, head)
#     if head.right is not None:
#         parent.left = head.right
#     return head
