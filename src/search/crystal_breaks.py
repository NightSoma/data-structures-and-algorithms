import math


def crystal_break_at(arr: list[bool]) -> int:
    if not arr:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] else -1

    low = 0
    high = len(arr) - 1
    while True:
        index = (low + high) // 2
        value = arr[index]
        next_index = index + 1
        next_value = arr[index + 1]

        if value != next_value:
            return next_index

        if value:
            high = index
        else:
            low = next_index

        if high == low:
            if value:
                return 0
            return -1


def crystal_break_at_isqrt(arr: list[bool]) -> int:
    if not arr:
        return -1

    step = math.isqrt(len(arr))
    for i in range(0, len(arr), step):
        if arr[i]:
            for j in range(i - 1, -1, -1):
                if not arr[j]:
                    return j + 1
            return 0
    return -1
