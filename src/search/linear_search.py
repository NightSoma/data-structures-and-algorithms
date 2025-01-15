from typing import Any


def linear_search(arr: list[Any], elem: Any) -> int:
    for i, e in enumerate(arr):
        if elem == e:
            return i
    return -1


def linear_search_bool(arr: list[Any], elem: Any) -> bool:
    for e in arr:
        if elem == e:
            return True
    return False
