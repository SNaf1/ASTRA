import pytest
from source_to_mutate import remove_vowels

def test_empty_string():
    assert remove_vowels('') == ''

def test_string_with_vowels_and_newline():
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'

def test_string_with_vowels():
    assert remove_vowels('abcdef') == 'bcdf'

def test_string_with_only_vowels():
    assert remove_vowels('aaaaa') == ''

def test_string_with_mixed_case_vowels():
    assert remove_vowels('aaBAA') == 'B'

def test_string_without_vowels():
    assert remove_vowels('zbcd') == 'zbcd'

def test_string_with_uppercase_vowels():
    assert remove_vowels('AEIOU') == ''

def test_string_with_mixed_case_and_consonants():
    assert remove_vowels('hEllO wOrLd') == 'hll wrLd'

def test_string_with_numbers_and_vowels():
    assert remove_vowels('1a2e3i4o5u') == '12345'

def test_string_with_special_characters_and_vowels():
    assert remove_vowels('!@#a$%^e&*i()o_+u') == '!@#$%^&*()_+'

def test_string_with_unicode_characters():
    assert remove_vowels('你好世界') == '你好世界'

def test_string_with_vowels_at_start_and_end():
    assert remove_vowels('apple') == 'ppl'

def test_string_with_repeated_vowels():
    assert remove_vowels('bee') == 'b'

def test_string_with_vowels_and_spaces():
    assert remove_vowels('a e i o u') == '    '