import pytest
from source_to_mutate import sorted_list_sum

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_single_even_length_string():
    assert sorted_list_sum(['aa']) == ['aa']

def test_single_odd_length_string():
    assert sorted_list_sum(['a']) == []

def test_mixed_lengths():
    assert sorted_list_sum(['aa', 'a', 'aaa']) == ['aa']

def test_multiple_even_lengths():
    assert sorted_list_sum(['ab', 'a', 'aaa', 'cd']) == ['ab', 'cd']

def test_duplicates():
    assert sorted_list_sum(['aa', 'aa', 'a', 'aaa']) == ['aa', 'aa']

def test_all_odd_lengths():
    assert sorted_list_sum(['a', 'aaa', 'bbbbb']) == []

def test_already_sorted():
    assert sorted_list_sum(['aa', 'bb', 'cc']) == ['aa', 'bb', 'cc']

def test_reverse_sorted():
    assert sorted_list_sum(['cc', 'bb', 'aa']) == ['aa', 'bb', 'cc']

def test_same_length_different_strings():
    assert sorted_list_sum(['ab', 'cd', 'aa']) == ['aa', 'ab', 'cd']

def test_longer_strings():
    assert sorted_list_sum(['aaaa', 'aa', 'aaaaaaaa', 'aaaaaa']) == ['aa', 'aaaa', 'aaaaaa', 'aaaaaaaa']

def test_mixed_case():
    assert sorted_list_sum(['Aa', 'aA', 'aa']) == ['Aa', 'aA', 'aa']

def test_numbers_as_strings():
    assert sorted_list_sum(['12', '1', '123']) == ['12']

def test_special_characters():
    assert sorted_list_sum(['!@', '!', '!@#']) == ['!@']

def test_empty_string():
    assert sorted_list_sum(['', 'a', 'aa']) == ['', 'aa']

def test_empty_and_non_empty():
    assert sorted_list_sum(['', 'aa']) == ['', 'aa']

def test_long_list():
    input_list = ['aa'] * 10 + ['a'] * 5
    expected_output = ['aa'] * 10
    assert sorted_list_sum(input_list) == expected_output

def test_strings_with_spaces():
    assert sorted_list_sum(['a a', 'aa', 'a']) == ['aa']

def test_strings_with_leading_and_trailing_spaces():
    assert sorted_list_sum(['  aa  ', 'aa', 'a']) == ['aa', '  aa  ']