import pytest
from source_to_mutate import recite, verse, _action, _next_bottle, _bottles, _next_verse

def test_recite_single_verse():
    expected = ['2 bottles of beer on the wall, 2 bottles of beer.', 'Take one down and pass it around, 1 bottle of beer on the wall.']
    assert recite(2, 1) == expected

def test_recite_multiple_verses():
    expected = ['2 bottles of beer on the wall, 2 bottles of beer.', 'Take one down and pass it around, 1 bottle of beer on the wall.', '', '1 bottle of beer on the wall, 1 bottle of beer.', 'Take it down and pass it around, no more bottles of beer on the wall.']
    assert recite(2, 2) == expected

def test_recite_zero_verses():
    assert recite(2, 0) == []

def test_recite_from_zero():
    expected = ['No more bottles of beer on the wall, no more bottles of beer.', 'Go to the store and buy some more, 99 bottles of beer on the wall.']
    assert recite(0, 1) == expected

def test_recite_from_one():
    expected = ['1 bottle of beer on the wall, 1 bottle of beer.', 'Take it down and pass it around, no more bottles of beer on the wall.']
    assert recite(1, 1) == expected

def test_verse_2():
    expected = ['2 bottles of beer on the wall, 2 bottles of beer.', 'Take one down and pass it around, 1 bottle of beer on the wall.']
    assert verse(2) == expected

def test_verse_1():
    expected = ['1 bottle of beer on the wall, 1 bottle of beer.', 'Take it down and pass it around, no more bottles of beer on the wall.']
    assert verse(1) == expected

def test_verse_0():
    expected = ['No more bottles of beer on the wall, no more bottles of beer.', 'Go to the store and buy some more, 99 bottles of beer on the wall.']
    assert verse(0) == expected

def test_action_2():
    assert _action(2) == 'Take one down and pass it around, '

def test_action_1():
    assert _action(1) == 'Take it down and pass it around, '

def test_action_0():
    assert _action(0) == 'Go to the store and buy some more, '

def test_next_bottle_2():
    assert _next_bottle(2) == '1 bottle of beer on the wall.'

def test_next_bottle_1():
    assert _next_bottle(1) == 'no more bottles of beer on the wall.'

def test_next_bottle_0():
    assert _next_bottle(0) == '99 bottles of beer on the wall.'

def test_bottles_2():
    assert _bottles(2) == '2 bottles'

def test_bottles_1():
    assert _bottles(1) == '1 bottle'

def test_bottles_0():
    assert _bottles(0) == 'no more bottles'

def test_next_verse_2():
    assert _next_verse(2) == 1

def test_next_verse_1():
    assert _next_verse(1) == 0

def test_next_verse_0():
    assert _next_verse(0) == 99

def test_recite_start_negative():
    expected = ['-1 bottles of beer on the wall, -1 bottles of beer.', 'Take it down and pass it around, 99 bottles of beer on the wall.']
    assert recite(-1, 1) == expected

def test_recite_take_negative():
    assert recite(2, -1) == []

def test_verse_negative():
    expected = ['-1 bottles of beer on the wall, -1 bottles of beer.', 'Take it down and pass it around, 99 bottles of beer on the wall.']
    assert verse(-1) == expected

def test_bottles_negative():
    assert _bottles(-1) == '-1 bottles'

def test_next_verse_negative():
    assert _next_verse(-1) == 99

def test_next_bottle_negative():
    assert _next_bottle(-1) == '99 bottles of beer on the wall.'

def test_action_negative():
    assert _action(-1) == 'Take it down and pass it around, '