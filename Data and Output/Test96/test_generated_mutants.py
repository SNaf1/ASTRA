import pytest
from source_to_mutate import count_up_to

def test_count_up_to_5():
    assert count_up_to(5) == [2, 3]

def test_count_up_to_11():
    assert count_up_to(11) == [2, 3, 5, 7]

def test_count_up_to_0():
    assert count_up_to(0) == []

def test_count_up_to_20():
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_count_up_to_1():
    assert count_up_to(1) == []

def test_count_up_to_18():
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

def test_count_up_to_2():
    assert count_up_to(2) == []

def test_count_up_to_3():
    assert count_up_to(3) == [2]

def test_count_up_to_4():
    assert count_up_to(4) == [2, 3]

def test_count_up_to_6():
    assert count_up_to(6) == [2, 3, 5]

def test_count_up_to_7():
    assert count_up_to(7) == [2, 3, 5]

def test_count_up_to_8():
    assert count_up_to(8) == [2, 3, 5, 7]

def test_count_up_to_9():
    assert count_up_to(9) == [2, 3, 5, 7]

def test_count_up_to_10():
    assert count_up_to(10) == [2, 3, 5, 7]