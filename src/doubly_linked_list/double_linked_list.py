"""Linked List one directional."""

from collections.abc import Generator, Iterator, Sequence
from typing import Generic

from .double_linked_list_tools import DoubleLinkedListTools
from .double_node import DoubleNode, T


class DoubleLinkedList(Generic[T]):
    """Linked List."""

    def __init__(self, other_container: Sequence[T] | None = None) -> None:
        """Create Linked List, where nodes only have reference to next node.

        Args:
            other_container (Sequence[T] | None, optional): Can initialize from other container. Defaults to None.
        """
        self.length: int = 0
        self.head: DoubleNode[T] | None = None
        self.tail: DoubleNode[T] | None = None

        if other_container is not None:
            for item in other_container:
                self.append(item)

    def __len__(self) -> int:
        """Length of Linked List.

        Returns:
            int: Number of nodes.
        """
        return self.length

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            raise NotImplementedError
        if other.length != self.length:
            return False
        return (
            all(node1 == node2 for node1, node2 in zip(self, other, strict=False))
            and self.length == other.length
            and self.head == other.head
            and self.tail == other.tail
        )

    def __iter__(self) -> Generator[DoubleNode[T]]:
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __reversed__(self) -> Generator[DoubleNode[T]]:
        """This method is called by the reversed() function."""
        current = self.tail
        while current is not None:
            yield current
            current = current.prev

    def find_closer_iterator(self, index: int) -> Iterator[DoubleNode[T]]:
        return iter(self) if index < self.length - 1 - index else reversed(self)

    def find_closer_enumerate(self, index: int) -> Generator[tuple[int, DoubleNode[T]]]:
        last_elem_idx = self.length - 1
        if index < self.length - 1 - index:
            for idx, node in enumerate(reversed(self)):
                yield last_elem_idx - idx, node
        else:
            for idx, node in enumerate(self):
                yield idx, node

    def insert_head(self, item: T) -> None:
        node = DoubleNode(item, prev_node=None, next_node=self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.length += 1

    def insert_at(self, item: T, index: int) -> None:
        DoubleLinkedListTools.validate_index(index, self.length)
        for idx, node in self.find_closer_enumerate(index):
            if idx == index:
                if node.prev is None:
                    self.insert_head(item)
                    return
                new_node = DoubleNode(item, prev_node=node.prev, next_node=node)
                node.prev.next = new_node

                self.length += 1

    def reverse(self) -> None:
        self.head, self.tail = self.tail, self.head
        for node in self:
            node.prev, node.next = node.next, node.prev

    def find_item_index(self, item: T) -> int | None:
        for idx, node in enumerate(self):
            if node.item == item:
                return idx
        return None

    def remove_head(self) -> T | None:
        if self.head is None:
            return None

        node_to_del = self.head
        deleted_item = self.head.item
        self.head = self.head.next
        del node_to_del
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return deleted_item

    def remove_node(self, node_to_del: DoubleNode[T]) -> T | None:
        prev_node = node_to_del.prev
        next_node = node_to_del.next

        if node_to_del is self.head:
            self.head = next_node
        if node_to_del is self.tail:
            self.tail = prev_node

        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node

        self.length -= 1
        deleted_item = node_to_del.item
        del node_to_del
        return deleted_item

    def remove(self, item: T) -> T | None:
        for node in self:
            if node.item == item:
                return self.remove_node(node_to_del=node)

        return None

    def remove_at(self, index: int) -> T | None:
        DoubleLinkedListTools.validate_index(index, self.length)

        for idx, node in self.find_closer_enumerate(index):
            if idx == index:
                return self.remove_node(node_to_del=node)

        return None

    def append(self, item: T) -> None:
        new_node = DoubleNode(item, prev_node=None, next_node=None)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.tail is None:
            self.tail = self.head
            for node in self:
                self.tail = node
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def get_node(self, index: int) -> DoubleNode[T] | None:
        DoubleLinkedListTools.validate_index(index, self.length)

        for idx, node in self.find_closer_enumerate(index):
            if index == idx:
                return node

        return None

    def get_item(self, index: int) -> T | None:
        node = self.get_node(index)
        if node is None:
            return None
        return node.item

    def __getitem__(self, key: int | slice) -> list[T] | T | None:
        if isinstance(key, slice):
            return [
                node.item
                for node in DoubleLinkedListTools.get_nodes_slice_generator(
                    self, key, self.length
                )
            ]

        if key < 0:
            key = self.length + key

        return self.get_item(key)

    def __setitem__(self, key: int | slice, value: T) -> None:
        if isinstance(key, slice):
            for node in DoubleLinkedListTools.get_nodes_slice_generator(
                self, key, self.length
            ):
                node.item = value
            return

        if key < 0:
            key = self.length + key
        node = self.get_node(key)
        if node is None:
            return
        node.item = value

    def __delitem__(self, key: int | slice) -> None:
        if isinstance(key, slice):
            for node in DoubleLinkedListTools.get_nodes_slice_generator(
                self, key, self.length
            ):
                self.remove_node(node)
            return

        if key < 0:
            key = self.length + key
        self.remove_at(key)

    def __str__(self) -> str:
        """String representaion of Linked List instance."""
        return f"LinkedList(head=[{self.head!s}], tail=[{self.tail!s}], len=[{self.length}])"

    def __repr__(self) -> str:
        """String representaion of Linked List instance.

        Suatable for debbuging.
        """
        return f"LinkedList(head=[{self.head!r}], tail=[{self.tail!r}], len=[{self.length}])"
