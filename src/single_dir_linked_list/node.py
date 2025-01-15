from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """Node of Linked List."""

    def __init__(
        self,
        item: T,
        next_node: "Node[T] | None" = None,
    ) -> None:
        """Initialize new node with item.

        Args:
            item (T): Item of the node.
            next_node (Node[T] | None, optional): Reference to next node. Defaults to None.
        """
        self.item = item
        self.next = next_node

    def __eq__(self, other: object) -> bool:
        """Check if nodes are equal.

        Args:
            other (object): Other node.

        Returns:
            bool: Return True if nodes equal.
        """
        if not isinstance(other, type(self)):
            raise NotImplementedError

        return self.item == other.item

    def __str__(self) -> str:
        """String representaion of node instance."""
        return f"Node(item=[{self.item}], next=[{self.next!r}])"

    def __repr__(self) -> str:
        """String representaion of node instance.

        Suatable for debbuging.
        """
        return f"Node(item=[{self.item}], next=[{bool(self.next)}])"
