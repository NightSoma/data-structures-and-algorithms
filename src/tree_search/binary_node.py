from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


@dataclass
class BinaryNode[T]:
    value: T
    left: "BinaryNode[T] | None"
    right: "BinaryNode[T] | None"
