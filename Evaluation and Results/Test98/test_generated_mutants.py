import pytest
from source_to_mutate import count_upper

def test_empty_string():
    assert count_upper('') == 0

def test_no_uppercase_vowels():
    assert count_upper('abcdefg') == 0

def test_single_uppercase_vowel_at_even_index():
    assert count_upper('aBCdEf') == 1

def test_single_uppercase_vowel_at_odd_index():
    assert count_upper('bAcdef') == 0

def test_multiple_uppercase_vowels_at_even_indices():
    assert count_upper('AEIOU') == 3

def test_multiple_uppercase_vowels_at_odd_indices():
    assert count_upper('aEiOu') == 0

def test_mixed_case_and_vowels():
    assert count_upper('aAeEiIoOuU') == 0

def test_only_lowercase_vowels():
    assert count_upper('aeiou') == 0

def test_string_with_numbers_and_symbols():
    assert count_upper('A1B2C3D4E5') == 2

def test_string_with_only_uppercase_consonants():
    assert count_upper('BCDFGHJKLMNPQRSTVWXYZ') == 0

def test_string_with_uppercase_vowels_and_consonants():
    assert count_upper('ABCDEFGHI') == 3

def test_string_with_special_characters():
    assert count_upper('A!B@C#D$E%') == 2

def test_long_string():
    assert count_upper('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA') == 25

def test_long_string_mixed():
    assert count_upper('AaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAa') == 25

def test_long_string_with_vowels_and_consonants():
    assert count_upper('AEIOUBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB') == 3

def test_string_with_non_ascii_characters():
    assert count_upper('ÄÖÜAEIOU') == 2

def test_string_with_spaces():
    assert count_upper('A B C D E') == 2

def test_string_with_newline():
    assert count_upper('A\nB\nC\nD\nE') == 2

def test_string_with_tab():
    assert count_upper('A\tB\tC\tD\tE') == 2

def test_string_with_mixed_spaces_and_tabs():
    assert count_upper('A \tB\t C \tD\t E') == 2