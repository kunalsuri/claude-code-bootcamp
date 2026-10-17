import pytest

from textstats import longest_word, word_count


def test_word_count_simple():
    assert word_count("hello world") == 2


@pytest.mark.parametrize(
    "text, expected",
    [
        ("", 0),
        ("   ", 0),
        ("\n", 0),
        ("a  b", 2),
        ("  a b  ", 2),
        ("a\nb\tc", 3),
    ],
)
def test_word_count_edge_cases(text, expected):
    assert word_count(text) == expected


def test_longest_word():
    assert longest_word("a quick brown fox") == "quick"


@pytest.mark.parametrize("text", ["", "   ", "\n"])
def test_longest_word_no_words(text):
    assert longest_word(text) == ""


def test_longest_word_tie_returns_first():
    assert longest_word("cat dog") == "cat"
