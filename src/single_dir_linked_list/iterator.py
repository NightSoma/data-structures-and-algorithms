from typing import Generic

from .node import Node, T


class LinkedListIterator(Generic[T]):
    def __init__(self):
        self.current: Node[T] | None = None
        self.start = 0
        self.step = 1
        self.deque = []

    # def get_nodes_slice(self, key: slice) -> list[Node[T]]:
    #     result_list: list[Node[T]] = []

    #     start = key.start
    #     if start is None:
    #         start = 0
    #     elif start < 0:
    #         start = self.length + key.start
    #     elif start > self.length:
    #         start = self.length

    #     stop = key.stop
    #     if stop is None:
    #         stop = self.length
    #     elif stop < 0:
    #         stop = self.length + key.stop + 1
    #     elif stop > self.length:
    #         stop = self.length

    #     step = key.step
    #     if step is None:
    #         step = 1

    #     if start > stop:
    #         raise ValueError("Expensive operation!")

    #     start_step = start % step
    #     for idx, node in enumerate(self):
    #         if start <= idx < stop and idx % step == start_step:
    #             result_list.append(node)
    #         elif stop <= idx:
    #             return result_list
    #     return result_list

    # def __iter__(
    #     self, start_node: Node[T] | None, start: int, step: int
    # ) -> "LinkedListIterator[T]":
    #     self.current = start_node
    #     self.start = start
    #     self.step = step

    #     for _ in range(0, self.start):
    #         if self.current is None:
    #             break
    #         self.current = self.current.next

    #     return self

    # def __next__(self) -> Node[T]:
    #     if self.current is None:
    #         raise StopIteration
    #     node = self.current

    #     for _ in range(self.step):
    #         if self.current is None:
    #             break
    #         self.current = self.current.next

    #     return node
