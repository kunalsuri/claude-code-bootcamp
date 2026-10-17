from textstats import longest_word, word_count


def test_word_count_simple():
    assert word_count("hello world") == 2


def test_longest_word():
    assert longest_word("a quick brown fox") == "quick"


def test_longest_word_empty():
    assert longest_word("") == ""
