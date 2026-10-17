"""Tiny text statistics helpers."""


def _words(text):
    """Split text into words on any run of whitespace."""
    return text.split()


def word_count(text):
    """Return the number of words in text."""
    return len(_words(text))


def longest_word(text):
    """Return the longest word in text, or an empty string if there are none.

    If several words tie for longest, the first one wins.
    """
    words = _words(text)
    return max(words, key=len) if words else ""
