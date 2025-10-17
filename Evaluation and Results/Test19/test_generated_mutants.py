import pytest
from source_to_mutate import sort_numbers

def test_empty_string():
    assert sort_numbers('') == ''

def test_single_number():
    assert sort_numbers('one') == 'one'

def test_multiple_numbers():
    assert sort_numbers('three one five') == 'one three five'

def test_numbers_already_sorted():
    assert sort_numbers('one two three') == 'one two three'

def test_numbers_reverse_sorted():
    assert sort_numbers('three two one') == 'one two three'

def test_duplicate_numbers():
    assert sort_numbers('one one two') == 'one one two'

def test_all_same_number():
    assert sort_numbers('two two two') == 'two two two'

def test_all_numbers():
    assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'

def test_leading_and_trailing_spaces():
    assert sort_numbers('  one two  ') == 'one two'

def test_multiple_spaces_between_numbers():
    assert sort_numbers('one   two') == 'one two'

def test_numbers_with_mixed_spaces():
    assert sort_numbers(' one  two three ') == 'one two three'

def test_numbers_with_zero():
    assert sort_numbers('zero one two') == 'zero one two'

def test_numbers_with_nine():
    assert sort_numbers('nine eight seven') == 'seven eight nine'

def test_numbers_with_all_digits():
    assert sort_numbers('one two three four five six seven eight nine zero') == 'zero one two three four five six seven eight nine'