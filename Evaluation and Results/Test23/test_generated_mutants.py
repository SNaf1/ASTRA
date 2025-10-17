import pytest
from source_to_mutate import strlen

def test_strlen_empty_string():
    assert strlen('') == 0

def test_strlen_single_character():
    assert strlen('a') == 1

def test_strlen_multiple_characters():
    assert strlen('abc') == 3

def test_strlen_with_spaces():
    assert strlen('  abc  ') == 7

def test_strlen_with_special_characters():
    assert strlen('!@#$%^') == 6

def test_strlen_with_numbers():
    assert strlen('12345') == 5

def test_strlen_mixed_characters():
    assert strlen('a1b2c3d') == 7

def test_strlen_unicode():
    assert strlen('你好世界') == 4

def test_strlen_long_string():
    long_string = 'a' * 100
    assert strlen(long_string) == 100