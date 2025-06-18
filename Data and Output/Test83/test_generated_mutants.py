import pytest
from source_to_mutate import starts_one_ends

def test_starts_one_ends_1():
    assert starts_one_ends(1) == 1

def test_starts_one_ends_2():
    assert starts_one_ends(2) == 18

def test_starts_one_ends_3():
    assert starts_one_ends(3) == 180

def test_starts_one_ends_4():
    assert starts_one_ends(4) == 1800

def test_starts_one_ends_5():
    assert starts_one_ends(5) == 18000

def test_starts_one_ends_6():
    assert starts_one_ends(6) == 180000

def test_starts_one_ends_7():
    assert starts_one_ends(7) == 1800000

def test_starts_one_ends_8():
    assert starts_one_ends(8) == 18000000

def test_starts_one_ends_9():
    assert starts_one_ends(9) == 180000000

def test_starts_one_ends_10():
    assert starts_one_ends(10) == 1800000000