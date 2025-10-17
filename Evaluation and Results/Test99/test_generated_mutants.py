import pytest
from source_to_mutate import closest_integer

def test_closest_integer_positive_integer():
    assert closest_integer('10') == 10

def test_closest_integer_positive_float_round_down():
    assert closest_integer('15.3') == 15

def test_closest_integer_positive_half_round_up():
    assert closest_integer('14.5') == 15

def test_closest_integer_negative_half_round_down():
    assert closest_integer('-14.5') == -15

def test_closest_integer_positive_float_round_up():
    assert closest_integer('14.7') == 15

def test_closest_integer_negative_float_round_down():
    assert closest_integer('-14.7') == -15

def test_closest_integer_negative_integer():
    assert closest_integer('-10') == -10

def test_closest_integer_zero():
    assert closest_integer('0') == 0

def test_closest_integer_empty_string():
    with pytest.raises(ValueError, match="could not convert string to float: ''"):
        closest_integer('')

def test_closest_integer_positive_float_trailing_zeros():
    assert closest_integer('10.00') == 10

def test_closest_integer_negative_float_trailing_zeros():
    assert closest_integer('-10.00') == -10

def test_closest_integer_positive_float_half_trailing_zeros():
    assert closest_integer('10.50') == 11

def test_closest_integer_negative_float_half_trailing_zeros():
    assert closest_integer('-10.50') == -11

def test_closest_integer_large_positive_number():
    assert closest_integer('1234567.89') == 1234568

def test_closest_integer_large_negative_number():
    assert closest_integer('-1234567.89') == -1234568

def test_closest_integer_small_positive_number():
    assert closest_integer('0.1') == 0

def test_closest_integer_small_negative_number():
    assert closest_integer('-0.1') == 0

def test_closest_integer_positive_point_five():
    assert closest_integer('0.5') == 1

def test_closest_integer_negative_point_five():
    assert closest_integer('-0.5') == -1

def test_closest_integer_multiple_decimal_places():
    assert closest_integer('10.12345') == 10

def test_closest_integer_negative_multiple_decimal_places():
    assert closest_integer('-10.12345') == -10

def test_closest_integer_positive_almost_integer():
    assert closest_integer('9.99999') == 10

def test_closest_integer_negative_almost_integer():
    assert closest_integer('-9.99999') == -10

def test_closest_integer_positive_float_many_nines():
    assert closest_integer('2.9999999999999999') == 3

def test_closest_integer_negative_float_many_nines():
    assert closest_integer('-2.9999999999999999') == -3

def test_closest_integer_positive_float_many_zeros():
    assert closest_integer('2.0000000000000001') == 2

def test_closest_integer_negative_float_many_zeros():
    assert closest_integer('-2.0000000000000001') == -2

def test_closest_integer_zero_point_zero():
    assert closest_integer('0.0') == 0

def test_closest_integer_negative_zero_point_zero():
    assert closest_integer('-0.0') == 0

def test_closest_integer_positive_number_with_leading_and_trailing_zeros():
    assert closest_integer('0010.500') == 11

def test_closest_integer_negative_number_with_leading_and_trailing_zeros():
    assert closest_integer('-0010.500') == -11

def test_closest_integer_positive_number_with_leading_zeros():
    assert closest_integer('0010') == 10

def test_closest_integer_negative_number_with_leading_zeros():
    assert closest_integer('-0010') == -10

def test_closest_integer_very_small_positive_number():
    assert closest_integer('0.0000000000000001') == 0

def test_closest_integer_very_small_negative_number():
    assert closest_integer('-0.0000000000000001') == 0