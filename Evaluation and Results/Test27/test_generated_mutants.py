import pytest
from source_to_mutate import *

def test_empty_string():
    assert flip_case("") == ""

def test_single_lowercase():
    assert flip_case("a") == "A"

def test_single_uppercase():
    assert flip_case("A") == "a"

def test_mixed_case():
    assert flip_case("Hello") == "hELLO"

def test_all_lowercase():
    assert flip_case("hello") == "HELLO"

def test_all_uppercase():
    assert flip_case("HELLO") == "hello"

def test_with_numbers():
    assert flip_case("Hello123") == "hELLO123"

def test_with_special_characters():
    assert flip_case("Hello!") == "hELLO!"

def test_mixed_case_and_numbers():
    assert flip_case("HeLlO123") == "hElLo123"

def test_mixed_case_and_special_characters():
    assert flip_case("HeLlO!") == "hElLo!"

def test_mixed_case_numbers_and_special_characters():
    assert flip_case("HeLlO123!") == "hElLo123!"

def test_string_with_spaces():
    assert flip_case("Hello World") == "hELLO wORLD"

def test_string_with_leading_and_trailing_spaces():
    assert flip_case("  Hello World  ") == "  hELLO wORLD  "

def test_string_with_multiple_spaces():
    assert flip_case("Hello   World") == "hELLO   wORLD"