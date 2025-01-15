import pytest

from graphs.dijkstra import dijkstra_list


@pytest.fixture
def adjacency_matrix_weighted() -> list[list[int]]:
    return [
        [1, 3, 1, 0, 0, 7, 0, 0, 0],  # Node 0
        [0, 0, 5, 0, 8, 0, 0, 0, 0],  # Node 1
        [1, 0, 0, 2, 0, 0, 0, 0, 0],  # Node 2
        [0, 0, 0, 0, 1, 0, 0, 7, 0],  # Node 3
        [0, 0, 0, 0, 0, 4, 2, 0, 0],  # Node 4
        [0, 0, 0, 0, 0, 5, 0, 0, 0],  # Node 5 (Dead end)
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  # Node 6
        [0, 0, 0, 0, 6, 1, 0, 0, 0],  # Node 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Node 8 (Dead end)
    ]


def test_path_from_node_0_to_node_5(
    adjacency_matrix_weighted: list[list[int]],
):
    assert dijkstra_list(adjacency_matrix_weighted, 0, 5) == (
        [0, 5],
        [7],
    )


def test_path_from_node_5_to_node_0(
    adjacency_matrix_weighted: list[list[int]],
):
    assert dijkstra_list(adjacency_matrix_weighted, 5, 0) is None


def test_path_from_node_0_to_node_5_delete_one_path(
    adjacency_matrix_weighted: list[list[int]],
):
    adjacency_matrix_weighted[0][5] = 0
    assert dijkstra_list(adjacency_matrix_weighted, 0, 5) == (
        [0, 2, 3, 4, 5],
        [1, 2, 1, 4],
    )


def test_path_from_node_5_to_node_0_delete_one_path(
    adjacency_matrix_weighted: list[list[int]],
):
    adjacency_matrix_weighted[0][5] = 0
    assert dijkstra_list(adjacency_matrix_weighted, 5, 0) is None
