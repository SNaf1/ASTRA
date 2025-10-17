import pytest
from source_to_mutate import sum_to_n, METADATA

def test_sum_to_n_positive():
    assert sum_to_n(5) == 15

def test_sum_to_n_zero():
    assert sum_to_n(0) == 0

def test_sum_to_n_one():
    assert sum_to_n(1) == 1

def test_sum_to_n_large():
    assert sum_to_n(100) == 5050

def test_sum_to_n_another_positive():
    assert sum_to_n(30) == 465

def test_sum_to_n_negative():
    assert sum_to_n(-1) == 0

def test_sum_to_n_large_negative():
    assert sum_to_n(-100) == 0