from dataclasses import dataclass, field


@dataclass
class RingBuffer[T]:
    ls: list[T | None] = field(default_factory=list)
    head_idx: int = 0
    tail_idx: int = -1

    def pop_head(self) -> T | None:
        if len(self) == 0:
            raise ValueError("RingBuffer empty!")

        item = self.ls[self.head_idx]
        self.head_idx = (self.head_idx + 1) % len(self.ls)

        return item

    def push_tail(self, item: T | None) -> None:
        if len(self) == len(self.ls):
            raise ValueError("Reached max capacity!")

        self.tail_idx = (self.tail_idx + 1) % len(self.ls)
        self.ls[self.tail_idx] = item

    def __len__(self) -> int:
        ln = self.tail_idx - self.head_idx + 1
        if ln < 0:
            return len(self.ls) - self.head_idx + self.tail_idx
        return ln
