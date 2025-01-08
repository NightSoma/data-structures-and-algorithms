from typing import Any


def binary_search(arr: list[Any], elem: float | int) -> int:
    if not arr:
        return -1

    low = 0
    high = len(arr)
    while low < high:
        divider = (high + low) // 2
        divider_num = arr[divider]

        if elem < divider_num:
            high = divider
        elif elem > divider_num:
            low = divider + 1
        else:
            return divider
    return -1
