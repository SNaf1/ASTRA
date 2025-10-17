import pytest
from source_to_mutate import bf

def test_bf_jupiter_neptune():
    assert bf('Jupiter', 'Neptune') == ('Saturn', 'Uranus')

def test_bf_earth_mercury():
    assert bf('Earth', 'Mercury') == ('Venus',)

def test_bf_mercury_uranus():
    assert bf('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')

def test_bf_same_planets():
    assert bf('Earth', 'Earth') == ()

def test_bf_invalid_planet1():
    assert bf('Invalid', 'Earth') == ()

def test_bf_invalid_planet2():
    assert bf('Earth', 'Invalid') == ()

def test_bf_both_invalid():
    assert bf('Invalid1', 'Invalid2') == ()

def test_bf_neptune_jupiter():
    assert bf('Neptune', 'Jupiter') == ('Saturn', 'Uranus')

def test_bf_mercury_venus():
    assert bf('Mercury', 'Venus') == ()

def test_bf_venus_mercury():
    assert bf('Venus', 'Mercury') == ()

def test_bf_uranus_neptune():
    assert bf('Uranus', 'Neptune') == ()

def test_bf_neptune_uranus():
    assert bf('Neptune', 'Uranus') == ()

def test_bf_mercury_neptune():
    assert bf('Mercury', 'Neptune') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')

def test_bf_neptune_mercury():
    assert bf('Neptune', 'Mercury') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')

def test_bf_earth_mars():
    assert bf('Earth', 'Mars') == ()

def test_bf_mars_earth():
    assert bf('Mars', 'Earth') == ()

def test_bf_earth_jupiter():
    assert bf('Earth', 'Jupiter') == ('Mars',)

def test_bf_jupiter_earth():
    assert bf('Jupiter', 'Earth') == ('Mars',)