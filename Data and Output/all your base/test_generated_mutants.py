import pytest
from source_to_mutate import from_digits, to_digits, rebase

def test_from_digits_base_10():
    assert from_digits([4, 2], 10) == 42

def test_from_digits_base_2():
    assert from_digits([1, 0, 1, 0, 1, 0], 2) == 42

def test_from_digits_base_16():
    assert from_digits([2, 10], 16) == 42

def test_from_digits_empty_digits():
    assert from_digits([], 10) == 0

def test_from_digits_single_digit():
    assert from_digits([7], 10) == 7

def test_to_digits_base_10():
    assert to_digits(42, 10) == [4, 2]

def test_to_digits_base_2():
    assert to_digits(42, 2) == [1, 0, 1, 0, 1, 0]

def test_to_digits_base_16():
    assert to_digits(42, 16) == [2, 10]

def test_to_digits_zero():
    assert to_digits(0, 10) == [0]

def test_to_digits_one():
    assert to_digits(1, 10) == [1]

def test_rebase_base_2_to_base_10():
    assert rebase(2, [1, 0, 1, 0, 1, 0], 10) == [4, 2]

def test_rebase_base_10_to_base_2():
    assert rebase(10, [4, 2], 2) == [1, 0, 1, 0, 1, 0]

def test_rebase_base_16_to_base_8():
    assert rebase(16, [2, 10], 8) == [5, 2]

def test_rebase_base_2_to_base_16():
    assert rebase(2, [1, 1, 1, 1, 1, 1], 16) == [3, 15]

def test_rebase_base_97_to_base_73():
    assert rebase(97, [3, 46, 6], 73) == [6, 9, 64]

def test_rebase_base_10_to_base_10():
    assert rebase(10, [0], 10) == [0]

def test_rebase_base_10_to_base_10_again():
    assert rebase(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def test_rebase_base_2_to_base_62():
    assert rebase(2, [1, 0, 1, 0, 1, 0], 62) == [42]

def test_rebase_empty_digits():
    assert rebase(2, [], 10) == [0]

def test_rebase_single_zero():
    assert rebase(10, [0], 2) == [0]

def test_rebase_invalid_input_base():
    with pytest.raises(ValueError) as excinfo:
        rebase(1, [0], 10)
    assert str(excinfo.value) == 'input base must be >= 2'

def test_rebase_invalid_output_base():
    with pytest.raises(ValueError) as excinfo:
        rebase(2, [0], 1)
    assert str(excinfo.value) == 'output base must be >= 2'

def test_rebase_invalid_digit():
    with pytest.raises(ValueError) as excinfo:
        rebase(10, [1, 2, -3, 4, 5, 6, 7, 8, 9, 0], 10)
    assert str(excinfo.value) == 'all digits must satisfy 0 <= d < input base'

def test_rebase_invalid_digit_2():
    with pytest.raises(ValueError) as excinfo:
        rebase(2, [1, 2, 1, 0, 1, 0], 10)
    assert str(excinfo.value) == 'all digits must satisfy 0 <= d < input base'