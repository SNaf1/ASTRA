import pytest
from source_to_mutate import find_fewest_coins

def test_positive_target():
    coins = [1, 5, 10, 25]
    target = 37
    expected = [1, 1, 10, 25]
    assert find_fewest_coins(coins, target) == expected

def test_target_zero():
    coins = [1, 5, 10, 25]
    target = 0
    expected = []
    assert find_fewest_coins(coins, target) == expected

def test_negative_target():
    coins = [1, 5, 10, 25]
    target = -1
    with pytest.raises(ValueError) as excinfo:
        find_fewest_coins(coins, target)
    assert "target can't be negative" in str(excinfo.value)

def test_no_solution():
    coins = [2, 4]
    target = 5
    with pytest.raises(ValueError) as excinfo:
        find_fewest_coins(coins, target)
    assert "can't make target with given coins" in str(excinfo.value)

def test_single_coin():
    coins = [1]
    target = 5
    expected = [1, 1, 1, 1, 1]
    assert find_fewest_coins(coins, target) == expected

def test_single_coin_exact():
    coins = [5]
    target = 5
    expected = [5]
    assert find_fewest_coins(coins, target) == [5]

def test_single_coin_no_solution():
    coins = [2]
    target = 5
    with pytest.raises(ValueError) as excinfo:
        find_fewest_coins(coins, target)
    assert "can't make target with given coins" in str(excinfo.value)

def test_large_target():
    coins = [1, 5, 10, 25, 100]
    target = 378
    expected = [1, 1, 1, 25, 25, 25, 100, 100, 100]
    assert find_fewest_coins(coins, target) == expected

def test_coins_unordered():
    coins = [25, 10, 5, 1]
    target = 37
    expected = [25, 10, 1, 1]
    assert find_fewest_coins(coins, target) == expected

def test_coins_with_duplicates():
    coins = [1, 1, 5, 10, 25]
    target = 37
    expected = [1, 1, 10, 25]
    assert find_fewest_coins(coins, target) == expected

def test_coins_with_zero():
    coins = [0, 1, 5, 10, 25]
    target = 37
    expected = [1, 1, 10, 25]
    assert find_fewest_coins(coins, target) == expected

def test_target_equals_coin():
    coins = [1, 5, 10, 25]
    target = 10
    expected = [10]
    assert find_fewest_coins(coins, target) == [10]

def test_target_slightly_larger_than_largest_coin():
    coins = [1, 5, 10]
    target = 11
    expected = [1, 10]
    assert find_fewest_coins(coins, target) == expected

def test_target_with_only_large_coins():
    coins = [25, 50, 100]
    target = 75
    expected = [25, 50]
    assert find_fewest_coins(coins, target) == expected

def test_target_with_all_coins_larger_than_target():
    coins = [5, 10, 25]
    target = 1
    with pytest.raises(ValueError) as excinfo:
        find_fewest_coins(coins, target)
    assert "can't make target with given coins" in str(excinfo.value)

def test_coins_with_same_value():
    coins = [1, 1, 1]
    target = 3
    expected = [1, 1, 1]
    assert find_fewest_coins(coins, target) == expected