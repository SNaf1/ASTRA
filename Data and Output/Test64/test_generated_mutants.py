import pytest
from source_to_mutate import vowels_count

def test_empty_string():
    with pytest.raises(IndexError):
        vowels_count('')

def test_no_vowels():
    assert vowels_count('bcdfghjklmnpqrstvwxz') == 0

def test_all_vowels_lowercase():
    assert vowels_count('aeiou') == 5

def test_all_vowels_uppercase():
    assert vowels_count('AEIOU') == 5

def test_mixed_vowels():
    assert vowels_count('aEiOu') == 5

def test_y_at_end_lowercase():
    assert vowels_count('fly') == 1

def test_y_at_end_uppercase():
    assert vowels_count('FLY') == 1

def test_y_not_at_end_lowercase():
    assert vowels_count('yellow') == 2

def test_y_not_at_end_uppercase():
    assert vowels_count('YELLOW') == 2

def test_mixed_case_with_y():
    assert vowels_count('aBCDy') == 2

def test_string_with_spaces():
    assert vowels_count('a e i o u') == 5

def test_string_with_numbers():
    assert vowels_count('a1e2i3o4u') == 5

def test_string_with_special_characters():
    assert vowels_count('a!e@i#o$u%') == 5

def test_string_with_y_and_other_vowels():
    assert vowels_count('bay') == 2

def test_string_with_multiple_ys():
    assert vowels_count('yayay') == 3

def test_string_with_y_in_middle():
    assert vowels_count('style') == 1

def test_string_with_y_and_uppercase_vowels():
    assert vowels_count('ABy') == 2

def test_string_with_only_y():
    assert vowels_count('y') == 1

def test_string_with_only_uppercase_y():
    assert vowels_count('Y') == 1

def test_string_with_y_and_other_characters():
    assert vowels_count('xyz') == 0

def test_string_with_uppercase_y_and_other_characters():
    assert vowels_count('xYz') == 0

def test_string_with_y_and_numbers():
    assert vowels_count('y123') == 0

def test_string_with_uppercase_y_and_numbers():
    assert vowels_count('Y123') == 0

def test_string_with_y_and_special_characters():
    assert vowels_count('y!@#') == 0

def test_string_with_uppercase_y_and_special_characters():
    assert vowels_count('Y!@#') == 0

def test_string_with_y_and_vowels_in_middle():
    assert vowels_count('bayou') == 3

def test_string_with_uppercase_y_and_vowels_in_middle():
    assert vowels_count('bAYOu') == 3

def test_string_with_y_and_vowels_at_start():
    assert vowels_count('ayu') == 2

def test_string_with_uppercase_y_and_vowels_at_start():
    assert vowels_count('AYU') == 2

def test_string_with_y_and_vowels_at_end():
    assert vowels_count('aby') == 2

def test_string_with_uppercase_y_and_vowels_at_end():
    assert vowels_count('ABY') == 2

def test_string_with_y_and_vowels_everywhere():
    assert vowels_count('aeiouy') == 6

def test_string_with_uppercase_y_and_vowels_everywhere():
    assert vowels_count('AEIOUY') == 6

def test_string_with_y_and_repeated_vowels():
    assert vowels_count('aaeeiioouuy') == 11

def test_string_with_uppercase_y_and_repeated_vowels():
    assert vowels_count('AAEEIIOOUUY') == 11

def test_long_string_with_vowels_and_y():
    assert vowels_count('The quick brown fox jumps over the lazy yellow dog') == 13

def test_long_string_with_uppercase_vowels_and_y():
    assert vowels_count('THE QUICK BROWN FOX JUMPS OVER THE LAZY YELLOW DOG') == 13