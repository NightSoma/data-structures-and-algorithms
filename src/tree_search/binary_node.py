from dataclasses import dataclass
from typing import TypeVar

from tree_search.comparable_protocol import Comparable

T = TypeVar("T", bound=Comparable)


@dataclass
class BinaryNode[T]:
    value: T
    left: "BinaryNode[T] | None" = None
    right: "BinaryNode[T] | None" = None
