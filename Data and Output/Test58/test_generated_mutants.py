import pytest
from source_to_mutate import common, METADATA

@pytest.fixture(autouse=True)
def reset_state():
    global METADATA
    METADATA = {}

def test_empty_lists():
    assert common([], []) == []

def test_one_empty_list():
    assert common([1, 2, 3], []) == []
    assert common([], [1, 2, 3]) == []

def test_no_common_elements():
    assert common([1, 2, 3], [4, 5, 6]) == []

def test_single_common_element():
    assert common([1, 2, 3], [3, 4, 5]) == [3]

def test_multiple_common_elements():
    assert common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_duplicate_elements_in_input_lists():
    assert common([1, 2, 2, 3], [2, 3, 3, 4]) == [2, 3]

def test_common_elements_with_different_order():
    assert common([3, 1, 2], [2, 3, 4]) == [2, 3]

def test_large_lists():
    l1 = list(range(100))
    l2 = list(range(50, 150))
    assert common(l1, l2) == list(range(50, 100))

def test_common_elements_at_the_beginning():
    assert common([1, 2, 3], [1, 2, 4]) == [1, 2]

def test_common_elements_at_the_end():
    assert common([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_common_elements_scattered():
    assert common([1, 3, 5, 7], [2, 3, 6, 7]) == [3, 7]

def test_identical_lists():
    assert common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

def test_lists_with_same_elements_different_counts():
    assert common([1, 1, 2, 2, 3], [1, 2, 3, 3, 3]) == [1, 2, 3]

def test_lists_with_negative_numbers():
    assert common([-1, -2, 0, 1], [-2, 0, 2]) == [-2, 0]

def test_lists_with_zero():
    assert common([0, 1, 2], [0, 2, 3]) == [0, 2]

def test_lists_with_floats():
    assert common([1.0, 2.0, 3.0], [2.0, 3.0, 4.0]) == [2.0, 3.0]

def test_lists_with_mixed_types():
    assert common([1, 2, '3'], [2, 3, 4]) == [2]

def test_lists_with_strings():
    assert common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

def test_lists_with_empty_string():
    assert common(['', 'a', 'b'], ['', 'c', 'b']) == ['', 'b']