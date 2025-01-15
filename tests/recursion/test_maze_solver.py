from recursion.maze_solver import maze_solver_back_tracker, maze_solver_path_builder


def test_maze_solver_path_builder__map_1():
    maze = ["#####E#", "#     #", "#S#####"]
    assert maze_solver_path_builder(maze=maze, start_tile="S", end_tile="E") == [
        (2, 1),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (0, 5),
    ]


def test_maze_solver_path_builder__map_2():
    maze = ["#####", "#   S", "# # #", "#   E"]
    assert maze_solver_path_builder(maze=maze, start_tile="S", end_tile="E") == [
        (1, 4),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 4),
    ]


def test_maze_solver_path_builder__map_3_super_simple():
    maze = ["SE"]
    assert maze_solver_path_builder(maze=maze, start_tile="S", end_tile="E") == [
        (0, 0),
        (0, 1),
    ]


def test_maze_solver_path_builder__map_4_shortes_path_test():
    maze = [".....", "..#..", "...E.", "#.#..", "S...."]
    assert maze_solver_path_builder(maze=maze, start_tile="S", end_tile="E") == [
        (4, 0),
        (4, 1),
        (3, 1),
        (2, 1),
        (2, 2),
        (2, 3),
    ]


def test_aze_solver_path_builder__impossibe_map():
    maze = ["S#E"]
    assert maze_solver_path_builder(maze=maze, start_tile="S", end_tile="E") == []


def test_maze_solver_back_tracker__map_1():
    maze = ["#####E#", "#     #", "#S#####"]
    assert maze_solver_back_tracker(maze=maze, start_tile="S", end_tile="E") == [
        (2, 1),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (0, 5),
    ]


def test_maze_solver_back_tracker__map_2():
    maze = ["#####", "#   S", "# # #", "#   E"]
    assert maze_solver_back_tracker(maze=maze, start_tile="S", end_tile="E") == [
        (1, 4),
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 4),
    ]


def test_maze_solver_back_tracker__map_3_super_simple():
    maze = ["SE"]
    assert maze_solver_back_tracker(maze=maze, start_tile="S", end_tile="E") == [
        (0, 0),
        (0, 1),
    ]


def test_maze_solver_back_tracker__map_4_shortes_path_test():
    maze = [".....", "..#..", "...E.", "#.#..", "S...."]
    assert maze_solver_back_tracker(maze=maze, start_tile="S", end_tile="E") == [
        (4, 0),
        (4, 1),
        (3, 1),
        (2, 1),
        (2, 2),
        (2, 3),
    ]


def test_maze_solver_back_tracker__impossibe_map():
    maze = ["S#E"]
    assert maze_solver_back_tracker(maze=maze, start_tile="S", end_tile="E") == []
