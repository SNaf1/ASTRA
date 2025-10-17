import pytest
from source_to_mutate import is_palindrome

def test_empty_string():
    assert is_palindrome('') == True

def test_single_character():
    assert is_palindrome('a') == True

def test_palindrome_aba():
    assert is_palindrome('aba') == True

def test_palindrome_aaaaa():
    assert is_palindrome('aaaaa') == True

def test_non_palindrome_zbcd():
    assert is_palindrome('zbcd') == False

def test_mixed_case_palindrome():
    assert is_palindrome('AbA') == True

def test_palindrome_with_space():
    assert is_palindrome('abc cba') == True

def test_long_palindrome():
    assert is_palindrome('racecaracecar') == True

def test_long_non_palindrome():
    assert is_palindrome('racecaracecarb') == False

def test_palindrome_with_numbers():
    assert is_palindrome('12321') == True

def test_non_palindrome_with_numbers():
    assert is_palindrome('12345') == False

def test_palindrome_with_special_characters():
    assert is_palindrome('madam!') == False

def test_non_palindrome_with_special_characters():
    assert is_palindrome('hello!') == False

def test_palindrome_with_mixed_characters():
    assert is_palindrome('A man, a plan, a canal: Panama') == False