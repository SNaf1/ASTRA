import pytest
from source_to_mutate import correct_bracketing, METADATA

def test_empty_string():
    assert correct_bracketing("") == True

def test_single_opening_bracket():
    assert correct_bracketing("(") == False

def test_single_closing_bracket():
    assert correct_bracketing(")") == False

def test_matching_brackets():
    assert correct_bracketing("()") == True

def test_nested_matching_brackets():
    assert correct_bracketing("(())") == True

def test_multiple_matching_brackets():
    assert correct_bracketing("()()") == True

def test_nested_and_multiple_matching_brackets():
    assert correct_bracketing("(()())") == True

def test_unbalanced_brackets_opening_first():
    assert correct_bracketing("((())") == False

def test_unbalanced_brackets_closing_first():
    assert correct_bracketing(")(()") == False

def test_long_balanced_brackets():
    assert correct_bracketing("((((()))))") == True

def test_long_unbalanced_brackets_opening():
    assert correct_bracketing("((((())))))(") == False

def test_long_unbalanced_brackets_closing():
    assert correct_bracketing("((((())))))(((") == False

def test_only_opening_brackets():
    assert correct_bracketing("(((((") == False

def test_only_closing_brackets():
    assert correct_bracketing(")))))") == False

def test_alternating_unbalanced():
    assert correct_bracketing("(()))(") == False

def test_alternating_balanced():
    assert correct_bracketing("(())(())") == True