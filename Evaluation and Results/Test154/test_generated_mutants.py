import pytest
from source_to_mutate import cycpattern_check

def test_cycpattern_check_false_abd():
    assert cycpattern_check('abcd', 'abd') == False

def test_cycpattern_check_true_ell():
    assert cycpattern_check('hello', 'ell') == True

def test_cycpattern_check_false_psus():
    assert cycpattern_check('whassup', 'psus') == False

def test_cycpattern_check_true_baa():
    assert cycpattern_check('abab', 'baa') == True

def test_cycpattern_check_false_eeff():
    assert cycpattern_check('efef', 'eeff') == False

def test_cycpattern_check_true_simen():
    assert cycpattern_check('himenss', 'simen') == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check('abc', '') == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check('', 'abc') == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check('', '') == True

def test_cycpattern_check_a_equals_b():
    assert cycpattern_check('abc', 'abc') == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check('abc', 'abcd') == False

def test_cycpattern_check_single_char_match():
    assert cycpattern_check('a', 'a') == True

def test_cycpattern_check_single_char_no_match():
    assert cycpattern_check('a', 'b') == False

def test_cycpattern_check_repeated_chars_a():
    assert cycpattern_check('aaaa', 'aa') == True

def test_cycpattern_check_repeated_chars_b():
    assert cycpattern_check('abc', 'bbb') == False

def test_cycpattern_check_rotation_at_end():
    assert cycpattern_check('abcdef', 'defabc') == True

def test_cycpattern_check_rotation_at_start():
    assert cycpattern_check('abcdef', 'bcdefa') == True

def test_cycpattern_check_long_strings_no_match():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'zyxwvutsrqponmlkjihgfedcba'
    assert cycpattern_check(a, b) == False

def test_cycpattern_check_long_strings_match():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'nopqrstuvwxyzabc'
    assert cycpattern_check(a, b) == False

def test_cycpattern_check_overlapping_rotation():
    assert cycpattern_check('abcabc', 'bca') == True

def test_cycpattern_check_same_char_rotation():
    assert cycpattern_check('aaaa', 'aa') == True

def test_cycpattern_check_almost_match():
    assert cycpattern_check('hello', 'elloo') == False

def test_cycpattern_check_complex_rotation():
    assert cycpattern_check('1234567890', '8901234567') == True