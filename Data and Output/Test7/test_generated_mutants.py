import pytest
from source_to_mutate import filter_by_substring, METADATA


def test_empty_list():
    assert filter_by_substring([], 'a') == []


def test_substring_present():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']


def test_substring_not_present():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == []


def test_empty_substring():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']


def test_substring_at_start():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab') == ['abc']


def test_substring_at_end():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ay') == ['array']


def test_substring_is_same_as_string():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array', 'a'], 'a') == ['abc', 'bacd', 'array', 'a']


def test_substring_is_longer_than_string():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'abcdefg') == []


def test_list_with_empty_string():
    assert filter_by_substring(['abc', '', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']


def test_list_with_only_empty_string():
    assert filter_by_substring([''], 'a') == []


def test_list_with_substring_only_in_empty_string():
    assert filter_by_substring(['', 'a'], 'a') == ['a']


def test_list_with_duplicate_strings():
    assert filter_by_substring(['abc', 'abc', 'bacd', 'abc'], 'abc') == ['abc', 'abc', 'abc']


def test_list_with_unicode_strings():
    assert filter_by_substring(['你好世界', 'hello world', '你好'], '你好') == ['你好世界', '你好']


def test_metadata():
    assert METADATA['author'] == 'jt'
    assert METADATA['dataset'] == 'test'