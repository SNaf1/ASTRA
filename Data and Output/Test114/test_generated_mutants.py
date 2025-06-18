import pytest
from source_to_mutate import minSubArraySum

def test_empty_array():
    nums = []
    with pytest.raises(ValueError):
        minSubArraySum(nums)

def test_single_positive_number():
    nums = [5]
    assert minSubArraySum(nums) == 5

def test_single_negative_number():
    nums = [-5]
    assert minSubArraySum(nums) == -5

def test_positive_numbers():
    nums = [2, 3, 4, 1, 2, 4]
    assert minSubArraySum(nums) == 1

def test_negative_numbers():
    nums = [-1, -2, -3]
    assert minSubArraySum(nums) == -6

def test_mixed_numbers():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert minSubArraySum(nums) == -5

def test_all_zeros():
    nums = [0, 0, 0]
    assert minSubArraySum(nums) == 0

def test_large_numbers():
    nums = [1000, 2000, 3000]
    assert minSubArraySum(nums) == 1000

def test_large_negative_numbers():
    nums = [-1000, -2000, -3000]
    assert minSubArraySum(nums) == -6000

def test_alternating_positive_negative():
    nums = [1, -2, 3, -4, 5]
    assert minSubArraySum(nums) == -4

def test_repeating_numbers():
    nums = [1, 1, 1, 1, 1]
    assert minSubArraySum(nums) == 1

def test_repeating_negative_numbers():
    nums = [-1, -1, -1, -1, -1]
    assert minSubArraySum(nums) == -5

def test_zero_in_array():
    nums = [1, 2, 0, 4, 5]
    assert minSubArraySum(nums) == 0

def test_zero_at_start():
    nums = [0, 1, 2, 3]
    assert minSubArraySum(nums) == 0

def test_zero_at_end():
    nums = [1, 2, 3, 0]
    assert minSubArraySum(nums) == 0

def test_negative_at_start():
    nums = [-5, 1, 2, 3]
    assert minSubArraySum(nums) == -5

def test_negative_at_end():
    nums = [1, 2, 3, -5]
    assert minSubArraySum(nums) == -5

def test_multiple_negative_numbers_at_start():
    nums = [-5, -4, -3, 1, 2]
    assert minSubArraySum(nums) == -12

def test_multiple_negative_numbers_at_end():
    nums = [1, 2, -3, -4, -5]
    assert minSubArraySum(nums) == -12