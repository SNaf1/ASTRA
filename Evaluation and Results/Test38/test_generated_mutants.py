import pytest
from source_to_mutate import *

def test_encode_cyclic_empty_string():
    assert encode_cyclic('') == ''

def test_encode_cyclic_single_character():
    assert encode_cyclic('a') == 'a'

def test_encode_cyclic_two_characters():
    assert encode_cyclic('ab') == 'ab'

def test_encode_cyclic_three_characters():
    assert encode_cyclic('abc') == 'bca'

def test_encode_cyclic_four_characters():
    assert encode_cyclic('abcd') == 'bca' + 'd'

def test_encode_cyclic_five_characters():
    assert encode_cyclic('abcde') == 'bca' + 'de'

def test_encode_cyclic_six_characters():
    assert encode_cyclic('abcdef') == 'bca' + 'efd'

def test_encode_cyclic_seven_characters():
    assert encode_cyclic('abcdefg') == 'bca' + 'efd' + 'g'

def test_encode_cyclic_multiple_of_three():
    assert encode_cyclic('abcdefghi') == 'bca' + 'efd' + 'hig'

def test_encode_cyclic_with_numbers():
    assert encode_cyclic('123456') == '231' + '564'

def test_encode_cyclic_with_special_characters():
    assert encode_cyclic('!@#$^&') == '@#!^&$'

def test_encode_cyclic_mixed_characters():
    assert encode_cyclic('a1b2c3d') == '1ba' + 'c32' + 'd'

def test_decode_cyclic_empty_string():
    assert decode_cyclic('') == ''

def test_decode_cyclic_single_character():
    assert decode_cyclic('a') == 'a'

def test_decode_cyclic_two_characters():
    assert decode_cyclic('ab') == 'ab'

def test_decode_cyclic_three_characters():
    assert decode_cyclic('bca') == 'abc'

def test_decode_cyclic_four_characters():
    assert decode_cyclic('bcad') == 'abcd'

def test_decode_cyclic_five_characters():
    assert decode_cyclic('bcade') == 'abcde'

def test_decode_cyclic_six_characters():
    assert decode_cyclic('bcadefd') == 'abcfded'

def test_decode_cyclic_seven_characters():
    assert decode_cyclic('bcadefdg') == 'abcfdedg'

def test_decode_cyclic_multiple_of_three():
    assert decode_cyclic('bcadefghig') == 'abcfdeighg'

def test_decode_cyclic_with_numbers():
    assert decode_cyclic('231564') == '123456'

def test_decode_cyclic_with_special_characters():
    assert decode_cyclic('@#!$^&') == '!@#&$^'

def test_decode_cyclic_mixed_characters():
    assert decode_cyclic('1ab2c3d') == 'b1a32cd'