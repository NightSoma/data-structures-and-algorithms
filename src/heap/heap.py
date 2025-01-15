from collections.abc import Callable, Sequence
from typing import Generic

from tree_search.binary_node import T


class MinHeap(Generic[T]):
    def __init__(
        self,
        from_container: Sequence[T] | None = None,
        key: Callable[[T, T], bool] = lambda x, y: x <= y,
    ):
        self.key = key
        self.heap: list[T] = []

        if from_container is not None:
            self.heap = list(from_container)
            self._heapify()

    def _heapify(self) -> None:
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._move_down(i)

    def push(self, item: T) -> None:
        self.heap.append(item)
        pushed_idx = len(self.heap) - 1
        self._move_up(pushed_idx)

    def _move_up(self, pushed_idx: int) -> None:
        parent_index = (pushed_idx - 1) // 2
        while pushed_idx > 0 and self.key(
            self.heap[pushed_idx], self.heap[parent_index]
        ):
            self.heap[pushed_idx], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[pushed_idx],
            )
            pushed_idx = parent_index
            parent_index = (pushed_idx - 1) // 2

    def pop(self) -> T:
        if not self.heap:
            raise ValueError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        result = self.heap[0]
        self.heap[0] = self.heap.pop()
        parent_idx = 0
        self._move_down(parent_idx)

        return result

    def _move_down(self, parent_idx: int):
        length = len(self.heap)
        while True:
            left_idx = parent_idx * 2 + 1
            right_idx = parent_idx * 2 + 2
            smallest_idx = parent_idx

            if left_idx < length and self.key(
                self.heap[left_idx], self.heap[smallest_idx]
            ):
                smallest_idx = left_idx

            if right_idx < length and self.key(
                self.heap[right_idx], self.heap[smallest_idx]
            ):
                smallest_idx = right_idx

            if smallest_idx == parent_idx:
                break

            self.heap[parent_idx], self.heap[smallest_idx] = (
                self.heap[smallest_idx],
                self.heap[parent_idx],
            )
            parent_idx = smallest_idx

    def __len__(self) -> int:
        return len(self.heap)
