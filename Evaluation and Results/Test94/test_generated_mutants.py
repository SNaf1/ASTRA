import pytest
from source_to_mutate import skjkasdkd

def test_empty_list():
    lst = []
    assert skjkasdkd(lst) == 0

def test_no_prime_numbers():
    lst = [4, 6, 8, 9, 10]
    assert skjkasdkd(lst) == 0

def test_single_prime_number():
    lst = [2]
    assert skjkasdkd(lst) == 2

def test_multiple_prime_numbers():
    lst = [2, 3, 5, 7]
    assert skjkasdkd(lst) == 7

def test_prime_and_non_prime_numbers():
    lst = [2, 4, 5, 6, 7, 8]
    assert skjkasdkd(lst) == 7

def test_largest_prime_at_the_end():
    lst = [4, 6, 8, 9, 2, 3, 5, 7]
    assert skjkasdkd(lst) == 7

def test_largest_prime_at_the_beginning():
    lst = [7, 4, 6, 8, 9, 2, 3, 5]
    assert skjkasdkd(lst) == 7

def test_duplicate_prime_numbers():
    lst = [2, 3, 5, 7, 2, 3, 5, 7]
    assert skjkasdkd(lst) == 7

def test_large_prime_number():
    lst = [101, 103, 107, 109]
    assert skjkasdkd(lst) == 10

def test_zero_in_list():
    lst = [0, 2, 3, 5, 7]
    assert skjkasdkd(lst) == 7

def test_one_in_list():
    lst = [1, 2, 3, 5, 7]
    assert skjkasdkd(lst) == 7

def test_example_1():
    lst = [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]
    assert skjkasdkd(lst) == 10

def test_example_2():
    lst = [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]
    assert skjkasdkd(lst) == 25

def test_example_3():
    lst = [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]
    assert skjkasdkd(lst) == 13

def test_example_4():
    lst = [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]
    assert skjkasdkd(lst) == 11

def test_example_5():
    lst = [0, 81, 12, 3, 1, 21]
    assert skjkasdkd(lst) == 3

def test_example_6():
    lst = [0, 8, 1, 2, 1, 7]
    assert skjkasdkd(lst) == 7

def test_large_numbers_non_prime():
    lst = [1000, 1001, 1002]
    assert skjkasdkd(lst) == 0

def test_negative_numbers():
    lst = [-2, -3, -5, -7]
    assert skjkasdkd(lst) == 0

def test_mixed_positive_and_negative():
    lst = [-2, 2, -3, 3, -5, 5, -7, 7]
    assert skjkasdkd(lst) == 7

def test_large_prime_at_start():
    lst = [997, 2, 3, 5, 7]
    assert skjkasdkd(lst) == 25

def test_large_prime_in_middle():
    lst = [2, 3, 997, 5, 7]
    assert skjkasdkd(lst) == 25

def test_all_same_prime():
    lst = [7, 7, 7, 7, 7]
    assert skjkasdkd(lst) == 7

def test_all_same_non_prime():
    lst = [4, 4, 4, 4, 4]
    assert skjkasdkd(lst) == 0

def test_one_prime_among_many_non_primes():
    lst = [4, 6, 8, 9, 10, 20, 30, 7]
    assert skjkasdkd(lst) == 7