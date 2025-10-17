import pytest
from source_to_mutate import mean_absolute_deviation

def test_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean_absolute_deviation([])

def test_single_element_list():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_positive_numbers():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_negative_numbers():
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == 1.0

def test_mixed_numbers():
    assert mean_absolute_deviation([-1.0, 1.0, -2.0, 2.0]) == 1.5

def test_decimal_numbers():
    assert mean_absolute_deviation([1.5, 2.5, 3.5, 4.5]) == 1.0

def test_zero_numbers():
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]) == 0.0

def test_large_numbers():
    assert mean_absolute_deviation([1000.0, 2000.0, 3000.0, 4000.0]) == 1000.0

def test_duplicate_numbers():
    assert mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]) == 0.0

def test_uneven_distribution():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 10.0]) == 3.0

def test_negative_and_positive_with_zero():
    assert mean_absolute_deviation([-2.0, -1.0, 0.0, 1.0, 2.0]) == 1.2