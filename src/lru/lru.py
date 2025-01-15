from dataclasses import dataclass
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class BinaryNode[V, K]:
    key: K
    value: V
    next: "BinaryNode[V, K] | None"
    prev: "BinaryNode[V, K] | None"


class LRU(Generic[K, V]):
    def __init__(self, max_size: int = 10):
        self.map: dict[K, BinaryNode[V, K]] = {}
        self.head: BinaryNode[V, K] | None = None
        self.tail: BinaryNode[V, K] | None = None
        self.max_size: int = max_size

    def _add(self, node: BinaryNode[V, K]) -> None:
        if self.tail is None:
            self.tail = node
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def _remove(self, node: BinaryNode[V, K]) -> None:
        if node is self.tail and self.tail is not None:
            if self.tail.prev is not None:
                self.tail.prev.next = None
            self.tail = self.tail.prev
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def update(self, key: K, value: V) -> None:
        node = None
        if key in self.map:
            node = self.map[key]

        if node is None:
            new_node = BinaryNode(key, value, self.head, None)
            self.map[key] = new_node
            self._add(new_node)
            if self.max_size < len(self.map) and self.tail is not None:
                self._remove(self.tail)
                del self.map[self.tail.key]
            return

        if node is self.head:
            self.map[key].value = value
            return
        self._remove(node)
        self._add(node)
        node.value = value

    def get(self, key: K) -> V | None:
        if key in self.map:
            node = self.map[key]

            if node is not self.head:
                self._remove(node)
                self._add(node)

            return node.value

        return None

    def __len__(self) -> int:
        return len(self.map)
