import pytest
from source_to_mutate import is_iterable, flatten

def test_is_iterable_list():
    assert is_iterable([1, 2, 3]) == True

def test_is_iterable_string():
    assert is_iterable('hello') == True

def test_is_iterable_int():
    assert is_iterable(123) == False

def test_is_iterable_tuple():
    assert is_iterable((1, 2)) == True

def test_is_iterable_set():
    assert is_iterable({1, 2}) == True

def test_is_iterable_dict():
    assert is_iterable({'a': 1}) == True

def test_is_iterable_bytes():
    assert is_iterable(b'abc') == True

def test_is_iterable_none():
    assert is_iterable(None) == False

def test_flatten_empty_list():
    assert flatten([]) == []

def test_flatten_single_level_list():
    assert flatten([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    assert flatten([1, [2, [3, 4]]]) == [1, 2, 3, 4]

def test_flatten_mixed_types():
    assert flatten([1, [2, 'hello']]) == [1, 2, 'hello']

def test_flatten_with_none():
    assert flatten([1, None, [2, None]]) == [1, 2]

def test_flatten_with_string():
    assert flatten([1, 'hello', [2, 'world']]) == [1, 'hello', 2, 'world']

def test_flatten_with_bytes():
    assert flatten([1, b'hello', [2, b'world']]) == [1, b'hello', 2, b'world']

def test_flatten_with_empty_list():
    assert flatten([1, [], 2]) == [1, 2]

def test_flatten_with_empty_nested_list():
    assert flatten([[[]]]) == []

def test_flatten_with_none_and_empty_list():
    assert flatten([None, []]) == []

def test_flatten_with_tuple():
    assert flatten([(1, 2), (3, 4)]) == [1, 2, 3, 4]

def test_flatten_with_nested_tuple():
    assert flatten([1, [(2, 3), 4]]) == [1, 2, 3, 4]

def test_flatten_with_mixed_iterables():
    assert flatten([[1, 2], (3, 4)]) == [1, 2, 3, 4]

def test_flatten_with_string_and_list():
    assert flatten(['abc', [1, 2]]) == ['abc', 1, 2]

def test_flatten_with_bytes_and_list():
    assert flatten([b'abc', [1, 2]]) == [b'abc', 1, 2]

def test_flatten_with_none_in_nested_list():
    assert flatten([[1, None, 2], [3, None, 4]]) == [1, 2, 3, 4]

def test_flatten_with_nested_none():
    assert flatten([1, [None, [2, None]]]) == [1, 2]

def test_flatten_with_nested_empty_lists():
    assert flatten([[], [[]]]) == []