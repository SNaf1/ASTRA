import pytest
from source_to_mutate import largest, smallest, get_extreme_palindrome_with_factors, reverse_num, num_digits, palindromes

def test_largest_palindrome_from_single_number():
    assert largest(1, 1) == (1, [(1, 1)])

def test_largest_palindrome_from_smaller_numbers():
    assert largest(1, 3) == (9, [(3, 3)])

def test_largest_palindrome_from_larger_numbers():
    assert largest(1, 4) == (9, [(3, 3)])

def test_largest_palindrome_from_increasing_range():
    assert largest(1, 9) == (9, [(1, 9), (3, 3), (9, 1)])

def test_largest_palindrome_from_decreasing_range():
    assert largest(1, 7) == (9, [(3, 3)])

def test_largest_palindrome_from_a_bigger_range():
    assert largest(10, 99) == (9009, [(91, 99), (99, 91)])

def test_largest_palindrome_from_a_three_digit_range():
    assert largest(100, 999) == (906609, [(913, 993), (993, 913)])

def test_smallest_palindrome_from_single_number():
    assert smallest(1, 1) == (1, [(1, 1)])

def test_smallest_palindrome_from_smaller_numbers():
    with pytest.raises(ValueError) as excinfo:
        smallest(1, 3)
    assert str(excinfo.value) == 'min must be <= max'

def test_smallest_palindrome_from_larger_numbers():
    with pytest.raises(ValueError) as excinfo:
        smallest(1, 4)
    assert str(excinfo.value) == 'min must be <= max'

def test_smallest_palindrome_from_increasing_range():
    with pytest.raises(ValueError) as excinfo:
        smallest(1, 9)
    assert str(excinfo.value) == 'min must be <= max'

def test_smallest_palindrome_from_decreasing_range():
    with pytest.raises(ValueError) as excinfo:
        smallest(1, 7)
    assert str(excinfo.value) == 'min must be <= max'

def test_smallest_palindrome_from_a_bigger_range():
    with pytest.raises(ValueError) as excinfo:
        smallest(10, 99)
    assert str(excinfo.value) == 'min must be <= max'

def test_smallest_palindrome_from_a_three_digit_range():
    with pytest.raises(ValueError) as excinfo:
        smallest(100, 999)
    assert str(excinfo.value) == 'min must be <= max'

def test_get_extreme_palindrome_with_factors_largest():
    assert get_extreme_palindrome_with_factors(99, 10, 'largest') == (9009, [(91, 99), (99, 91)])

def test_get_extreme_palindrome_with_factors_smallest():
    assert get_extreme_palindrome_with_factors(99, 10, 'smallest') == (121, [(11, 11)])

def test_get_extreme_palindrome_with_factors_no_palindromes():
    assert get_extreme_palindrome_with_factors(10, 1, 'largest') == (9, [(1, 9), (3, 3), (9, 1)])

def test_reverse_num_single_digit():
    assert reverse_num(5) == 5

def test_reverse_num_multiple_digits():
    assert reverse_num(123) == 321

def test_reverse_num_with_trailing_zeros():
    assert reverse_num(120) == 21

def test_num_digits_single_digit():
    assert num_digits(5) == 1

def test_num_digits_multiple_digits():
    assert num_digits(123) == 3

def test_num_digits_zero():
    assert num_digits(1) == 1

def test_palindromes_single_number():
    assert list(palindromes(1, 1)) == [1]

def test_palindromes_smaller_numbers():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 3))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_larger_numbers():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 4))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_increasing_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 9))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_decreasing_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 7))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_a_bigger_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(10, 11))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_a_three_digit_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(100, 101))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_single_number():
    assert list(palindromes(1, 1, reverse=True)) == [1]

def test_palindromes_reverse_smaller_numbers():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 3, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_larger_numbers():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 4, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_increasing_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 9, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_decreasing_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(1, 7, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_a_bigger_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(10, 11, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_reverse_a_three_digit_range():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(100, 101, reverse=True))
    assert str(excinfo.value) == 'min must be <= max'

def test_palindromes_min_greater_than_max():
    with pytest.raises(ValueError) as excinfo:
        list(palindromes(min_factor=2, max_factor=1))
    assert str(excinfo.value) == 'min must be <= max'