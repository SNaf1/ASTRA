import pytest
from source_to_mutate import parse_nested_parens, METADATA

def test_empty_string():
    assert parse_nested_parens('') == []

def test_single_empty_group():
    assert parse_nested_parens(' ') == []

def test_single_group_no_nesting():
    assert parse_nested_parens('()') == [1]

def test_single_group_simple_nesting():
    assert parse_nested_parens('(())') == [2]

def test_single_group_multiple_nesting():
    assert parse_nested_parens('((()))') == [3]

def test_multiple_groups_no_nesting():
    assert parse_nested_parens('() () ()') == [1, 1, 1]

def test_multiple_groups_mixed_nesting():
    assert parse_nested_parens('() (()) ((()))') == [1, 2, 3]

def test_complex_example():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

def test_group_with_unbalanced_parentheses():
    assert parse_nested_parens('(()') == [2]

def test_group_with_unbalanced_parentheses_2():
    assert parse_nested_parens('))') == [0]

def test_group_with_unbalanced_parentheses_mixed():
    assert parse_nested_parens('(()))') == [2]

def test_multiple_groups_with_unbalanced_parentheses():
    assert parse_nested_parens('(())) (())') == [2, 2]

def test_group_with_only_closing_parentheses():
    assert parse_nested_parens(')') == [0]

def test_group_with_only_opening_parentheses():
    assert parse_nested_parens('(') == [1]

def test_multiple_spaces():
    assert parse_nested_parens('  ()  (())  ') == [1, 2]

def test_group_with_internal_spaces():
    assert parse_nested_parens('()  (())') == [1, 2]

def test_long_nested_group():
    assert parse_nested_parens('((((((((((((((((((()))))))))))))))))))))') == [19]

def test_metadata():
    assert METADATA['author'] == 'jt'
    assert METADATA['dataset'] == 'test'