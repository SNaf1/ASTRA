import pytest
from source_to_mutate import compare

def test_compare_correct_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_incorrect_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [2, 3, 4, 5, 6, 2]
    expected = [1, 1, 1, 1, 1, 1]
    assert compare(game, guess) == expected

def test_compare_mixed_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_compare_all_incorrect():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    game = []
    guess = []
    expected = []
    assert compare(game, guess) == expected

def test_compare_single_element_correct():
    game = [5]
    guess = [5]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_single_element_incorrect():
    game = [5]
    guess = [10]
    expected = [5]
    assert compare(game, guess) == expected

def test_compare_negative_numbers():
    game = [-1, -2, -3]
    guess = [-1, -3, -2]
    expected = [0, 1, 1]
    assert compare(game, guess) == expected

def test_compare_zero_values():
    game = [0, 0, 0]
    guess = [1, -1, 0]
    expected = [1, 1, 0]
    assert compare(game, guess) == expected

def test_compare_large_numbers():
    game = [1000, 2000, 3000]
    guess = [1001, 1999, 3000]
    expected = [1, 1, 0]
    assert compare(game, guess) == expected