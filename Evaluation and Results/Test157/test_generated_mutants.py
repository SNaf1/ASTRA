import pytest
from source_to_mutate import right_angle_triangle

def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_different_order():
    assert right_angle_triangle(5, 3, 4) == True

def test_right_angle_triangle_another_true():
    assert right_angle_triangle(5, 12, 13) == True

def test_right_angle_triangle_another_false():
    assert right_angle_triangle(2, 3, 4) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == True

def test_right_angle_triangle_one_zero():
    assert right_angle_triangle(0, 1, 1) == True

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(65, 72, 97) == True

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_almost_right():
    assert right_angle_triangle(3, 4, 5.1) == False

def test_right_angle_triangle_float_values():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_right_angle_triangle_float_false():
    assert right_angle_triangle(1.1, 2.2, 3.3) == False

def test_right_angle_triangle_negative_input():
    assert right_angle_triangle(-3, 4, 5) == True

def test_right_angle_triangle_negative_and_zero():
    assert right_angle_triangle(-3, 0, 3) == True