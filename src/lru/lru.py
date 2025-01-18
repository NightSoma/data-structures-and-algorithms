from dataclasses import dataclass
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class BinaryNode[K, V]:
    key: K
    value: V
    next: "BinaryNode[K, V] | None"
    prev: "BinaryNode[K, V] | None"


class LRU(Generic[K, V]):
    def __init__(self, max_size: int = 10):
        self.map: dict[K, BinaryNode[K, V]] = {}
        self.head: BinaryNode[K, V] | None = None
        self.tail: BinaryNode[K, V] | None = None
        self.max_size: int = max_size

    def _add(self, node: BinaryNode[K, V]) -> None:
        if self.tail is None:
            self.tail = node
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def _remove(self, node: BinaryNode[K, V]) -> None:
        if node is self.tail and self.tail is not None:
            if self.tail.prev is not None:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def _find_and_move_node_if_needed(self, key: K) -> BinaryNode[K, V]:
        node = self.map[key]

        if node is not self.head:
            self._remove(node)
            self._add(node)

        return node

    def update(self, key: K, value: V) -> None:
        if key not in self.map:
            new_node = BinaryNode(key, value, self.head, None)
            self.map[key] = new_node
            self._add(new_node)
            if self.max_size < len(self.map) and self.tail is not None:
                self._remove(self.tail)
                del self.map[self.tail.key]
            return

        node = self._find_and_move_node_if_needed(key)

        node.value = value

    def get(self, key: K) -> V | None:
        if key not in self.map:
            return None

        node = self._find_and_move_node_if_needed(key)

        return node.value

    def __len__(self) -> int:
        return len(self.map)
