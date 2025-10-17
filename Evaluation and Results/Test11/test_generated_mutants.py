import pytest
from source_to_mutate import string_xor, METADATA


def test_string_xor_basic():
    assert string_xor('010', '110') == '100'


def test_string_xor_same():
    assert string_xor('111', '111') == '000'


def test_string_xor_different():
    assert string_xor('000', '111') == '111'


def test_string_xor_empty():
    assert string_xor('', '') == ''


def test_string_xor_one_empty():
    assert string_xor('0', '') == ''


def test_string_xor_one_longer():
    assert string_xor('1010', '101') == '000'


def test_string_xor_zeroes():
    assert string_xor('0000', '0000') == '0000'


def test_string_xor_ones():
    assert string_xor('1111', '1111') == '0000'


def test_string_xor_mixed():
    assert string_xor('1010', '0101') == '1111'


def test_string_xor_long():
    assert string_xor('10101010', '01010101') == '11111111'


def test_string_xor_long_same():
    assert string_xor('10101010', '10101010') == '00000000'


def test_string_xor_long_different():
    assert string_xor('11001100', '00110011') == '11111111'