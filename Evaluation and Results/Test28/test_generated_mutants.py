import pytest
from source_to_mutate import concatenate

def test_concatenate_empty_list():
    assert concatenate([]) == ""

def test_concatenate_single_string():
    assert concatenate(["hello"]) == "hello"

def test_concatenate_multiple_strings():
    assert concatenate(["a", "b", "c"]) == "abc"

def test_concatenate_strings_with_spaces():
    assert concatenate(["hello", " ", "world"]) == "hello world"

def test_concatenate_strings_with_numbers():
    assert concatenate(["1", "2", "3"]) == "123"

def test_concatenate_strings_with_special_characters():
    assert concatenate(["!", "@", "#"]) == "!@#"

def test_concatenate_mixed_strings():
    assert concatenate(["a", "1", "!", "b"]) == "a1!b"

def test_concatenate_long_strings():
    assert concatenate(["This is a long", " string"]) == "This is a long string"

def test_concatenate_empty_strings():
    assert concatenate(["", "", ""]) == ""

def test_concatenate_list_with_empty_string():
    assert concatenate(["a", "", "b"]) == "ab"