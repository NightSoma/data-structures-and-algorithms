from collections.abc import Generator, Reversible
from typing import Any


class DoubleLinkedListTools:
    @staticmethod
    def validate_index(index: int, length: int) -> None:
        if index != 0 and (index < 0 or index >= length):
            raise ValueError("Index is out of bounds.")

    @staticmethod
    def get_nodes_slice_generator(
        iterator: Reversible[Any], slice_obj: slice, length: int
    ) -> Generator[Any]:
        """Generate elements from iterator based on slice parameters."""
        step = slice_obj.step if slice_obj.step is not None else 1
        if step == 0:
            raise ValueError("slice step cannot be zero")

        def _normalize_index(idx: int | None, default: int) -> int:
            if idx is None:
                return default
            return idx + length if idx < 0 else idx

        if step > 0:
            idx_increment = 1
            start = _normalize_index(slice_obj.start, 0)
            stop = _normalize_index(slice_obj.stop, length)
            it = iterator
            idx = 0
            start_step = start % step
        else:
            idx_increment = -1
            start = _normalize_index(slice_obj.start, length)
            stop = _normalize_index(slice_obj.stop, 0)
            it = reversed(iterator)
            idx = length - 1
            start, stop = stop + 1, start + 1
            start_step = stop % step

        for element in it:
            if start <= idx < stop and idx % step == start_step:
                yield element
            elif stop <= idx:
                return
            idx += idx_increment
