import pytest
from source_to_mutate import compare_one

def test_compare_one_int_float():
    assert compare_one(1, 2.5) == 2.5

def test_compare_one_int_string():
    assert compare_one(1, '2,3') == '2,3'

def test_compare_one_string_string():
    assert compare_one('5,1', '6') == '6'

def test_compare_one_string_int_equal():
    assert compare_one('1', 1) is None

def test_compare_one_int_int_equal():
    assert compare_one(1, 1) is None

def test_compare_one_float_float_equal():
    assert compare_one(1.0, 1.0) is None

def test_compare_one_string_string_equal():
    assert compare_one('1', '1') is None

def test_compare_one_float_int():
    assert compare_one(2.5, 1) == 2.5

def test_compare_one_string_float():
    assert compare_one('2,3', 1.0) == '2,3'

def test_compare_one_float_string():
    assert compare_one(1.0, '2,3') == '2,3'

def test_compare_one_negative_int_float():
    assert compare_one(-1, 2.5) == 2.5

def test_compare_one_negative_float_int():
    assert compare_one(2.5, -1) == 2.5

def test_compare_one_negative_int_string():
    assert compare_one(-1, '2,3') == '2,3'

def test_compare_one_negative_string_int():
    assert compare_one('2,3', -1) == '2,3'

def test_compare_one_negative_string_string():
    assert compare_one('-5,1', '-6') == '-5,1'

def test_compare_one_zero_int_float():
    assert compare_one(0, 2.5) == 2.5

def test_compare_one_zero_float_int():
    assert compare_one(2.5, 0) == 2.5

def test_compare_one_zero_int_string():
    assert compare_one(0, '2,3') == '2,3'

def test_compare_one_zero_string_int():
    assert compare_one('2,3', 0) == '2,3'

def test_compare_one_zero_string_string():
    assert compare_one('0', '2,3') == '2,3'

def test_compare_one_large_numbers():
    assert compare_one(1000000, 2000000) == 2000000

def test_compare_one_large_string_numbers():
    assert compare_one('1000000', '2000000') == '2000000'

def test_compare_one_decimal_string():
    assert compare_one('1.5', 2) == 2

def test_compare_one_decimal_string_comma():
    assert compare_one('1,5', 2) == 2

def test_compare_one_int_decimal_string():
    assert compare_one(2, '1.5') == 2

def test_compare_one_int_decimal_string_comma():
    assert compare_one(2, '1,5') == 2

def test_compare_one_negative_decimal_string():
    assert compare_one('-1.5', -2) == '-1.5'

def test_compare_one_negative_decimal_string_comma():
    assert compare_one('-1,5', -2) == '-1,5'

def test_compare_one_negative_int_decimal_string():
    assert compare_one(-2, '-1.5') == '-1.5'

def test_compare_one_negative_int_decimal_string_comma():
    assert compare_one(-2, '-1,5') == '-1,5'

def test_compare_one_same_string_different_formats():
    assert compare_one('1.5', '1,5') is None

def test_compare_one_same_string_different_formats_reversed():
    assert compare_one('1,5', '1.5') is None

def test_compare_one_same_string_different_formats_equal():
    assert compare_one('1,5', '1.5') is None