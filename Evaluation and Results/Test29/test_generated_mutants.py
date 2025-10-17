import pytest
from source_to_mutate import filter_by_prefix


def test_empty_list():
    assert filter_by_prefix([], 'a') == []


def test_empty_prefix():
    assert filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']


def test_no_match():
    assert filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []


def test_single_match():
    assert filter_by_prefix(['abc', 'bcd', 'cde'], 'a') == ['abc']


def test_multiple_matches():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']


def test_prefix_is_substring():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'ab'], 'abc') == ['abc']


def test_prefix_is_longer_than_string():
    assert filter_by_prefix(['abc', 'bcd', 'cde'], 'abcd') == []


def test_mixed_case():
    assert filter_by_prefix(['Abc', 'abc', 'BCD'], 'a') == ['abc']


def test_special_characters():
    assert filter_by_prefix(['!abc', '@bcd', '#cde'], '!') == ['!abc']


def test_unicode():
    assert filter_by_prefix(['你好abc', '你好bcd', '你好cde'], '你好') == ['你好abc', '你好bcd', '你好cde']


def test_empty_string_in_list():
    assert filter_by_prefix(['', 'abc', 'bcd'], '') == ['', 'abc', 'bcd']


def test_prefix_is_empty_string():
    assert filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']