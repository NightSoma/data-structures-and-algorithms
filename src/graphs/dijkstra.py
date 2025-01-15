def dijkstra_list(
    graph: list[list[int]], source: int, sink: int
) -> tuple[list[int], list[int]] | None:
    visited: set[int] = set()
    origin: list[int] = [-1] * len(graph)
    dists = [float("inf")] * len(graph)

    dists[source] = 0
    curr = source

    while curr != -1:
        find_shorter_dist_from_curr_node(graph, origin, dists, curr)

        visited.add(curr)

        curr = find_unvisited_node(visited, dists)

    if sink not in visited:
        return None

    return constract_shortest_path(graph, source, sink, origin)


def find_shorter_dist_from_curr_node(
    graph: list[list[int]], origin: list[int], dists: list[float], curr: int
):
    for idx, weight in enumerate(graph[curr]):
        if weight == 0:
            continue
        accum_weight = dists[curr] + weight
        if dists[idx] > accum_weight:
            origin[idx] = curr
            dists[idx] = accum_weight


def constract_shortest_path(
    graph: list[list[int]], source: int, sink: int, origin: list[int]
):
    path: list[int] = []
    path_weights: list[int] = []
    curr = sink

    while source != curr:
        new_curr = origin[curr]
        path.append(curr)
        path_weights.append(graph[new_curr][curr])
        curr = new_curr
    path.append(source)

    return list(reversed(path)), list(reversed(path_weights))


def find_unvisited_node(visited: set[int], dists: list[float]):
    min_dist = float("inf")
    min_dist_idx = -1

    for idx, new_curr in enumerate(dists):
        if min_dist > new_curr and idx not in visited:
            min_dist = new_curr
            min_dist_idx = idx

    return min_dist_idx
