from collections.abc import Generator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class TrieNode[T]:
    character: str
    is_end_of_word: bool
    dictionary: "dict[str, TrieNode[T]]"


class Tries(Generic[T]):
    def __init__(self) -> None:
        self.dictionary: dict[str, TrieNode[T]] = {}

    def insert(self, word: str) -> None:
        current_node = None
        current_dict = self.dictionary

        for idx, char in enumerate(word):
            if char not in current_dict:
                current_dict[char] = TrieNode(
                    character=char, is_end_of_word=False, dictionary={}
                )
            current_node = current_dict[char]

            if idx >= len(word) - 1:
                current_node.is_end_of_word = True

            current_dict = current_node.dictionary

    def search(self, word: str) -> bool:
        current_dict = self.dictionary
        last_node = None

        for char in word:
            if char not in current_dict:
                return False
            last_node = current_dict[char]
            current_dict = last_node.dictionary

        if last_node is None:
            return False

        return last_node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current_dict = self.dictionary
        last_node = None

        for char in prefix:
            if char not in current_dict:
                return False
            last_node = current_dict[char]
            current_dict = last_node.dictionary

        if last_node is not None:
            return (
                len(
                    list(
                        self._get_all_words_continuations_generator(
                            last_node.dictionary
                        )
                    )
                )
                > 0
            )

        return False

    def _get_all_words_continuations_generator(
        self, dictionary: dict[str, TrieNode[T]]
    ) -> Generator[str]:
        for char, node in dictionary.items():
            for word in self._get_all_words_continuations_generator(node.dictionary):
                word = char + word

                yield word

            if node.is_end_of_word:
                yield char

    def get_all_words(self) -> list[str]:
        return list(self._get_all_words_continuations_generator(self.dictionary))

    def delete(self, word: str) -> bool:
        current_dict = self.dictionary
        last_node = None

        for char in word:
            if char not in current_dict:
                return False
            last_node = current_dict[char]
            current_dict = last_node.dictionary

        if last_node is not None and last_node.is_end_of_word:
            last_node.is_end_of_word = False
            return True

        return False

    def auto_complete(self, prefix: str) -> list[str]:
        current_dict = self.dictionary
        last_node = None

        for char in prefix:
            if char not in current_dict:
                return []
            last_node = current_dict[char]
            current_dict = last_node.dictionary

        if last_node is not None:
            words: list[str] = []
            for word in self._get_all_words_continuations_generator(
                last_node.dictionary
            ):
                words.append(prefix + word)
            if last_node.is_end_of_word:
                words.append(prefix)
            return sorted(words)

        return []

    def is_empty(self) -> bool:
        return not bool(self.dictionary)

    def clear(self) -> None:
        """Removes all words from the Trie."""
        self.dictionary = {}
