def runner_path_builder(
    seen: set[tuple[int, int]],
    maze: list[str],
    path: list[tuple[int, int]],
    current_pos: tuple[int, int],
    end_tile: str,
) -> list[tuple[int, int]]:
    if current_pos in seen:
        return []
    if not (
        0 <= current_pos[0] < len(maze)
        and 0 <= current_pos[1] < len(maze[current_pos[0]])
    ):
        return []
    if maze[current_pos[0]][current_pos[1]] == "#":
        return []
    if maze[current_pos[0]][current_pos[1]] == end_tile:
        return path

    seen.add(current_pos)
    results: list[list[tuple[int, int]]] = []
    for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_pos = (current_pos[0] + pos[0], current_pos[1] + pos[1])
        result = runner_path_builder(
            seen=seen,
            maze=maze,
            path=[*path, new_pos],
            current_pos=new_pos,
            end_tile=end_tile,
        )

        if result:
            results.append(result)

    if results:
        return min(results, key=lambda x: len(x))

    return []


def maze_solver_path_builder(
    maze: list[str], start_tile: str, end_tile: str
) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()

    list_idx = 0
    string_idx = 0
    for idx, line in enumerate(maze):
        list_idx = idx
        string_idx = line.find(start_tile)
        if string_idx != -1:
            break

    return runner_path_builder(
        seen=seen,
        maze=maze,
        path=[(list_idx, string_idx)],
        current_pos=(list_idx, string_idx),
        end_tile=end_tile,
    )


def runner_backtracker(
    seen: set[tuple[int, int]],
    maze: list[str],
    current_pos: tuple[int, int],
    end_tile: str,
) -> list[tuple[int, int]]:
    if current_pos in seen:
        return []
    if not (
        0 <= current_pos[0] < len(maze)
        and 0 <= current_pos[1] < len(maze[current_pos[0]])
    ):
        return []
    if maze[current_pos[0]][current_pos[1]] == "#":
        return []
    if maze[current_pos[0]][current_pos[1]] == end_tile:
        return [current_pos]

    seen.add(current_pos)
    results: list[list[tuple[int, int]]] = []
    for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        result = runner_backtracker(
            seen=seen,
            maze=maze,
            current_pos=(current_pos[0] + pos[0], current_pos[1] + pos[1]),
            end_tile=end_tile,
        )

        if result:
            result.append(current_pos)
            results.append(result)

    if results:
        return min(results, key=lambda x: len(x))

    return []


def maze_solver_back_tracker(
    maze: list[str], start_tile: str, end_tile: str
) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()

    list_idx = 0
    string_idx = 0
    for idx, line in enumerate(maze):
        list_idx = idx
        string_idx = line.find(start_tile)
        if string_idx != -1:
            break

    return list(
        reversed(
            runner_backtracker(
                seen=seen,
                maze=maze,
                current_pos=(list_idx, string_idx),
                end_tile=end_tile,
            )
        )
    )
