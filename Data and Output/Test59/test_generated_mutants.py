import pytest
from source_to_mutate import largest_prime_factor, METADATA

def test_largest_prime_factor_example_1():
    assert largest_prime_factor(13195) == 29

def test_largest_prime_factor_example_2():
    assert largest_prime_factor(2048) == 2

def test_largest_prime_factor_small_number():
    assert largest_prime_factor(4) == 2

def test_largest_prime_factor_another_small_number():
    assert largest_prime_factor(6) == 3

def test_largest_prime_factor_prime_squared():
    assert largest_prime_factor(9) == 3

def test_largest_prime_factor_larger_number():
    assert largest_prime_factor(35) == 7

def test_largest_prime_factor_number_with_multiple_prime_factors():
    assert largest_prime_factor(14) == 7

def test_largest_prime_factor_number_with_same_prime_factor_multiple_times():
    assert largest_prime_factor(8) == 2

def test_largest_prime_factor_number_with_large_prime_factor():
    assert largest_prime_factor(100) == 5

def test_largest_prime_factor_number_with_close_prime_factors():
    assert largest_prime_factor(21) == 7

def test_largest_prime_factor_number_with_one_large_prime_factor():
    assert largest_prime_factor(22) == 11

def test_largest_prime_factor_number_with_only_one_prime_factor():
    assert largest_prime_factor(27) == 3

def test_largest_prime_factor_number_with_prime_factor_at_end():
    assert largest_prime_factor(15) == 5

def test_largest_prime_factor_number_with_prime_factor_at_beginning():
    assert largest_prime_factor(10) == 5

def test_largest_prime_factor_number_with_prime_factor_in_middle():
    assert largest_prime_factor(26) == 13

def test_largest_prime_factor_number_with_prime_factor_repeated():
    assert largest_prime_factor(12) == 3

def test_largest_prime_factor_number_with_prime_factor_repeated_many_times():
    assert largest_prime_factor(16) == 2

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime():
    assert largest_prime_factor(18) == 3

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime_larger():
    assert largest_prime_factor(20) == 5

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime_smaller():
    assert largest_prime_factor(30) == 5

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime_smaller_and_larger():
    assert largest_prime_factor(42) == 7

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime_smaller_and_larger_and_repeated():
    assert largest_prime_factor(60) == 5

def test_largest_prime_factor_number_with_prime_factor_repeated_and_another_prime_smaller_and_larger_and_repeated_and_larger():
    assert largest_prime_factor(84) == 7