import pytest
from source_to_mutate import filter_integers

def test_empty_list():
    assert filter_integers([]) == []

def test_only_integers():
    assert filter_integers([1, 2, 3]) == [1, 2, 3]

def test_only_strings():
    assert filter_integers(['a', 'b', 'c']) == []

def test_mixed_types():
    assert filter_integers(['a', 3.14, 5, 'b', 10]) == [5, 10]

def test_floats_and_integers():
    assert filter_integers([1.0, 2, 3.0, 4]) == [2, 4]

def test_booleans_and_integers():
    assert filter_integers([True, False, 1, 0, 5]) == [True, False, 1, 0, 5]

def test_none_and_integers():
    assert filter_integers([None, 1, 2, None]) == [1, 2]

def test_list_of_lists():
    assert filter_integers([[1, 2], [3, 4], 5]) == [5]

def test_list_of_dicts():
    assert filter_integers([{'a': 1}, {'b': 2}, 3]) == [3]

def test_large_numbers():
    assert filter_integers([1000000, 2000000, 'a']) == [1000000, 2000000]

def test_negative_numbers():
    assert filter_integers([-1, -2, -3, 'a']) == [-1, -2, -3]

def test_zero():
    assert filter_integers([0, 'a', 1]) == [0, 1]

def test_mixed_negative_positive():
    assert filter_integers([-1, 0, 1, 'a']) == [-1, 0, 1]

def test_duplicate_integers():
    assert filter_integers([1, 1, 1, 2, 2, 3]) == [1, 1, 1, 2, 2, 3]

def test_empty_string():
    assert filter_integers(["", 1, 2]) == [1, 2]

def test_special_characters():
    assert filter_integers(["!", "@", "#", 1, 2]) == [1, 2]

def test_unicode_strings():
    assert filter_integers(["你好", 1, 2]) == [1, 2]

def test_complex_numbers():
    assert filter_integers([1+1j, 1, 2]) == [1, 2]

def test_bytes_and_integers():
    assert filter_integers([b'abc', 1, 2]) == [1, 2]