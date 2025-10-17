import pytest
from source_to_mutate import has_close_elements, METADATA, check

def test_empty_list():
    assert has_close_elements([], 0.5) == False

def test_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_identical_elements():
    assert has_close_elements([1.0, 1.0, 1.0], 0.5) == True

def test_negative_numbers():
    assert has_close_elements([-1.0, -2.0, -3.0, -1.1], 0.2) == True

def test_mixed_positive_negative():
    assert has_close_elements([-1.0, 1.0], 2.1) == True

def test_threshold_zero():
    assert has_close_elements([1.0, 1.0], 0.0) == False

def test_large_threshold():
    assert has_close_elements([1.0, 5.0], 10.0) == True

def test_large_numbers():
    assert has_close_elements([1000.0, 1000.1], 0.2) == True

def test_duplicate_numbers_far_apart():
    assert has_close_elements([1.0, 2.0, 3.0, 1.0], 0.5) == True

def test_close_elements_near_end():
    assert has_close_elements([1.0, 2.0, 2.1], 0.2) == True

def test_close_elements_near_beginning():
    assert has_close_elements([2.1, 2.0, 1.0], 0.2) == True

def test_threshold_equal_to_distance():
    assert has_close_elements([1.0, 2.0], 1.0) == False

def test_example_1():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True

def test_example_2():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False

def test_example_3():
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True

def test_example_4():
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False

def test_example_5():
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True

def test_example_6():
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True

def test_example_7():
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False