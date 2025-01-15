def walk(
    graph: list[list[int]], source: int, needle: int, seen: set[int]
) -> list[int] | None:
    if source == needle:
        return [needle]
    if source in seen:
        return None
    seen.add(source)

    result = None
    for idx, weight in enumerate(graph[source]):
        if source != idx and weight != 0:
            result = walk(graph, idx, needle, seen)

            if result is not None:
                result.append(source)
                break

    return result


def depth_first_search_recursion(
    graph: list[list[int]], source: int, needle: int
) -> list[int] | None:
    seen: set[int] = set()
    result = walk(graph, source, needle, seen)
    if result:
        return list(reversed(result))
    return None


def depth_first_search_stack(
    graph: list[list[int]], source: int, needle: int
) -> list[int] | None:
    seen: set[int] = {source}
    stack: list[int] = [source]
    weigths_stack: list[int] = []

    while stack:
        source = stack[-1]
        if needle == source:
            break

        for idx, weight in enumerate(graph[source]):
            if source != idx and weight != 0 and idx not in seen:
                stack.append(idx)
                weigths_stack.append(weight)
                seen.add(idx)
                break
        else:
            stack.pop()
            if weigths_stack:
                weigths_stack.pop()
    else:
        return None
    return stack


# Versions with shortest paths search according to weights
# def walk(
#     graph: list[list[int]], source: int, needle: int, seen: set[int]
# ) -> tuple[list[int], list[int]] | None:
#     if source in seen and source != needle:
#         return None
#     seen.add(source)

#     if source == needle:
#         return [needle], []

#     results = send_walkers(graph, source, needle, seen)

#     if results:
#         return min(results, key=lambda x: sum(x[0]))

#     return None


# def send_walkers(graph: list[list[int]], source: int, needle: int, seen: set[int]):
#     results: list[tuple[list[int], list[int]]] = []

#     for idx, weight in enumerate(graph[source]):
#         if weight != 0:
#             result = walk(graph, idx, needle, seen)

#             if result is not None:
#                 result[0].append(source)
#                 result[1].append(weight)
#                 results.append(result)

#             if idx == needle:
#                 break
#     return results


# def depth_first_search_recursion(
#     graph: list[list[int]], source: int, needle: int
# ) -> tuple[list[int], list[int]] | None:
#     seen: set[int] = set()
#     result = walk(graph, source, needle, seen)
#     if result:
#         return list(reversed(result[0])), list(reversed(result[1]))
#     return None


# def depth_first_search_stack(
#     graph: list[list[int]], source: int, needle: int
# ) -> tuple[list[int], list[int]] | None:
#     seen: set[int] = {source}
#     stack: list[int] = [source]
#     weigths_stack: list[int] = []
#     paths: list[list[int]] = []
#     paths_weights: list[list[int]] = []

#     while stack:
#         source = stack[-1]
#         if needle == source:
#             paths.append(list(stack))
#             paths_weights.append(list(weigths_stack))
#             stack.pop()
#             if weigths_stack:
#                 weigths_stack.pop()

#         for idx, weight in enumerate(graph[source]):
#             if source != idx and weight != 0 and (idx not in seen or idx == needle):
#                 stack.append(idx)
#                 weigths_stack.append(weight)
#                 seen.add(idx)
#                 break
#         else:
#             stack.pop()
#             if weigths_stack:
#                 weigths_stack.pop()

#     if not paths:
#         return None

#     zipped_index_sums = zip(
#         list(range(len(paths_weights))),
#         [sum(weights) for weights in paths_weights],
#         strict=False,
#     )

#     min_path_index = min(zipped_index_sums, key=lambda x: x[1])[0]

#     return paths[min_path_index], paths_weights[min_path_index]
