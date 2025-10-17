import pytest
from source_to_mutate import total_match

def test_empty_lists():
    assert total_match([], []) == []

def test_same_length_lists():
    assert total_match(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']

def test_list1_shorter():
    assert total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']

def test_list2_shorter():
    assert total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']

def test_list1_shorter_single_char():
    assert total_match(['4'], ['1', '2', '3', '4', '5']) == ['4']

def test_list1_empty():
    assert total_match([], ['a', 'b']) == []

def test_list2_empty():
    assert total_match(['a', 'b'], []) == []

def test_list1_shorter_equal_length():
    assert total_match(['a'], ['aa']) == ['a']

def test_list2_shorter_equal_length():
    assert total_match(['aaa'], ['a']) == ['a']

def test_list1_equal_list2():
    assert total_match(['abc'], ['abc']) == ['abc']

def test_list1_shorter_multiple_strings():
    assert total_match(['a', 'b'], ['c', 'd', 'e']) == ['a', 'b']

def test_list2_shorter_multiple_strings():
    assert total_match(['c', 'd', 'e'], ['a', 'b']) == ['a', 'b']

def test_list1_shorter_with_empty_string():
    assert total_match([''], ['a', 'b']) == ['']

def test_list2_shorter_with_empty_string():
    assert total_match(['a', 'b'], ['']) == ['']

def test_list1_equal_with_empty_string():
    assert total_match([''], ['']) == ['']

def test_list1_shorter_with_numbers():
    assert total_match(['123'], ['12345']) == ['123']

def test_list2_shorter_with_numbers():
    assert total_match(['12345'], ['123']) == ['123']

def test_list1_shorter_with_special_chars():
    assert total_match(['!@#'], ['!@#$%^']) == ['!@#']

def test_list2_shorter_with_special_chars():
    assert total_match(['!@#$%^'], ['!@#']) == ['!@#']

def test_list1_shorter_mixed_chars():
    assert total_match(['a1!', 'b2@'], ['c3#', 'd4$', 'e5%']) == ['a1!', 'b2@']

def test_list2_shorter_mixed_chars():
    assert total_match(['c3#', 'd4$', 'e5%'], ['a1!', 'b2@']) == ['a1!', 'b2@']

def test_list1_shorter_same_length_strings():
    assert total_match(['aa', 'bb'], ['cc', 'dd', 'ee']) == ['aa', 'bb']

def test_list2_shorter_same_length_strings():
    assert total_match(['cc', 'dd', 'ee'], ['aa', 'bb']) == ['aa', 'bb']