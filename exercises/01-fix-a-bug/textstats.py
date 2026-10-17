"""Tiny text statistics helpers."""


def word_count(text):
    """Return the number of words in text."""
    return len(text.split(" "))


def longest_word(text):
    """Return the longest word in text, or an empty string if there are none."""
    words = text.split()
    return max(words, key=len) if words else ""
