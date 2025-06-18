import pytest
from source_to_mutate import mod_inverse, translate, encode, decode, BLOCK_SIZE, ALPHABET

def test_mod_inverse_coprime():
    assert mod_inverse(3, 26) == 9

def test_mod_inverse_not_coprime():
    assert mod_inverse(13, 26) == 1

def test_mod_inverse_zero():
    assert mod_inverse(0, 26) == 1

def test_mod_inverse_one():
    assert mod_inverse(1, 26) == 1

def test_mod_inverse_large_number():
    assert mod_inverse(29, 26) == 9

def test_translate_encode():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_decode():
    with pytest.raises(ValueError) as excinfo:
        translate('def', 1, 3, 1)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_empty_string():
    with pytest.raises(ValueError) as excinfo:
        translate('', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_special_characters():
    with pytest.raises(ValueError) as excinfo:
        translate('a!b@c#', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_numbers():
    with pytest.raises(ValueError) as excinfo:
        translate('1a2b3c', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_uppercase():
    with pytest.raises(ValueError) as excinfo:
        translate('AbC', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_mixed_case():
    with pytest.raises(ValueError) as excinfo:
        translate('aBc', 1, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_non_coprime_raises_error():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 13, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_non_coprime_decode_raises_error():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 13, 3, 1)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_empty_string():
    with pytest.raises(ValueError) as excinfo:
        encode('', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_short_string():
    with pytest.raises(ValueError) as excinfo:
        encode('abc', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_long_string():
    with pytest.raises(ValueError) as excinfo:
        encode('abcdefghijklm', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_with_special_characters():
    with pytest.raises(ValueError) as excinfo:
        encode('a!b@c#d$e%', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_with_numbers():
    with pytest.raises(ValueError) as excinfo:
        encode('1a2b3c4d5e', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_mixed_case():
    with pytest.raises(ValueError) as excinfo:
        encode('aBcDe', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_empty_string():
    with pytest.raises(ValueError) as excinfo:
        decode('', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_short_string():
    with pytest.raises(ValueError) as excinfo:
        decode('def', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_long_string():
    with pytest.raises(ValueError) as excinfo:
        decode('defgh ijkln', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_with_special_characters():
    with pytest.raises(ValueError) as excinfo:
        decode('d!e@f#g$h%', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_with_numbers():
    with pytest.raises(ValueError) as excinfo:
        decode('1d2e3f4g5h', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_mixed_case():
    with pytest.raises(ValueError) as excinfo:
        decode('dEfGh', 1, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_non_coprime_raises_error():
    with pytest.raises(ValueError) as excinfo:
        encode('abc', 13, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_decode_non_coprime_raises_error():
    with pytest.raises(ValueError) as excinfo:
        decode('abc', 13, 3)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_encode_block_size_one():
    global BLOCK_SIZE
    original_block_size = BLOCK_SIZE
    BLOCK_SIZE = 1
    try:
        with pytest.raises(ValueError) as excinfo:
            encode('abcdefghijklm', 1, 3)
        assert str(excinfo.value) == 'a and m must be coprime.'
    finally:
        BLOCK_SIZE = original_block_size

def test_decode_block_size_one():
    global BLOCK_SIZE
    original_block_size = BLOCK_SIZE
    BLOCK_SIZE = 1
    try:
        with pytest.raises(ValueError) as excinfo:
            decode('d e f g h i j k l n', 1, 3)
        assert str(excinfo.value) == 'a and m must be coprime.'
    finally:
        BLOCK_SIZE = original_block_size

def test_translate_with_negative_b():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 1, -3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_with_large_a():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 27, 3, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_with_large_b():
    with pytest.raises(ValueError) as excinfo:
        translate('abc', 1, 29, 0)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_with_negative_b_decode():
    with pytest.raises(ValueError) as excinfo:
        translate('xyz', 1, -3, 1)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_with_large_a_decode():
    with pytest.raises(ValueError) as excinfo:
        translate('def', 27, 3, 1)
    assert str(excinfo.value) == 'a and m must be coprime.'

def test_translate_with_large_b_decode():
    with pytest.raises(ValueError) as excinfo:
        translate('def', 1, 29, 1)
    assert str(excinfo.value) == 'a and m must be coprime.'