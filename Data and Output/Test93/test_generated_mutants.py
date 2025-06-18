import pytest
from source_to_mutate import encode

def test_encode_empty_string():
    assert encode('') == ''

def test_encode_test():
    assert encode('test') == 'TGST'

def test_encode_this_is_a_message():
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'

def test_encode_all_vowels():
    assert encode('aeiouAEIOU') == 'CGKQWcgkqw'

def test_encode_no_vowels():
    assert encode('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ') == 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'

def test_encode_mixed_case():
    assert encode('HeLlO wOrLd') == 'hGlLq WqRlD'

def test_encode_with_spaces():
    assert encode('  test  ') == '  TGST  '

def test_encode_with_numbers():
    assert encode('12345') == '12345'

def test_encode_with_special_characters():
    assert encode('!@#$%^&*()') == '!@#$%^&*()'

def test_encode_vowel_at_end():
    assert encode('tea') == 'TGC'

def test_encode_vowel_at_beginning():
    assert encode('eat') == 'GCT'

def test_encode_multiple_vowels_together():
    assert encode('aeiou') == 'CGKQW'

def test_encode_mixed_vowels_and_consonants():
    assert encode('apple') == 'CPPLG'

def test_encode_long_string():
    assert encode('The quick brown fox jumps over the lazy Dog') == 'tHG QWKCK BRQWN FQX JWMPS QVGR THG LCZY dQG'