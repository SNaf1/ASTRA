import pytest
from source_to_mutate import solve

def test_solve_1000():
    assert solve(1000) == '1'

def test_solve_150():
    assert solve(150) == '110'

def test_solve_147():
    assert solve(147) == '1100'

def test_solve_0():
    assert solve(0) == '0'

def test_solve_1():
    assert solve(1) == '1'

def test_solve_9():
    assert solve(9) == '1001'

def test_solve_10():
    assert solve(10) == '1'

def test_solve_99():
    assert solve(99) == '10010'

def test_solve_100():
    assert solve(100) == '1'

def test_solve_999():
    assert solve(999) == '11011'

def test_solve_10000():
    assert solve(10000) == '1'