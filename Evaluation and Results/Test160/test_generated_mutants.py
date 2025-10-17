import pytest
from source_to_mutate import do_algebra

def test_addition_and_multiplication():
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_subtraction_and_division():
    operator = ['-', '//']
    operand = [10, 5, 2]
    assert do_algebra(operator, operand) == 8

def test_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_multiple_operations():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_only_addition():
    operator = ['+']
    operand = [1, 2]
    assert do_algebra(operator, operand) == 3

def test_only_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_only_multiplication():
    operator = ['*']
    operand = [3, 4]
    assert do_algebra(operator, operand) == 12

def test_only_division():
    operator = ['//']
    operand = [10, 3]
    assert do_algebra(operator, operand) == 3

def test_complex_expression():
    operator = ['+', '*', '//', '-']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == -3

def test_large_numbers():
    operator = ['+', '*']
    operand = [1000, 2000, 3000]
    assert do_algebra(operator, operand) == 6001000

def test_zero_values():
    operator = ['+', '*']
    operand = [0, 1, 2]
    assert do_algebra(operator, operand) == 2

def test_zero_division():
    operator = ['//']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_exponentiation_with_zero():
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1

def test_exponentiation_with_one():
    operator = ['**']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_negative_result():
    operator = ['-']
    operand = [1, 5]
    assert do_algebra(operator, operand) == -4

def test_multiple_exponentiations():
    operator = ['**', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 512

def test_division_by_zero_handled_by_eval():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)