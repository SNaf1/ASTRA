import pytest
from source_to_mutate import numerical_letter_grade

def test_empty_list():
    assert numerical_letter_grade([]) == []

def test_single_a_plus():
    assert numerical_letter_grade([4.0]) == ['A+']

def test_single_a():
    assert numerical_letter_grade([3.8]) == ['A']

def test_single_a_minus():
    assert numerical_letter_grade([3.4]) == ['A-']

def test_single_b_plus():
    assert numerical_letter_grade([3.1]) == ['B+']

def test_single_b():
    assert numerical_letter_grade([2.8]) == ['B']

def test_single_b_minus():
    assert numerical_letter_grade([2.4]) == ['B-']

def test_single_c_plus():
    assert numerical_letter_grade([2.1]) == ['C+']

def test_single_c():
    assert numerical_letter_grade([1.8]) == ['C']

def test_single_c_minus():
    assert numerical_letter_grade([1.4]) == ['C-']

def test_single_d_plus():
    assert numerical_letter_grade([1.1]) == ['D+']

def test_single_d():
    assert numerical_letter_grade([0.8]) == ['D']

def test_single_d_minus():
    assert numerical_letter_grade([0.1]) == ['D-']

def test_single_e():
    assert numerical_letter_grade([0.0]) == ['E']

def test_multiple_grades():
    grades = [4.0, 3.8, 3.4, 3.1, 2.8, 2.4, 2.1, 1.8, 1.4, 1.1, 0.8, 0.1, 0.0]
    expected_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    assert numerical_letter_grade(grades) == expected_grades

def test_example_grades():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

def test_boundary_values():
    grades = [3.71, 3.31, 3.01, 2.71, 2.31, 2.01, 1.71, 1.31, 1.01, 0.71, 0.01]
    expected_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
    assert numerical_letter_grade(grades) == expected_grades

def test_gpa_equal_to_3_7():
    assert numerical_letter_grade([3.7]) == ['A-']

def test_gpa_equal_to_3_3():
    assert numerical_letter_grade([3.3]) == ['B+']

def test_gpa_equal_to_3_0():
    assert numerical_letter_grade([3.0]) == ['B']

def test_gpa_equal_to_2_7():
    assert numerical_letter_grade([2.7]) == ['B-']

def test_gpa_equal_to_2_3():
    assert numerical_letter_grade([2.3]) == ['C+']

def test_gpa_equal_to_2_0():
    assert numerical_letter_grade([2.0]) == ['C']

def test_gpa_equal_to_1_7():
    assert numerical_letter_grade([1.7]) == ['C-']

def test_gpa_equal_to_1_3():
    assert numerical_letter_grade([1.3]) == ['D+']

def test_gpa_equal_to_1_0():
    assert numerical_letter_grade([1.0]) == ['D']

def test_gpa_equal_to_0_7():
    assert numerical_letter_grade([0.7]) == ['D-']