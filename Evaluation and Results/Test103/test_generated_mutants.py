import pytest
from source_to_mutate import rounded_avg

def test_rounded_avg_basic():
    assert rounded_avg(1, 5) == '0b11'

def test_rounded_avg_n_greater_than_m():
    assert rounded_avg(7, 5) == -1

def test_rounded_avg_range_10_20():
    assert rounded_avg(10, 20) == '0b1111'

def test_rounded_avg_range_20_33():
    assert rounded_avg(20, 33) == '0b11010'

def test_rounded_avg_same_number():
    assert rounded_avg(5, 5) == '0b101'

def test_rounded_avg_small_range():
    assert rounded_avg(1, 2) == '0b10'

def test_rounded_avg_large_numbers():
    assert rounded_avg(100, 105) == '0b1100110'

def test_rounded_avg_n_close_to_m():
    assert rounded_avg(99, 100) == '0b1100100'

def test_rounded_avg_zero_range():
    assert rounded_avg(0, 0) == '0b0'

def test_rounded_avg_negative_n():
    assert rounded_avg(-1, 5) == '0b10'

def test_rounded_avg_negative_m():
    assert rounded_avg(1, -5) == -1

def test_rounded_avg_large_range():
    assert rounded_avg(1, 100) == '0b110010'