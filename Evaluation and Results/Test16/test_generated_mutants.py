import pytest
from source_to_mutate import count_distinct_characters

def test_empty_string():
    assert count_distinct_characters('') == 0

def test_single_character():
    assert count_distinct_characters('a') == 1

def test_all_same_characters():
    assert count_distinct_characters('aaaa') == 1

def test_mixed_case():
    assert count_distinct_characters('aA') == 1

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3

def test_string_with_spaces():
    assert count_distinct_characters('abc def') == 7

def test_string_with_numbers():
    assert count_distinct_characters('abc123') == 6

def test_string_with_special_characters():
    assert count_distinct_characters('abc!@#') == 6

def test_string_with_mixed_case_and_numbers():
    assert count_distinct_characters('aBc123') == 6

def test_string_with_mixed_case_and_special_characters():
    assert count_distinct_characters('aBc!@#') == 6

def test_string_with_repeated_characters():
    assert count_distinct_characters('aabbcc') == 3

def test_string_with_repeated_characters_mixed_case():
    assert count_distinct_characters('aAbBcC') == 3

def test_long_string():
    assert count_distinct_characters('The quick brown fox jumps over the lazy Fox') == 25

def test_string_with_unicode_characters():
    assert count_distinct_characters('你好世界') == 4

def test_string_with_mixed_unicode_and_ascii():
    assert count_distinct_characters('hello你好') == 6

def test_string_with_numbers_and_unicode():
    assert count_distinct_characters('123你好') == 5

def test_string_with_special_characters_and_unicode():
    assert count_distinct_characters('!@#你好') == 5

def test_string_with_mixed_case_unicode():
    assert count_distinct_characters('你好NiHao') == 7

def test_string_with_empty_spaces():
    assert count_distinct_characters('   ') == 1