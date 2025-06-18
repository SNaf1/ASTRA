import pytest
from source_to_mutate import iscube

def test_iscube_positive_cube():
    assert iscube(8) == True

def test_iscube_negative_cube():
    assert iscube(-8) == True

def test_iscube_zero():
    assert iscube(0) == True

def test_iscube_one():
    assert iscube(1) == True

def test_iscube_positive_non_cube():
    assert iscube(2) == False

def test_iscube_large_cube():
    assert iscube(1728) == True

def test_iscube_large_non_cube():
    assert iscube(180) == False

def test_iscube_negative_non_cube():
    assert iscube(-2) == False

def test_iscube_perfect_cube():
    assert iscube(64) == True

def test_iscube_large_negative_cube():
    assert iscube(-2197) == True

def test_iscube_fractional_cube_close_to_integer():
    assert iscube(7.999999999999999) == False

def test_iscube_large_number():
    assert iscube(9261) == True

def test_iscube_very_large_cube():
    assert iscube(10648) == True