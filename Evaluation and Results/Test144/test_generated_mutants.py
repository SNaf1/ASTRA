import pytest
from source_to_mutate import simplify

def test_simplify_true_1():
    assert simplify("1/5", "5/1") == True

def test_simplify_false_1():
    assert simplify("1/6", "2/1") == False

def test_simplify_false_2():
    assert simplify("7/10", "10/2") == False

def test_simplify_true_2():
    assert simplify("2/4", "2/1") == True

def test_simplify_true_3():
    assert simplify("1/2", "2/1") == True

def test_simplify_false_3():
    assert simplify("1/3", "2/1") == False

def test_simplify_true_4():
    assert simplify("1/1", "1/1") == True

def test_simplify_false_4():
    assert simplify("1/3", "1/2") == False

def test_simplify_large_numbers_true():
    assert simplify("1000/1", "1/1000") == True

def test_simplify_large_numbers_false():
    assert simplify("1000/3", "1/1000") == False

def test_simplify_same_fraction_true():
    assert simplify("2/2", "1/1") == True

def test_simplify_same_fraction_false():
    assert simplify("2/3", "1/1") == False

def test_simplify_one_numerator_true():
    assert simplify("1/4", "4/1") == True

def test_simplify_one_denominator_true():
    assert simplify("4/1", "1/4") == True

def test_simplify_one_numerator_false():
    assert simplify("1/5", "4/1") == False

def test_simplify_one_denominator_false():
    assert simplify("4/1", "1/5") == False

def test_simplify_complex_true():
    assert simplify("12/4", "2/6") == True

def test_simplify_complex_false():
    assert simplify("12/5", "2/6") == False