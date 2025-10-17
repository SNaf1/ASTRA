import pytest
from source_to_mutate import maximum_value

def test_empty_items():
    assert maximum_value(10, []) == 0

def test_single_item_within_weight():
    items = [{'weight': 5, 'value': 10}]
    assert maximum_value(10, items) == 10

def test_single_item_exceeding_weight():
    items = [{'weight': 15, 'value': 10}]
    assert maximum_value(10, items) == 0

def test_multiple_items_within_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 3, 'value': 7}, {'weight': 2, 'value': 3}]
    assert maximum_value(10, items) == 20

def test_multiple_items_some_exceeding_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 13, 'value': 7}, {'weight': 2, 'value': 3}]
    assert maximum_value(10, items) == 13

def test_multiple_items_all_exceeding_weight():
    items = [{'weight': 15, 'value': 10}, {'weight': 13, 'value': 7}, {'weight': 12, 'value': 3}]
    assert maximum_value(10, items) == 0

def test_maximum_weight_zero():
    items = [{'weight': 5, 'value': 10}, {'weight': 3, 'value': 7}, {'weight': 2, 'value': 3}]
    assert maximum_value(0, items) == 0

def test_items_with_same_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 5, 'value': 7}]
    assert maximum_value(10, items) == 17

def test_items_with_same_value():
    items = [{'weight': 5, 'value': 10}, {'weight': 3, 'value': 10}]
    assert maximum_value(10, items) == 20

def test_large_maximum_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 3, 'value': 7}, {'weight': 2, 'value': 3}]
    assert maximum_value(100, items) == 20

def test_large_number_of_items():
    items = [{'weight': i + 1, 'value': i * 2} for i in range(10)]
    assert maximum_value(15, items) == 26

def test_item_with_zero_weight():
    items = [{'weight': 0, 'value': 5}]
    assert maximum_value(5, items) == 5

def test_item_with_zero_value():
    items = [{'weight': 5, 'value': 0}]
    assert maximum_value(10, items) == 0

def test_multiple_items_exact_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 5, 'value': 7}]
    assert maximum_value(5, items) == 10

def test_multiple_items_one_exact_weight():
    items = [{'weight': 5, 'value': 10}, {'weight': 3, 'value': 7}]
    assert maximum_value(5, items) == 10

def test_duplicate_items():
    items = [{'weight': 5, 'value': 10}, {'weight': 5, 'value': 10}]
    assert maximum_value(10, items) == 20

def test_complex_scenario():
    items = [{'weight': 1, 'value': 1}, {'weight': 3, 'value': 4}, {'weight': 4, 'value': 5}, {'weight': 5, 'value': 7}]
    assert maximum_value(7, items) == 9

def test_maximum_weight_equals_item_weight():
    items = [{'weight': 7, 'value': 10}]
    assert maximum_value(7, items) == 10