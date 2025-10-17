import pytest
from source_to_mutate import get_max_triples

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

def test_get_max_triples_three():
    assert get_max_triples(3) == 0

def test_get_max_triples_four():
    assert get_max_triples(4) == 1

def test_get_max_triples_five():
    assert get_max_triples(5) == 1

def test_get_max_triples_six():
    assert get_max_triples(6) == 4

def test_get_max_triples_seven():
    assert get_max_triples(7) == 10

def test_get_max_triples_eight():
    assert get_max_triples(8) == 11

def test_get_max_triples_nine():
    assert get_max_triples(9) == 21

def test_get_max_triples_ten():
    assert get_max_triples(10) == 36