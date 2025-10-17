import pytest
from source_to_mutate import same_chars

def test_same_chars_true_1():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True

def test_same_chars_true_2():
    assert same_chars('abcd', 'dddddddabc') == True

def test_same_chars_true_3():
    assert same_chars('dddddddabc', 'abcd') == True

def test_same_chars_false_1():
    assert same_chars('eabcd', 'dddddddabc') == False

def test_same_chars_false_2():
    assert same_chars('abcd', 'dddddddabce') == False

def test_same_chars_false_3():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False

def test_same_chars_empty_strings():
    assert same_chars('', '') == True

def test_same_chars_one_empty_string():
    assert same_chars('', 'abc') == False

def test_same_chars_single_char_same():
    assert same_chars('a', 'a') == True

def test_same_chars_single_char_different():
    assert same_chars('a', 'b') == False

def test_same_chars_same_string():
    assert same_chars('abc', 'abc') == True

def test_same_chars_same_chars_different_order():
    assert same_chars('abc', 'cba') == True

def test_same_chars_same_chars_different_counts():
    assert same_chars('aabbcc', 'abc') == True

def test_same_chars_same_chars_different_counts_reversed():
    assert same_chars('abc', 'aabbcc') == True

def test_same_chars_special_characters():
    assert same_chars('!@#$', '$#@!') == True

def test_same_chars_mixed_characters():
    assert same_chars('a1b2c3', '3c2b1a') == True

def test_same_chars_long_strings_same():
    s = 'abcdefghijklmnopqrstuvwxyz'
    assert same_chars(s * 10, s) == True

def test_same_chars_long_strings_different():
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = 'abcdefghijklmnopqrstuwwxyz'
    assert same_chars(s1, s2) == False

def test_same_chars_unicode_characters():
    assert same_chars('你好世界', '界世好你') == True

def test_same_chars_unicode_and_ascii():
    assert same_chars('a你好b世界', '界世b好a你') == True

def test_same_chars_numbers():
    assert same_chars('12345', '54321') == True

def test_same_chars_numbers_and_letters():
    assert same_chars('a1b2c3', '3c2b1a') == True

def test_same_chars_repeated_chars_and_different_chars():
    assert same_chars('aaaaabc', 'abc') == True

def test_same_chars_repeated_chars_and_different_chars_reversed():
    assert same_chars('abc', 'aaaaabc') == True