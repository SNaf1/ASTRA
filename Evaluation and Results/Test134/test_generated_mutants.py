import pytest
from source_to_mutate import check_if_last_char_is_a_letter

def test_empty_string():
    assert check_if_last_char_is_a_letter("") == False

def test_single_word_ending_with_letter():
    assert check_if_last_char_is_a_letter("apple") == False

def test_single_letter():
    assert check_if_last_char_is_a_letter("a") == True

def test_multiple_words_last_char_is_letter():
    assert check_if_last_char_is_a_letter("apple pi e") == True

def test_multiple_words_last_char_is_not_letter():
    assert check_if_last_char_is_a_letter("apple pie") == False

def test_multiple_words_last_char_is_letter_with_space_at_end():
    assert check_if_last_char_is_a_letter("apple pi e ") == False

def test_multiple_words_last_char_is_number():
    assert check_if_last_char_is_a_letter("apple pi 2") == False

def test_multiple_words_last_char_is_special_character():
    assert check_if_last_char_is_a_letter("apple pi $") == False

def test_multiple_words_last_char_is_uppercase_letter():
    assert check_if_last_char_is_a_letter("apple pi E") == True

def test_multiple_words_last_char_is_multiple_letters():
    assert check_if_last_char_is_a_letter("apple pi ee") == False

def test_multiple_spaces():
    assert check_if_last_char_is_a_letter("apple   pi e") == True

def test_string_with_only_space():
    assert check_if_last_char_is_a_letter(" ") == False

def test_string_with_leading_and_trailing_spaces():
    assert check_if_last_char_is_a_letter("  apple pi e  ") == False

def test_string_with_number_at_the_end():
    assert check_if_last_char_is_a_letter("test 1") == False

def test_string_with_special_char_at_the_end():
    assert check_if_last_char_is_a_letter("test !") == False

def test_string_with_tab():
    assert check_if_last_char_is_a_letter("test\ta") == False

def test_string_with_newline():
    assert check_if_last_char_is_a_letter("test\na") == False

def test_string_with_unicode_character():
    assert check_if_last_char_is_a_letter("test é") == False

def test_string_with_multiple_unicode_characters():
    assert check_if_last_char_is_a_letter("test éé") == False

def test_string_with_unicode_character_as_single_char():
    assert check_if_last_char_is_a_letter("é") == False

def test_string_with_number_and_letter():
    assert check_if_last_char_is_a_letter("1a") == False