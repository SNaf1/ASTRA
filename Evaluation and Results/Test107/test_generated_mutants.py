import pytest
from source_to_mutate import even_odd_palindrome

def test_even_odd_palindrome_example_1():
    assert even_odd_palindrome(3) == (1, 2)

def test_even_odd_palindrome_example_2():
    assert even_odd_palindrome(12) == (4, 6)

def test_even_odd_palindrome_1():
    assert even_odd_palindrome(1) == (0, 1)

def test_even_odd_palindrome_2():
    assert even_odd_palindrome(2) == (1, 1)

def test_even_odd_palindrome_9():
    assert even_odd_palindrome(9) == (4, 5)

def test_even_odd_palindrome_10():
    assert even_odd_palindrome(10) == (4, 5)

def test_even_odd_palindrome_11():
    assert even_odd_palindrome(11) == (4, 6)

def test_even_odd_palindrome_99():
    assert even_odd_palindrome(99) == (8, 10)

def test_even_odd_palindrome_100():
    assert even_odd_palindrome(100) == (8, 10)

def test_even_odd_palindrome_101():
    assert even_odd_palindrome(101) == (8, 11)

def test_even_odd_palindrome_999():
    assert even_odd_palindrome(999) == (48, 60)

def test_even_odd_palindrome_1000():
    assert even_odd_palindrome(1000) == (48, 60)