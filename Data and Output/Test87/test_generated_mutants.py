import pytest
from source_to_mutate import get_row

def test_empty_list():
    assert get_row([], 1) == []

def test_empty_rows():
    assert get_row([[], [], []], 1) == []

def test_single_element_list_found():
    assert get_row([[1]], 1) == [(0, 0)]

def test_single_element_list_not_found():
    assert get_row([[2]], 1) == []

def test_multiple_rows_different_lengths():
    lst = [[1, 2, 3], [1, 2], [1]]
    assert get_row(lst, 1) == [(0, 0), (1, 0), (2, 0)]

def test_multiple_occurrences_in_same_row():
    lst = [[1, 1, 1]]
    assert get_row(lst, 1) == [(0, 2), (0, 1), (0, 0)]

def test_multiple_occurrences_in_different_rows():
    lst = [[1, 2], [3, 1], [1, 4]]
    assert get_row(lst, 1) == [(0, 0), (1, 1), (2, 0)]

def test_no_occurrences():
    lst = [[2, 3], [4, 5], [6, 7]]
    assert get_row(lst, 1) == []

def test_example_1():
    lst = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]]
    assert get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

def test_example_2():
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

def test_large_list():
    lst = [[i + j for j in range(10)] for i in range(10)]
    assert get_row(lst, 5) == [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]

def test_negative_numbers():
    lst = [[-1, 2], [1, -2]]
    assert get_row(lst, 1) == [(1, 0)]

def test_zero():
    lst = [[0, 1], [1, 0]]
    assert get_row(lst, 0) == [(0, 0), (1, 1)]

def test_duplicate_rows():
    lst = [[1, 2], [1, 2], [1, 2]]
    assert get_row(lst, 1) == [(0, 0), (1, 0), (2, 0)]

def test_x_is_string():
    lst = [[1, 2], [1, 2]]
    assert get_row(lst, '1') == []