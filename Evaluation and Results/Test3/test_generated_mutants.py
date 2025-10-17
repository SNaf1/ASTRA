import pytest
from source_to_mutate import below_zero


def test_empty_operations():
    assert below_zero([]) == False


def test_all_positive_operations():
    assert below_zero([1, 2, 3]) == False


def test_single_negative_operation():
    assert below_zero([-1]) == True


def test_single_positive_operation():
    assert below_zero([1]) == False


def test_mixed_operations_below_zero():
    assert below_zero([1, 2, -4, 5]) == True


def test_mixed_operations_not_below_zero():
    assert below_zero([1, 2, -2, 5]) == False


def test_multiple_negative_operations():
    assert below_zero([-1, -2, -3]) == True


def test_large_positive_operations():
    assert below_zero([1000, 2000, 3000]) == False


def test_large_negative_operations():
    assert below_zero([-1000, -2000, -3000]) == True


def test_zero_operations():
    assert below_zero([0, 0, 0]) == False


def test_mixed_operations_zero_balance():
    assert below_zero([1, -1, 1, -1]) == False


def test_mixed_operations_below_zero_at_end():
    assert below_zero([1, 2, 3, -10]) == True


def test_mixed_operations_below_zero_multiple_times():
    assert below_zero([-1, 2, -3, 4, -5]) == True


def test_mixed_operations_large_numbers():
    assert below_zero([100, -50, 200, -300, 50]) == True


def test_mixed_operations_equal_positive_and_negative():
    assert below_zero([5, -5, 10, -10, 0]) == False