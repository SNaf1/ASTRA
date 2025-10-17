import pytest
from source_to_mutate import eat

def test_eat_enough_remaining():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_all_remaining():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_more_than_remaining():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_number():
    assert eat(0, 5, 5) == [5, 0]

def test_eat_zero_need():
    assert eat(5, 0, 5) == [5, 5]

def test_eat_zero_remaining():
    assert eat(5, 5, 0) == [5, 0]

def test_eat_zero_all():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_max_number():
    assert eat(1000, 1, 1) == [1001, 0]

def test_eat_max_need():
    assert eat(1, 1000, 1) == [2, 0]

def test_eat_max_remaining():
    assert eat(1, 1, 1000) == [2, 999]

def test_eat_max_all():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_need_equals_remaining():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

def test_eat_number_equals_remaining():
    assert eat(5, 10, 5) == [10, 0]