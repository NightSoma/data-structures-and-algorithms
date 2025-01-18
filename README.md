# Data Structures and Algorithms - Python Implementations

This repository contains my implementations of various important data structures and algorithms in Python. These implementations were developed as part of my learning journey while taking the [Algorithms course by ThePrimeagen on Frontend Masters](https://frontendmasters.com/courses/algorithms/).

## Key Features

* **Comprehensive:** Covers a wide range of fundamental data structures and algorithms (see [Contents](#contents)).
* **Well-Tested:** 280 tests with 100% code coverage using `pytest` and `pytest-cov`.
* **Clean Code:** Focus on readability and maintainability.
* **Modern Tooling:** Uses `uv` for efficient dependency and virtual environment management.

## Contents

This repository is organized into the following directories:

* **`search`:** Search algorithms (binary search, linear search, 'crystal breaks' problem).
* **`sort`:** Sorting algorithms (bubble sort, quicksort).
* **`heap`:** Heap implementation.
* **`stack`:** Stack implementation.
* **`queue`:** Queue implementation.
* **`ring_buffer`:** Ring buffer implementation.
* **`recursion`:** Examples of recursion (maze solver).
* **`singly_linked_list`:** Singly linked list implementation.
* **`doubly_linked_list`:** Doubly linked list implementation.
* **`tree_search`:** Tree search algorithms (BST, DFOperations on BinaryTree, traversal, compare).
* **`tries`:** Trie implementation.
* **`graphs`:** Graph algorithms (BFS, DFS, Dijkstra's).
* **`lru`:** LRU (Least Recently Used) cache.

## Requirements

* Python 3.13 or higher.
* `uv`

## Setup and Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/NightSoma/data-structures-and-algorithms.git
    cd data_structures_and_algorithms
    ```

2. **Initialize project and create a virtual environment using `uv`:**

    ```bash
    uv init --no-workspace
    uv venv
    ```

3. **Activate the virtual environment:**

    ```bash
     source .venv/bin/activate  # On Linux/macOS
    .venv/Scripts/activate  # On Windows
    ```

   *Note: gitbash on windows may not run  `.venv/Scripts/activate`*

4. **Install dependencies with `uv`:**

    ```bash
    uv pip install ".[dev,test]"
    ```

## Running Tests

To run all tests with coverage analysis:

```bash
pytest --cov=. --cov-report term-missing
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
