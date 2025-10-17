import pytest
from source_to_mutate import string_sequence

def test_string_sequence_zero():
    assert string_sequence(0) == '0'

def test_string_sequence_positive():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_one():
    assert string_sequence(1) == '0 1'

def test_string_sequence_large():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'