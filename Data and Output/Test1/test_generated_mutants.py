import pytest
from source_to_mutate import separate_paren_groups, METADATA, check

def test_empty_string():
    assert separate_paren_groups('') == []

def test_single_group():
    assert separate_paren_groups('()') == ['()']

def test_multiple_groups():
    assert separate_paren_groups('() (()) ((()))') == ['()', '(())', '((()))']

def test_nested_groups():
    assert separate_paren_groups('(()(())((())))') == ['(()(())((())))']

def test_mixed_groups():
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']

def test_with_spaces():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_unbalanced_parentheses():
    assert separate_paren_groups('(') == []

def test_unbalanced_parentheses_2():
    assert separate_paren_groups(')') == []

def test_unbalanced_parentheses_mixed():
    assert separate_paren_groups('(()') == []

def test_unbalanced_parentheses_mixed_2():
    assert separate_paren_groups('))') == []

def test_nested_and_unbalanced():
    assert separate_paren_groups('((())') == []

def test_nested_and_unbalanced_2():
    assert separate_paren_groups('(()))') == ['(())']

def test_complex_nested():
    assert separate_paren_groups('(((())))') == ['(((())))']

def test_complex_nested_multiple():
    assert separate_paren_groups('(((()))) ((()))') == ['(((())))', '((()))']

def test_empty_groups():
    assert separate_paren_groups('  ') == []

def test_only_spaces_and_parentheses():
    assert separate_paren_groups(' ( )  ( ( ) ) ') == ['()', '(())']

def test_long_string():
    assert separate_paren_groups('()()()()()()()()()()') == ['()', '()', '()', '()', '()', '()', '()', '()', '()', '()']

def test_long_nested_string():
    assert separate_paren_groups('((((((((((())))))))))))') == ['((((((((((()))))))))))']