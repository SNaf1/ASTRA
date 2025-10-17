import pytest
from source_to_mutate import decimal_to_binary

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"

def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"

def test_decimal_to_binary_fifteen():
    assert decimal_to_binary(15) == "db1111db"

def test_decimal_to_binary_thirty_two():
    assert decimal_to_binary(32) == "db100000db"

def test_decimal_to_binary_large_number():
    assert decimal_to_binary(255) == "db11111111db"

def test_decimal_to_binary_another_large_number():
    assert decimal_to_binary(1024) == "db10000000000db"

def test_decimal_to_binary_prime_number():
    assert decimal_to_binary(17) == "db10001db"