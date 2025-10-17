import pytest
from source_to_mutate import car_race_collision

def test_car_race_collision_zero():
    assert car_race_collision(0) == 0

def test_car_race_collision_one():
    assert car_race_collision(1) == 1

def test_car_race_collision_two():
    assert car_race_collision(2) == 4

def test_car_race_collision_ten():
    assert car_race_collision(10) == 100

def test_car_race_collision_large():
    assert car_race_collision(100) == 10000