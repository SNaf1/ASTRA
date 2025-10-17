import pytest
from source_to_mutate import sum_product, METADATA


def test_empty_list():
    assert sum_product([]) == (0, 1)


def test_single_element_list():
    assert sum_product([5]) == (5, 5)


def test_positive_numbers():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_negative_numbers():
    assert sum_product([-1, -2, -3]) == (-6, -6)


def test_mixed_numbers():
    assert sum_product([-1, 2, -3, 4]) == (2, 24)


def test_zero_in_list():
    assert sum_product([1, 2, 0, 4]) == (7, 0)


def test_large_numbers():
    assert sum_product([100, 200, 300]) == (600, 6000000)


def test_duplicate_numbers():
    assert sum_product([2, 2, 2, 2]) == (8, 16)


def test_negative_and_zero():
    assert sum_product([-1, 0, -2]) == (-3, 0)


def test_metadata():
    assert METADATA['author'] == 'jt'
    assert METADATA['dataset'] == 'test'