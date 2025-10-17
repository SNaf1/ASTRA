import pytest
from source_to_mutate import select_words

def test_empty_string():
    assert select_words('', 4) == []

def test_single_word_match():
    assert select_words('Mary had a little lamb', 4) == ['little']

def test_multiple_words_match():
    assert select_words('Mary had a little lamb', 3) == ['Mary', 'lamb']

def test_no_match():
    assert select_words('simple white space', 2) == []

def test_hello_world():
    assert select_words('Hello world', 4) == ['world']

def test_uncle_sam():
    assert select_words('Uncle sam', 3) == ['Uncle']

def test_single_word_exact_match():
    assert select_words('test', 2) == []

def test_single_word_no_match():
    assert select_words('test', 3) == ['test']

def test_multiple_words_mixed_match():
    assert select_words('test case example', 4) == ['example']

def test_multiple_spaces():
    assert select_words('  test   case  ', 2) == ['case']

def test_all_vowels():
    assert select_words('aeiou', 0) == ['aeiou']

def test_all_consonants():
    assert select_words('bcdfghjklmnpqrstvwxyz', 21) == ['bcdfghjklmnpqrstvwxyz']

def test_mixed_case():
    assert select_words('TeSt CaSe', 2) == ['CaSe']

def test_numbers_in_string():
    assert select_words('123 abc 456', 3) == ['123', '456']

def test_special_characters_in_string():
    assert select_words('!@# abc $%^', 3) == ['!@#', '$%^']

def test_n_zero():
    assert select_words('Mary had a little lamb', 0) == ['a']

def test_n_greater_than_word_length():
    assert select_words('Mary had a little lamb', 10) == []

def test_long_string():
    long_string = 'a' * 100 + ' b' * 50 + ' cdef'
    assert select_words(long_string, 3) == ['cdef']