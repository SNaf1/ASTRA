import pytest
from source_to_mutate import tri

def test_tri_0():
    assert tri(0) == [1]

def test_tri_1():
    assert tri(1) == [1, 3]

def test_tri_2():
    assert tri(2) == [1, 3, 2.0]

def test_tri_3():
    assert tri(3) == [1, 3, 2.0, 8.0]

def test_tri_4():
    assert tri(4) == [1, 3, 2.0, 8.0, 3.0]

def test_tri_5():
    assert tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]

def test_tri_6():
    assert tri(6) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]

def test_tri_7():
    assert tri(7) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0]

def test_tri_8():
    assert tri(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]

def test_tri_9():
    assert tri(9) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0]

def test_tri_10():
    assert tri(10) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0, 6.0]