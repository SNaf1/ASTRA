import pytest
from source_to_mutate import rescale_to_unit

def test_empty_list():
    with pytest.raises(ValueError):
        rescale_to_unit([])

def test_single_element_list():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0])

def test_positive_numbers():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_negative_numbers():
    assert rescale_to_unit([-5.0, -4.0, -3.0, -2.0, -1.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_mixed_numbers():
    assert rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_duplicate_min_max():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0])

def test_min_and_max_are_same():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([5.0, 5.0])

def test_floats():
    assert rescale_to_unit([1.5, 2.5, 3.5, 4.5, 5.5]) == [0.0, 0.25, 0.5, 0.75, 1.0]

def test_large_numbers():
    assert rescale_to_unit([1000.0, 2000.0, 3000.0]) == [0.0, 0.5, 1.0]

def test_small_numbers():
    assert rescale_to_unit([0.001, 0.002, 0.003]) == [0.0, 0.5, 1.0]

def test_negative_and_positive_with_zero():
    assert rescale_to_unit([-10.0, 0.0, 10.0]) == [0.0, 0.5, 1.0]

def test_same_min_and_max_with_other_numbers():
    assert rescale_to_unit([1.0, 2.0, 1.0, 2.0]) == [0.0, 1.0, 0.0, 1.0]

def test_very_small_difference():
    numbers = [1.0, 1.000000000000001]
    result = rescale_to_unit(numbers)
    assert result[0] == 0.0
    assert result[1] == 1.0

def test_identical_numbers():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([2.0, 2.0, 2.0])