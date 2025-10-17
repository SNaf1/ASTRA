import pytest
from source_to_mutate import all_prefixes

def test_empty_string():
    assert all_prefixes("") == []

def test_single_character():
    assert all_prefixes("a") == ["a"]

def test_multiple_characters():
    assert all_prefixes("abc") == ["a", "ab", "abc"]

def test_numbers():
    assert all_prefixes("123") == ["1", "12", "123"]

def test_special_characters():
    assert all_prefixes("!@#") == ["!", "!@", "!@#"]

def test_mixed_characters():
    assert all_prefixes("a1!") == ["a", "a1", "a1!"]

def test_long_string():
    assert all_prefixes("abcdefghij") == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']