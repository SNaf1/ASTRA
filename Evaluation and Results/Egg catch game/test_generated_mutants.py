import pytest
from selected_functions import *

@pytest.fixture(autouse=True)
def reset_state():
    import selected_functions
    selected_functions.eggs.clear()
    selected_functions.score = 0
    selected_functions.lives_remaining = 3
    if hasattr(selected_functions, 'egg_speed'):
        selected_functions.egg_speed = 500
    if hasattr(selected_functions, 'egg_interval'):
        selected_functions.egg_interval = 1000
    if hasattr(selected_functions, 'difficulty'):
        selected_functions.difficulty = 0.9

def test_increase_score():
    import selected_functions
    selected_functions.score = 0
    selected_functions.egg_speed = 500
    selected_functions.egg_interval = 1000
    selected_functions.difficulty = 0.9
    increase_score(10)
    assert selected_functions.score == 10
    assert selected_functions.egg_speed == int(500 * 0.9)
    assert selected_functions.egg_interval == int(1000 * 0.9)

def test_increase_score_multiple_times():
    import selected_functions
    selected_functions.score = 0
    selected_functions.egg_speed = 500
    selected_functions.egg_interval = 1000
    selected_functions.difficulty = 0.9
    increase_score(10)
    increase_score(5)
    assert selected_functions.score == 15
    assert selected_functions.egg_speed == int(int(500 * 0.9) * 0.9)
    assert selected_functions.egg_interval == int(int(1000 * 0.9) * 0.9)

def test_lose_a_life():
    import selected_functions
    selected_functions.lives_remaining = 3
    lose_a_life()
    assert selected_functions.lives_remaining == 2

def test_lose_all_lives():
    import selected_functions
    selected_functions.lives_remaining = 1
    lose_a_life()
    assert selected_functions.lives_remaining == 0

# Since move_eggs, egg_dropped, check_catch, move_left, and move_right rely heavily on tkinter and canvas interactions,
# creating isolated unit tests without mocking the tkinter environment is extremely difficult and not very useful.
# These tests would essentially become integration tests requiring a running tkinter application.
# Skipping these tests.