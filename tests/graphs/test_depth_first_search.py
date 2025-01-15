import pytest

from graphs.depth_first_search import (
    depth_first_search_recursion,
    depth_first_search_stack,
)


@pytest.fixture
def adjacency_matrix_weighted() -> list[list[int]]:
    return [
        [1, 3, 1, 0, 0, 0, 0, 0, 0],  # Node 0
        [0, 0, 5, 0, 8, 0, 0, 0, 0],  # Node 1
        [1, 0, 0, 0, 0, 0, 0, 0, 0],  # Node 2
        [0, 0, 0, 0, 1, 0, 0, 7, 0],  # Node 3
        [0, 0, 0, 0, 0, 4, 2, 0, 0],  # Node 4
        [0, 0, 0, 0, 0, 5, 0, 0, 0],  # Node 5 (Dead end)
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  # Node 6
        [0, 0, 0, 0, 6, 1, 0, 0, 0],  # Node 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Node 8 (Dead end)
    ]


def test_path_from_node_0_to_node_5_recursion(
    adjacency_matrix_weighted: list[list[int]],
):
    assert depth_first_search_recursion(adjacency_matrix_weighted, 0, 5) == (
        [0, 1, 4, 5]
    )


def test_path_from_node_5_to_node_0_recursion(
    adjacency_matrix_weighted: list[list[int]],
):
    assert depth_first_search_recursion(adjacency_matrix_weighted, 5, 0) is None


def test_path_from_node_0_to_node_5_stack(
    adjacency_matrix_weighted: list[list[int]],
):
    assert depth_first_search_stack(adjacency_matrix_weighted, 0, 5) == [0, 1, 4, 5]


def test_path_from_node_5_to_node_0_stack(
    adjacency_matrix_weighted: list[list[int]],
):
    assert depth_first_search_stack(adjacency_matrix_weighted, 5, 0) is None
