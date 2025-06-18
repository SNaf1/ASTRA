import pytest
from source_to_mutate import reverse_delete

def test_empty_strings():
    assert reverse_delete('', '') == ('', True)

def test_empty_s():
    assert reverse_delete('', 'abc') == ('', True)

def test_empty_c():
    assert reverse_delete('abc', '') == ('abc', False)

def test_no_matching_chars():
    assert reverse_delete('abc', 'def') == ('abc', False)

def test_single_char_s_and_c_match():
    assert reverse_delete('a', 'a') == ('', True)

def test_single_char_s_and_c_no_match():
    assert reverse_delete('a', 'b') == ('a', True)

def test_multiple_chars_s_and_c_match():
    assert reverse_delete('abcde', 'ae') == ('bcd', False)

def test_multiple_chars_s_and_c_partial_match():
    assert reverse_delete('abcdef', 'b') == ('acdef', False)

def test_palindrome_after_deletion():
    assert reverse_delete('abcdedcba', 'ab') == ('cdedc', True)

def test_palindrome_no_deletion():
    assert reverse_delete('madam', '') == ('madam', True)

def test_non_palindrome_no_deletion():
    assert reverse_delete('hello', '') == ('hello', False)

def test_all_chars_deleted():
    assert reverse_delete('aaaa', 'a') == ('', True)

def test_c_longer_than_s():
    assert reverse_delete('a', 'abc') == ('', True)

def test_duplicate_chars_in_s():
    assert reverse_delete('aabbcc', 'a') == ('bbcc', False)

def test_duplicate_chars_in_c():
    assert reverse_delete('abc', 'aa') == ('bc', False)

def test_mixed_case():
    assert reverse_delete('aBcDe', 'ae') == ('BcD', False)

def test_special_characters():
    assert reverse_delete('!@#$%^', '$') == ('!@#%^', False)

def test_numbers():
    assert reverse_delete('12345', '24') == ('135', False)

def test_mixed_characters():
    assert reverse_delete('a1b2c3d', '12') == ('abc3d', False)

def test_s_is_palindrome_but_deletion_makes_it_not():
    assert reverse_delete('madam', 'm') == ('ada', True)

def test_s_is_not_palindrome_but_deletion_makes_it_palindrome():
    assert reverse_delete('ababa', 'b') == ('aaa', True)

def test_c_contains_s():
    assert reverse_delete('abc', 'abcdefg') == ('', True)