import pytest
from source_to_mutate import words_string

def test_empty_string():
    assert words_string("") == []

def test_single_word():
    assert words_string("hello") == ['hello']

def test_words_separated_by_spaces():
    assert words_string("hello world") == ['hello', 'world']

def test_words_separated_by_commas():
    assert words_string("hello,world") == ['hello', 'world']

def test_words_separated_by_mixed_spaces_and_commas():
    assert words_string("hello, world,test") == ['hello', 'world', 'test']

def test_multiple_spaces():
    assert words_string("hello   world") == ['hello', 'world']

def test_multiple_commas():
    assert words_string("hello,,,world") == ['hello', 'world']

def test_leading_and_trailing_spaces():
    assert words_string("  hello world  ") == ['hello', 'world']

def test_leading_and_trailing_commas():
    assert words_string(",,hello world,,") == ['hello', 'world']

def test_mixed_leading_trailing_spaces_and_commas():
    assert words_string(" , hello world, ") == ['hello', 'world']

def test_string_with_numbers():
    assert words_string("one, two, three, four, five, six") == ['one', 'two', 'three', 'four', 'five', 'six']

def test_string_with_special_characters():
    assert words_string("hello! world?") == ['hello!', 'world?']

def test_string_with_mixed_special_characters_and_separators():
    assert words_string("hello!, world?,test ") == ['hello!', 'world?', 'test']

def test_string_with_only_spaces():
    assert words_string("   ") == []

def test_string_with_only_commas():
    assert words_string(",,,") == []

def test_string_with_commas_and_spaces():
    assert words_string(", , ,") == []

def test_string_with_one_comma_and_one_space():
    assert words_string(", ") == []

def test_string_with_comma_space_and_word():
    assert words_string(", hello ") == ['hello']

def test_string_with_space_comma_and_word():
    assert words_string(" ,hello") == ['hello']