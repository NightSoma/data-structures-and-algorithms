from typing import Generic, TypeVar

T = TypeVar("T")


class DoubleNode(Generic[T]):
    """Node of Linked List."""

    def __init__(
        self,
        item: T,
        prev_node: "DoubleNode[T] | None" = None,
        next_node: "DoubleNode[T] | None" = None,
    ) -> None:
        self.item = item
        self.prev = prev_node
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
        return f"Node(item=[{self.item}], prev=[{self.prev is not None}], next=[{self.next is not None}])"

    def __repr__(self) -> str:
        """String representaion of node instance.

        Suatable for debbuging.
        """
        return f"Node(item=[{self.item}], prev=[{self.prev!s}], next=[{self.next!s}])"
