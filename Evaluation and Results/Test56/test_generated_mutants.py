import pytest
from source_to_mutate import correct_bracketing, METADATA

def test_empty_string():
    assert correct_bracketing("") == True

def test_single_opening_bracket():
    assert correct_bracketing("<") == False

def test_single_closing_bracket():
    assert correct_bracketing(">") == False

def test_matching_brackets():
    assert correct_bracketing("<>") == True

def test_multiple_matching_brackets():
    assert correct_bracketing("<><>") == True

def test_nested_matching_brackets():
    assert correct_bracketing("<<>>") == True

def test_complex_matching_brackets():
    assert correct_bracketing("<<><>>") == True

def test_unclosed_opening_brackets():
    assert correct_bracketing("<<>") == False

def test_unclosed_closing_brackets():
    assert correct_bracketing("<>>") == False

def test_mixed_unclosed_brackets():
    assert correct_bracketing("><<>") == False

def test_only_opening_brackets():
    assert correct_bracketing("<<<") == False

def test_only_closing_brackets():
    assert correct_bracketing(">>>") == False

def test_long_matching_brackets():
    assert correct_bracketing("<<<<>>>>") == True

def test_long_unclosed_opening_brackets():
    assert correct_bracketing("<<<<>") == False

def test_long_unclosed_closing_brackets():
    assert correct_bracketing("<>>>>") == False

def test_alternating_unclosed_brackets():
    assert correct_bracketing("><><><") == False

def test_alternating_unclosed_brackets_2():
    assert correct_bracketing("<><><>") == True

def test_nested_and_sequential():
    assert correct_bracketing("<<>><>") == True

def test_nested_and_sequential_unclosed():
    assert correct_bracketing("<<>><") == False