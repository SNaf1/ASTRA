import pytest
from source_to_mutate import intersection

def test_intersection_no_intersection():
    assert intersection((1, 2), (3, 4)) == 'NO'

def test_intersection_one_point_intersection():
    assert intersection((1, 2), (2, 3)) == 'NO'

def test_intersection_prime_length():
    assert intersection((-3, -1), (-5, 5)) == 'YES'

def test_intersection_non_prime_length():
    assert intersection((-1, 1), (0, 4)) == 'NO'

def test_intersection_identical_intervals():
    assert intersection((1, 5), (1, 5)) == 'NO'

def test_intersection_interval1_inside_interval2():
    assert intersection((2, 3), (1, 4)) == 'NO'

def test_intersection_interval2_inside_interval1():
    assert intersection((1, 4), (2, 3)) == 'NO'

def test_intersection_negative_intervals():
    assert intersection((-5, -3), (-4, -2)) == 'NO'

def test_intersection_zero_length():
    assert intersection((1, 1), (1, 1)) == 'NO'

def test_intersection_large_numbers():
    assert intersection((1000, 1002), (1001, 1003)) == 'NO'

def test_intersection_negative_and_positive():
    assert intersection((-2, 0), (0, 2)) == 'NO'

def test_intersection_overlapping_negative():
    assert intersection((-5, -2), (-3, -1)) == 'NO'

def test_intersection_overlapping_positive():
    assert intersection((2, 5), (3, 6)) == 'YES'

def test_intersection_adjacent_intervals():
    assert intersection((1, 3), (3, 5)) == 'NO'

def test_intersection_same_start():
    assert intersection((2, 5), (2, 4)) == 'YES'

def test_intersection_same_end():
    assert intersection((2, 5), (3, 5)) == 'YES'

def test_intersection_zero_start():
    assert intersection((0, 2), (1, 3)) == 'NO'

def test_intersection_zero_end():
    assert intersection((-2, 0), (-1, 1)) == 'NO'

def test_intersection_equal_start_and_end():
    assert intersection((5, 5), (5, 6)) == 'NO'

def test_intersection_equal_start_and_end_negative():
    assert intersection((-5, -5), (-6, -5)) == 'NO'