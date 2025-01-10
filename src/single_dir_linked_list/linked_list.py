"""Linked List one directional."""

from collections.abc import Generator, Sequence
from typing import Generic

from .node import Node, T


class LinkedList(Generic[T]):
    """Linked List."""

    def __init__(self, other_container: Sequence[T] | None = None) -> None:
        """Create Linked List, where nodes only have reference to next node.

        Args:
            other_container (Sequence[T] | None, optional): Can initialize from other container. Defaults to None.
        """
        self.length: int = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.next_iterated_node: Node[T] | None = None

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

    def __iter__(self) -> "LinkedList[T]":
        self.next_iterated_node = self.head
        return self

    def __next__(self) -> Node[T]:
        if self.next_iterated_node is None:
            raise StopIteration

        current_node = self.next_iterated_node
        self.next_iterated_node = self.next_iterated_node.next

        return current_node

    def insert_at_head(self, item: T) -> None:
        self.head = Node(item, self.head)
        self.length += 1

    def insert_at(self, item: T, index: int) -> None:
        self._validate_index(index)
        prev = None
        for idx, node in enumerate(self):
            if idx == index:
                if prev is None:
                    self.insert_at_head(item)
                    return

                prev.next = Node(item, node)
                self.length += 1

            prev = node

    def reverse(self) -> "LinkedList[T]":
        return LinkedList(list(reversed([node.item for node in self])))

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

    def _remove_node(self, prev_node: Node[T] | None, node_to_del: Node[T]) -> T | None:
        if node_to_del is self.head:
            self.head = node_to_del.next
        if node_to_del is self.tail:
            self.tail = prev_node
        if prev_node is not None:
            prev_node.next = node_to_del.next

        self.length -= 1
        deleted_item = node_to_del.item
        del node_to_del
        return deleted_item

    def remove(self, item: T) -> T | None:
        prev_node = None
        for node in self:
            if node.item == item:
                return self._remove_node(prev_node=prev_node, node_to_del=node)

            prev_node = node
        return None

    def remove_at(self, index: int) -> T | None:
        self._validate_index(index)

        prev_node = None
        for idx, node in enumerate(self):
            if idx == index:
                return self._remove_node(prev_node=prev_node, node_to_del=node)

            prev_node = node
        return None

    def append(self, item: T) -> None:
        new_node = Node(item, next_node=None)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.tail is None:
            self.tail = self.head
            for node in self:
                self.tail = node

        self.tail.next = new_node
        self.tail = new_node

    def get_node(self, index: int) -> Node[T] | None:
        self._validate_index(index)

        for idx, node in enumerate(self):
            if index == idx:
                return node

        return None

    def get(self, index: int) -> T | None:
        node = self.get_node(index)
        if node is None:
            return None
        return node.item

    def _validate_index(self, index: int) -> None:
        if index != 0 and (index < 0 or index >= self.length):
            raise ValueError("Index is out of bounds.")

    @staticmethod
    def _slice_adapter(_slice: slice, length: int) -> tuple[int, int, int]:
        start = _slice.start
        if start is None:
            start = 0
        elif start < 0:
            start = length + _slice.start
        elif start > length:
            start = length

        stop = _slice.stop
        if stop is None:
            stop = length
        elif stop < 0:
            stop = length + _slice.stop + 1
        elif stop > length:
            stop = length

        step = _slice.step
        if step is None:
            step = 1
        elif step <= 0:
            raise ValueError("Step can't be 0 or lower!")

        if start > stop:
            raise ValueError("Expensive operation!")

        return start, stop, step

    def _get_nodes_slice(self, key: slice) -> Generator[tuple[Node[T] | None, Node[T]]]:
        start, stop, step = LinkedList._slice_adapter(_slice=key, length=self.length)

        prev_node = None
        start_step = start % step
        for idx, node in enumerate(self):
            if start <= idx < stop and idx % step == start_step:
                yield prev_node, node
            elif stop <= idx:
                return
            else:
                prev_node = node

    def __getitem__(self, key: int | slice) -> list[T] | T | None:
        if isinstance(key, slice):
            return [node[1].item for node in self._get_nodes_slice(key)]

        if key < 0:
            key = self.length + key

        return self.get(key)

    def __setitem__(self, key: int | slice, value: T) -> None:
        if isinstance(key, slice):
            for _, node in self._get_nodes_slice(key):
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
            for prev_node, node in self._get_nodes_slice(key):
                self._remove_node(prev_node, node)
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
        return f"LinkedList(head=[{self.head!s}], tail=[{self.tail!s}], len=[{self.length}])"
