import pytest
from source_to_mutate import is_nested

def test_empty_string():
    assert is_nested('') == False

def test_single_open_bracket():
    assert is_nested('[') == False

def test_single_close_bracket():
    assert is_nested(']') == False

def test_simple_valid_sequence():
    assert is_nested('[]') == False

def test_nested_brackets():
    assert is_nested('[[]]') == True

def test_multiple_unnested_brackets():
    assert is_nested('[][]') == False

def test_unbalanced_brackets_with_nested():
    assert is_nested('[]]]]]]][[[[[]') == False

def test_complex_nested_brackets():
    assert is_nested('[[][]]') == True

def test_complex_nested_brackets_2():
    assert is_nested('[[]][[') == True

def test_only_closing_brackets():
    assert is_nested(']]]]') == False

def test_only_opening_brackets():
    assert is_nested('[[[[') == False

def test_nested_with_extra_closing():
    assert is_nested('[[]]]') == True

def test_nested_with_extra_opening():
    assert is_nested('[[[]') == False

def test_long_nested_sequence():
    assert is_nested('[[[[[[]]]]]]') == True

def test_long_unnested_sequence():
    assert is_nested('[][][][][][]') == True

def test_alternating_brackets():
    assert is_nested('][][][') == False

def test_nested_at_end():
    assert is_nested('[]][[]]') == True

def test_nested_at_start():
    assert is_nested('[[]][]') == True

def test_nested_in_middle():
    assert is_nested('[][[]][]') == True

def test_nested_with_adjacent_unbalanced():
    assert is_nested('[[]][') == True

def test_nested_with_adjacent_unbalanced_2():
    assert is_nested('][[]]') == True

def test_long_string_with_nested_and_unbalanced():
    assert is_nested('[][[[][]]]]') == True

def test_long_string_with_nested_and_unbalanced_2():
    assert is_nested('[[[[[][]]]]][') == True