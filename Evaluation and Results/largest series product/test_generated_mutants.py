import pytest
from source_to_mutate import slices, largest_product

def test_slices_valid_input():
    assert slices('12345', 2) == [[1, 2], [2, 3], [3, 4], [4, 5]]

def test_slices_invalid_size_greater_than_series():
    with pytest.raises(ValueError) as excinfo:
        slices('123', 4)
    assert 'span must be smaller than string length' in str(excinfo.value)

def test_slices_invalid_size_negative():
    with pytest.raises(ValueError) as excinfo:
        slices('123', -1)
    assert 'span must not be negative' in str(excinfo.value)

def test_slices_invalid_size_zero():
    with pytest.raises(ValueError) as excinfo:
        slices('123', 0)
    assert 'span must not be negative' in str(excinfo.value)

def test_slices_invalid_input_non_digit():
    with pytest.raises(ValueError) as excinfo:
        slices('12a3', 2)
    assert 'digits input must only contain digits' in str(excinfo.value)

def test_slices_empty_series():
    with pytest.raises(ValueError) as excinfo:
        slices('', 1)
    assert 'span must be smaller than string length' in str(excinfo.value)

def test_slices_size_equals_series_length():
    assert slices('123', 3) == [[1, 2, 3]]

def test_largest_product_valid_input():
    assert largest_product('12345', 2) == 20

def test_largest_product_size_zero():
    assert largest_product('12345', 0) == 1

def test_largest_product_size_one():
    assert largest_product('12345', 1) == 5

def test_largest_product_size_equals_series_length():
    assert largest_product('123', 3) == 6

def test_largest_product_series_with_zeros():
    assert largest_product('1027', 2) == 14

def test_largest_product_series_with_all_zeros():
    assert largest_product('0000', 2) == 0

def test_largest_product_single_digit_series():
    assert largest_product('5', 1) == 5

def test_largest_product_invalid_input_non_digit():
    with pytest.raises(ValueError) as excinfo:
        largest_product('12a3', 2)
    assert 'digits input must only contain digits' in str(excinfo.value)

def test_largest_product_invalid_size_greater_than_series():
    with pytest.raises(ValueError) as excinfo:
        largest_product('123', 4)
    assert 'span must be smaller than string length' in str(excinfo.value)

def test_largest_product_invalid_size_negative():
    with pytest.raises(ValueError) as excinfo:
        largest_product('123', -1)
    assert 'span must not be negative' in str(excinfo.value)