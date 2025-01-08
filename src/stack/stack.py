from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: "Node[T] | None"


@dataclass
class Stack(Generic[T]):
    length: int = 0
    head: "Node[T] | None" = None

    def add_head(self, value: T) -> None:
        self.length += 1
        node = Node(value, None)
        node.next = self.head
        self.head = node

    def pop_head(self) -> T | None:
        if self.head is None:
            return None
        self.length -= 1
        value = self.head.value
        self.head = self.head.next
        return value

    def peek_head(self) -> T | None:
        if self.head is None:
            return None
        return self.head.value
