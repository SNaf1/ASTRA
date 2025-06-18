import pytest
from source_to_mutate import hex_key

def test_empty_string():
    assert hex_key('') == 0

def test_single_prime():
    assert hex_key('2') == 1

def test_single_non_prime():
    assert hex_key('0') == 0

def test_example_1():
    assert hex_key('AB') == 1

def test_example_2():
    assert hex_key('1077E') == 2

def test_example_3():
    assert hex_key('ABED1A33') == 4

def test_example_4():
    assert hex_key('123456789ABCDEF0') == 6

def test_example_5():
    assert hex_key('2020') == 2

def test_all_primes():
    assert hex_key('2357BD') == 6

def test_all_non_primes():
    assert hex_key('014689ACEF') == 0

def test_mixed_primes_and_non_primes():
    assert hex_key('12A3B4C5D6E7F') == 6

def test_long_string_with_primes():
    assert hex_key('2222222222222222') == 16

def test_long_string_without_primes():
    assert hex_key('0000000000000000') == 0

def test_string_with_repeated_primes():
    assert hex_key('22335577BBDD') == 12

def test_string_with_repeated_non_primes():
    assert hex_key('001144668899AAEEFFCC') == 0

def test_string_with_mixed_repeated_primes_and_non_primes():
    assert hex_key('0213456789ABCDEF') == 6

def test_string_with_only_one_prime_repeated():
    assert hex_key('22222222222222220') == 16

def test_string_with_only_one_non_prime_repeated():
    assert hex_key('00000000000000002') == 1

def test_string_with_primes_at_start_and_end():
    assert hex_key('20000000000000002') == 2

def test_string_with_primes_at_start_and_end_different_primes():
    assert hex_key('20000000000000003') == 2

def test_string_with_primes_at_start_and_end_different_primes_long():
    assert hex_key('2000000000000000D') == 2