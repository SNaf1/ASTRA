import pytest
from source_to_mutate import max_fill

def test_empty_grid():
    grid = []
    capacity = 1
    assert max_fill(grid, capacity) == 0

def test_empty_wells():
    grid = [[0, 0, 0], [0, 0, 0]]
    capacity = 5
    assert max_fill(grid, capacity) == 0

def test_single_well_empty():
    grid = [[0, 0, 0]]
    capacity = 1
    assert max_fill(grid, capacity) == 0

def test_single_well_full():
    grid = [[1, 1, 1, 1]]
    capacity = 2
    assert max_fill(grid, capacity) == 2

def test_single_well_partial():
    grid = [[0, 0, 1, 0]]
    capacity = 1
    assert max_fill(grid, capacity) == 1

def test_multiple_wells_varying_water():
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    capacity = 1
    assert max_fill(grid, capacity) == 6

def test_multiple_wells_varying_water_capacity_2():
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    capacity = 2
    assert max_fill(grid, capacity) == 5

def test_multiple_wells_varying_water_capacity_3():
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    capacity = 3
    assert max_fill(grid, capacity) == 4

def test_large_grid_small_capacity():
    grid = [[1] * 100] * 100
    capacity = 1
    assert max_fill(grid, capacity) == 10000

def test_large_grid_large_capacity():
    grid = [[1] * 100] * 100
    capacity = 10
    assert max_fill(grid, capacity) == 1000

def test_mixed_wells_same_capacity():
    grid = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
    capacity = 2
    assert max_fill(grid, capacity) == 4

def test_all_wells_full_capacity_equals_well_size():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    capacity = 3
    assert max_fill(grid, capacity) == 3

def test_all_wells_full_capacity_greater_than_well_size():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    capacity = 4
    assert max_fill(grid, capacity) == 3

def test_wells_with_zeros_and_ones():
    grid = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]
    capacity = 2
    assert max_fill(grid, capacity) == 3

def test_wells_with_all_zeros_and_ones():
    grid = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 1]]
    capacity = 2
    assert max_fill(grid, capacity) == 3

def test_wells_with_single_one():
    grid = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    capacity = 1
    assert max_fill(grid, capacity) == 1

def test_wells_with_single_one_large_capacity():
    grid = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    capacity = 5
    assert max_fill(grid, capacity) == 1