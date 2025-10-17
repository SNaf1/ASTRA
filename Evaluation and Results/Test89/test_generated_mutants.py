import pytest
from source_to_mutate import encrypt

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_single_letter():
    assert encrypt('h') == 'l'

def test_encrypt_two_letters():
    assert encrypt('hi') == 'lm'

def test_encrypt_multiple_letters():
    assert encrypt('asdfghjkl') == 'ewhjklnop'

def test_encrypt_wrap_around():
    assert encrypt('gf') == 'kj'

def test_encrypt_wrap_around_2():
    assert encrypt('et') == 'ix'

def test_encrypt_with_space():
    assert encrypt('hello world') == 'lipps asvph'

def test_encrypt_with_uppercase():
    assert encrypt('Hello') == 'Hipps'

def test_encrypt_with_numbers():
    assert encrypt('123') == '123'

def test_encrypt_with_special_characters():
    assert encrypt('!@#$%^') == '!@#$%^'

def test_encrypt_mixed_characters():
    assert encrypt('a1b2c!d@e#') == 'e1f2g!h@i#'

def test_encrypt_long_string():
    assert encrypt('the quick brown fox jumps over the lazy dog') == 'xli uymgo fvsar jsb nyqtw sziv xli pedc hsk'

def test_encrypt_z():
    assert encrypt('z') == 'd'

def test_encrypt_y():
    assert encrypt('y') == 'c'