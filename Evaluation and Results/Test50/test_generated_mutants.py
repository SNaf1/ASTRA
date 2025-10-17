import pytest
from source_to_mutate import encode_shift, decode_shift

def test_encode_shift_empty_string():
    assert encode_shift("") == ""

def test_encode_shift_single_char():
    assert encode_shift("a") == "f"

def test_encode_shift_multiple_chars():
    assert encode_shift("abc") == "fgh"

def test_encode_shift_wraparound():
    assert encode_shift("xyz") == "cde"

def test_encode_shift_mixed_case():
    assert encode_shift("abcxyz") == "fghcde"

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_single_char():
    assert decode_shift("f") == "a"

def test_decode_shift_multiple_chars():
    assert decode_shift("fgh") == "abc"

def test_decode_shift_wraparound():
    assert decode_shift("cde") == "xyz"

def test_decode_shift_mixed_case():
    assert decode_shift("fghcde") == "abcxyz"

def test_encode_decode_roundtrip():
    original = "hello"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original

def test_encode_decode_roundtrip_empty():
    original = ""
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original

def test_encode_decode_roundtrip_wraparound():
    original = "xyzabc"
    encoded = encode_shift(original)
    decoded = decode_shift(encoded)
    assert decoded == original