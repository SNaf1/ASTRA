import pytest
from source_to_mutate import how_many_times

def test_empty_string_empty_substring():
    assert how_many_times('', '') == 1

def test_empty_string_non_empty_substring():
    assert how_many_times('', 'a') == 0

def test_non_empty_string_empty_substring():
    assert how_many_times('abc', '') == 4

def test_substring_longer_than_string():
    assert how_many_times('ab', 'abc') == 0

def test_substring_equals_string():
    assert how_many_times('abc', 'abc') == 1

def test_substring_occurs_once():
    assert how_many_times('abcabc', 'def') == 0

def test_substring_occurs_multiple_times():
    assert how_many_times('abcabc', 'abc') == 2

def test_overlapping_substrings():
    assert how_many_times('aaaa', 'aa') == 3

def test_substring_at_start():
    assert how_many_times('abcdef', 'abc') == 1

def test_substring_at_end():
    assert how_many_times('abcdef', 'ef') == 1

def test_substring_in_middle():
    assert how_many_times('abcdef', 'cd') == 1

def test_string_with_special_characters():
    assert how_many_times('a!b@c#', '!') == 1

def test_substring_with_special_characters():
    assert how_many_times('a!b@c#', 'b@') == 1

def test_string_and_substring_with_special_characters():
    assert how_many_times('a!b@c#', 'a!b') == 1

def test_case_sensitive():
    assert how_many_times('abcABC', 'abc') == 1

def test_numbers_in_string():
    assert how_many_times('123456', '123') == 1

def test_numbers_in_substring():
    assert how_many_times('123456', '234') == 1

def test_mixed_characters():
    assert how_many_times('a1b2c3d4', 'b2c') == 1

def test_long_string_and_substring():
    long_string = 'abcdefg' * 100
    long_substring = 'def'
    assert how_many_times(long_string, long_substring) == 100

def test_long_string_and_substring_overlapping():
    long_string = 'aaaaa' * 100
    long_substring = 'aa'
    assert how_many_times(long_string, long_substring) == 499

def test_unicode_characters():
    assert how_many_times('你好世界', '你好') == 1

def test_substring_is_same_character():
    assert how_many_times('aaaa', 'a') == 4