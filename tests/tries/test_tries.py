import pytest

from tries.tries import T, Tries


@pytest.fixture
def trie_with_words() -> Tries[str]:
    empty_trie = Tries[str]()
    words = ["apple", "app", "apricot", "banana", "ban", "bat"]
    for word in words:
        empty_trie.insert(word)
    return empty_trie


def test_insert_and_search():
    empty_trie = Tries[str]()
    empty_trie.insert("apple")
    assert empty_trie.search("apple") is True
    assert empty_trie.search("app") is False
    assert empty_trie.search("banana") is False
    assert empty_trie.search("") is False


def test_starts_with(trie_with_words: Tries[T]):
    assert trie_with_words.starts_with("") is False
    assert trie_with_words.starts_with("app") is True
    assert trie_with_words.starts_with("ba") is True
    assert trie_with_words.starts_with("ca") is False
    assert trie_with_words.starts_with("appl") is True
    assert trie_with_words.starts_with("apric") is True


def test_get_all_words(trie_with_words: Tries[T]):
    words = trie_with_words.get_all_words()
    assert sorted(words) == sorted(["apple", "app", "apricot", "banana", "ban", "bat"])


def test_delete(trie_with_words: Tries[T]):
    trie_with_words.delete("app")
    assert trie_with_words.search("app") is False
    assert trie_with_words.search("apple") is True
    assert trie_with_words.starts_with("ap") is True

    trie_with_words.delete("apple")
    assert trie_with_words.search("apple") is False
    assert trie_with_words.starts_with("ap") is True

    trie_with_words.delete("ban")
    assert trie_with_words.search("ban") is False
    assert trie_with_words.search("banana") is True
    assert trie_with_words.starts_with("ba") is True


def test_delete_nonexistent_word(trie_with_words: Tries[T]):
    trie_with_words.delete("")
    trie_with_words.delete("orange")
    assert trie_with_words.search("orange") is False


def test_auto_complete(trie_with_words: Tries[T]):
    assert trie_with_words.auto_complete("app") == sorted(["app", "apple"])
    assert trie_with_words.auto_complete("ba") == sorted(["banana", "ban", "bat"])
    assert trie_with_words.auto_complete("x") == []
    assert trie_with_words.auto_complete("") == []


def test_is_empty(trie_with_words: Tries[T]):
    empty_trie = Tries[str]()
    assert empty_trie.is_empty() is True
    assert trie_with_words.is_empty() is False


def test_clear(trie_with_words: Tries[T]):
    trie_with_words.clear()
    assert trie_with_words.is_empty() is True
    assert trie_with_words.get_all_words() == []
