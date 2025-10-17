import pytest
from source_to_mutate import anti_shuffle

def test_empty_string():
    assert anti_shuffle('') == ''

def test_single_word():
    assert anti_shuffle('hello') == 'ehllo'

def test_multiple_words():
    assert anti_shuffle('hello world') == 'ehllo dlorw'

def test_with_spaces():
    assert anti_shuffle(' hello world ') == ' ehllo dlorw '

def test_with_punctuation():
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'

def test_mixed_case():
    assert anti_shuffle('Mixed Case') == 'Mdeix Caes'

def test_numbers():
    assert anti_shuffle('12345') == '12345'

def test_numbers_and_letters():
    assert anti_shuffle('a1b2c3d') == '123abcd'

def test_special_characters():
    assert anti_shuffle('!@#$%^') == '!#$%@^'

def test_mixed_special_characters_and_letters():
    assert anti_shuffle('a!b@c#') == '!#@abc'

def test_long_string():
    assert anti_shuffle('This is a very long string with many words') == 'This is a ervy glno ginrst hitw amny dorsw'

def test_already_ordered():
    assert anti_shuffle('abc def ghi') == 'abc def ghi'

def test_single_character_words():
    assert anti_shuffle('a b c d') == 'a b c d'

def test_repeated_characters():
    assert anti_shuffle('aabbcc') == 'aabbcc'

def test_mixed_case_and_numbers():
    assert anti_shuffle('aA1bB2') == '12ABab'

def test_leading_and_trailing_spaces():
    assert anti_shuffle('  hello world  ') == '  ehllo dlorw  '

def test_multiple_spaces_between_words():
    assert anti_shuffle('hello   world') == 'ehllo   dlorw'

def test_non_ascii_characters():
    assert anti_shuffle('你好世界') == '世你好界'

def test_mixed_ascii_and_non_ascii():
    assert anti_shuffle('hello 你好') == 'ehllo 你好'

def test_string_with_only_spaces():
    assert anti_shuffle('   ') == '   '