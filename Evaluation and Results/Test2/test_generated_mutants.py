import pytest
from source_to_mutate import truncate_number

def test_truncate_number_positive_integer():
    assert truncate_number(5.0) == 0.0

def test_truncate_number_positive_decimal():
    assert truncate_number(3.14) == pytest.approx(0.14)

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_large_number():
    assert truncate_number(1234567.89) == pytest.approx(0.89)

def test_truncate_number_small_decimal():
    assert truncate_number(0.001) == pytest.approx(0.001)

def test_truncate_number_one():
    assert truncate_number(1.0) == 0.0

def test_truncate_number_almost_one():
    assert truncate_number(0.99999) == pytest.approx(0.99999)