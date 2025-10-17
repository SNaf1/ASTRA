import pytest
from source_to_mutate import is_palindrome, make_palindrome, METADATA, check

def test_is_palindrome_empty_string():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_palindrome():
    assert is_palindrome('madam') == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome('hello') == False

def test_is_palindrome_mixed_case_palindrome():
    assert is_palindrome('Racecar') == False

def test_is_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False

def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_char():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_simple_case():
    assert make_palindrome('cat') == 'catac'

def test_make_palindrome_already_palindrome():
    assert make_palindrome('xyx') == 'xyx'

def test_make_palindrome_longer_string():
    assert make_palindrome('abcde') == 'abcdedcba'

def test_make_palindrome_cata():
    assert make_palindrome('cata') == 'catac'

def test_make_palindrome_jerry():
    assert make_palindrome('jerry') == 'jerryrrej'

def test_make_palindrome_race():
    assert make_palindrome('race') == 'racecar'

def test_make_palindrome_level():
    assert make_palindrome('level') == 'level'

def test_metadata_author():
    assert METADATA['author'] == 'jt'

def test_metadata_dataset():
    assert METADATA['dataset'] == 'test'

def test_check_empty_string():
    assert check(make_palindrome) is None

def test_check_x():
    assert check(make_palindrome) is None

def test_check_xyz():
    assert check(make_palindrome) is None

def test_check_xyx():
    assert check(make_palindrome) is None

def test_check_jerry():
    assert check(make_palindrome) is None