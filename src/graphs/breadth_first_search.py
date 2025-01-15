from collections import deque


def breadth_first_search(
    graph: list[list[int]], source: int, needle: int
) -> tuple[list[int], list[int]] | None:
    queue: deque[int] = deque([source])

    origin: list[int] = [-1] * len(graph)
    seen: set[int] = {source}

    while len(queue) > 0:
        node = queue.popleft()
        if node == needle:
            break

        for idx, weigth in enumerate(graph[node]):
            if weigth == 0:
                continue

            if idx in seen:
                continue
            seen.add(idx)

            origin[idx] = node
            queue.append(idx)
        seen.add(node)

    if needle not in seen:
        return None

    path: list[int] = []
    path_weights: list[int] = []
    curr = needle
    while source != curr:
        new_curr = origin[curr]
        path.append(curr)
        path_weights.append(graph[new_curr][curr])
        curr = new_curr
    path.append(source)

    return list(reversed(path)), list(reversed(path_weights))
