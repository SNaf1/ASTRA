import pytest
from source_to_mutate import longest

def test_empty_list():
    assert longest([]) is None

def test_single_string():
    assert longest(['abc']) == 'abc'

def test_multiple_strings_different_lengths():
    assert longest(['a', 'bb', 'ccc']) == 'ccc'

def test_multiple_strings_same_length():
    assert longest(['a', 'b', 'c']) == 'a'

def test_multiple_strings_mixed_lengths_same_longest_length():
    assert longest(['a', 'bb', 'ccc', 'ddd', 'ee']) == 'ccc'

def test_strings_with_spaces():
    assert longest(['a ', ' bb', 'ccc ']) == 'ccc '

def test_strings_with_special_characters():
    assert longest(['a!', 'bb@', 'ccc#']) == 'ccc#'

def test_empty_strings():
    assert longest(['', 'a', 'bb']) == 'bb'

def test_all_empty_strings():
    assert longest(['', '', '']) == ''

def test_long_list_of_strings():
    strings = [str(i) for i in range(100)]
    strings.append('1' * 101)
    assert longest(strings) == '1' * 101

def test_strings_with_unicode():
    assert longest(['你好', '世界']) == '你好'

def test_strings_with_numbers():
    assert longest(['123', '45', '6']) == '123'