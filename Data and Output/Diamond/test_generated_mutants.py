import pytest
from source_to_mutate import rows, make_half

def test_rows_A():
    expected = ["A"]
    assert rows("A") == expected

def test_rows_B():
    expected = [' A ', 'B B', ' A ']
    assert rows("B") == expected

def test_rows_C():
    expected = ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
    assert rows("C") == ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']

def test_make_half_1_1():
    expected = ['A']
    assert make_half(1, 1) == expected

def test_make_half_2_3():
    expected = [' A ', 'B B']
    assert make_half(2, 3) == [' A ', 'B B']

def test_make_half_3_5():
    expected = ['  A  ', ' B B ', 'C   C']
    assert make_half(3, 5) == ['  A  ', ' B B ', 'C   C']

def test_rows_D():
    expected = ['   A   ', '  B B  ', ' C   C ', 'D     D', ' C   C ', '  B B  ', '   A   ']
    assert rows("D") == ['   A   ', '  B B  ', ' C   C ', 'D     D', ' C   C ', '  B B  ', '   A   ']

def test_rows_E():
    expected = ['    A    ', '   B B   ', '  C   C  ', ' D     D ', 'E       E', ' D     D ', '  C   C  ', '   B B   ', '    A    ']
    assert rows("E") == ['    A    ', '   B B   ', '  C   C  ', ' D     D ', 'E       E', ' D     D ', '  C   C  ', '   B B   ', '    A    ']