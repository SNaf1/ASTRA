import pytest
from source_to_mutate import is_happy

def test_empty_string():
    assert is_happy('') == False

def test_one_char_string():
    assert is_happy('a') == False

def test_two_char_string():
    assert is_happy('aa') == False

def test_three_distinct_chars():
    assert is_happy('abc') == True

def test_three_same_chars():
    assert is_happy('aaa') == False

def test_four_distinct_chars():
    assert is_happy('abcd') == True

def test_four_chars_with_repetition():
    assert is_happy('aabc') == False

def test_four_chars_with_repetition_at_end():
    assert is_happy('bcda') == True

def test_five_chars_with_repetition():
    assert is_happy('abaca') == False

def test_five_chars_with_repetition_at_start():
    assert is_happy('aabca') == False

def test_long_string_distinct():
    assert is_happy('abcdefgh') == True

def test_long_string_with_repetition():
    assert is_happy('abcdefgha') == True

def test_long_string_with_repetition_close():
    assert is_happy('abcdefghg') == False

def test_long_string_with_repetition_close2():
    assert is_happy('abcdefghh') == False

def test_string_with_numbers():
    assert is_happy('1234') == True

def test_string_with_special_characters():
    assert is_happy('!@#$') == True

def test_string_with_mixed_characters():
    assert is_happy('a1b2c') == True

def test_string_with_mixed_characters_and_repetition():
    assert is_happy('a1a2c') == False

def test_string_with_mixed_characters_and_repetition_close():
    assert is_happy('a112c') == False

def test_string_with_spaces():
    assert is_happy('abc def') == True

def test_string_with_repeated_spaces():
    assert is_happy('ab  c') == False

def test_string_with_leading_and_trailing_spaces():
    assert is_happy('   abc   ') == False

def test_string_with_unicode_characters():
    assert is_happy('你好世界') == True

def test_string_with_unicode_repetition():
    assert is_happy('你好你世界') == False

def test_string_with_unicode_repetition_close():
    assert is_happy('你好你你') == False

def test_string_with_same_char_at_start_and_end():
    assert is_happy('aba') == False

def test_string_with_same_char_at_start_and_end_long():
    assert is_happy('abacdefa') == False

def test_string_with_same_char_at_start_and_end_long_close():
    assert is_happy('abacdefaa') == False