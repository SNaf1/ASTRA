import pytest
from source_to_mutate import histogram

def test_empty_string():
    assert histogram('') == {}

def test_single_letter():
    assert histogram('a') == {'a': 1}

def test_multiple_distinct_letters():
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}

def test_repeated_letters():
    assert histogram('a b b a') == {'a': 2, 'b': 2}

def test_repeated_letters_mixed():
    assert histogram('a b c a b') == {'a': 2, 'b': 2}

def test_single_dominant_letter():
    assert histogram('b b b b a') == {'b': 4}

def test_multiple_dominant_letters():
    assert histogram('a a b b c') == {'a': 2, 'b': 2}

def test_multiple_dominant_letters_uneven():
    assert histogram('a a b b b c') == {'b': 3}

def test_long_string():
    assert histogram('a b c d e f g h i j k l m n o p q r s t u v w x y z') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}

def test_string_with_spaces():
    assert histogram('   a   b   c   ') == {'a': 1, 'b': 1, 'c': 1}

def test_string_with_leading_and_trailing_spaces():
    assert histogram('  a b  ') == {'a': 1, 'b': 1}

def test_string_with_internal_multiple_spaces():
    assert histogram('a  b   c') == {'a': 1, 'b': 1, 'c': 1}

def test_string_with_only_spaces():
    assert histogram('   ') == {}

def test_mixed_case_string():
    assert histogram('A a B b') == {'A': 1, 'a': 1, 'B': 1, 'b': 1}

def test_numbers_in_string():
    assert histogram('1 2 3') == {'1': 1, '2': 1, '3': 1}

def test_special_characters_in_string():
    assert histogram('! @ #') == {'!': 1, '@': 1, '#': 1}

def test_empty_string_with_spaces():
    assert histogram(' ') == {}

def test_repeated_letter_with_space():
    assert histogram('a a ') == {'a': 2}