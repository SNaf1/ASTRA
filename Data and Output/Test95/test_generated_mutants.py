import pytest
from source_to_mutate import check_dict_case

def test_empty_dict():
    assert check_dict_case({}) == False

def test_all_lower_case():
    assert check_dict_case({'a': 'apple', 'b': 'banana'}) == True

def test_mixed_case():
    assert check_dict_case({'a': 'apple', 'A': 'banana', 'B': 'banana'}) == False

def test_non_string_key():
    assert check_dict_case({'a': 'apple', 8: 'banana', 'a': 'apple'}) == False

def test_mixed_case_2():
    assert check_dict_case({'Name': 'John', 'Age': '36', 'City': 'Houston'}) == False

def test_all_upper_case():
    assert check_dict_case({'STATE': 'NC', 'ZIP': '12345'}) == True

def test_mixed_case_3():
    assert check_dict_case({'a': 'apple', 'B': 'banana'}) == False

def test_all_lower_case_single_item():
    assert check_dict_case({'a': 'apple'}) == True

def test_all_upper_case_single_item():
    assert check_dict_case({'A': 'apple'}) == True

def test_mixed_case_single_item():
    assert check_dict_case({'A a': 'apple'}) == False

def test_dict_with_space_in_key():
    assert check_dict_case({'a b': 'apple', 'c d': 'banana'}) == True

def test_dict_with_number_in_key():
    assert check_dict_case({'a1': 'apple', 'b2': 'banana'}) == True

def test_dict_with_special_char_in_key():
    assert check_dict_case({'a!': 'apple', 'b@': 'banana'}) == True

def test_dict_with_empty_string_key():
    assert check_dict_case({'': 'apple'}) == False

def test_dict_with_numeric_keys_as_strings():
    assert check_dict_case({'1': 'one', '2': 'two'}) == False

def test_dict_with_mixed_numeric_and_alpha_keys():
    assert check_dict_case({'a': 'one', '1': 'two'}) == False