import pytest
from source_to_mutate import intersperse


def test_empty_list():
    assert intersperse([], 4) == []


def test_single_element_list():
    assert intersperse([1], 4) == [1]


def test_multiple_elements_list():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_negative_numbers():
    assert intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]


def test_zero_delimeter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]


def test_negative_delimeter():
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]


def test_mixed_numbers_and_delimeter():
    assert intersperse([-1, 0, 1], 2) == [-1, 2, 0, 2, 1]


def test_large_numbers():
    assert intersperse([1000, 2000, 3000], 500) == [1000, 500, 2000, 500, 3000]


def test_same_numbers():
    assert intersperse([5, 5, 5], 5) == [5, 5, 5, 5, 5]


def test_list_with_one_element_and_negative_delimeter():
    assert intersperse([1], -5) == [1]