import pytest
from source_to_mutate import BLOCK_SIZE, trtbl, base_trans, encode, decode

@pytest.fixture(autouse=True)
def reset_state():
    pass

def test_base_trans_empty():
    assert base_trans('') == ''

def test_base_trans_only_special_chars():
    assert base_trans('!@#$%^') == ''

def test_base_trans_mixed_alpha_numeric_special():
    assert base_trans('HeLlO123!@#WoRlD') == 'svool123dliow'

def test_base_trans_all_lowercase():
    assert base_trans('abcdefghijklmnopqrstuvwxyz') == 'zyxwvutsrqponmlkjihgfedcba'

def test_base_trans_all_uppercase():
    assert base_trans('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'zyxwvutsrqponmlkjihgfedcba'

def test_base_trans_with_spaces():
    assert base_trans('Hello World') == 'svooldliow'

def test_base_trans_numbers_only():
    assert base_trans('1234567890') == '1234567890'

def test_encode_empty():
    assert encode('') == ''

def test_encode_only_special_chars():
    assert encode('!@#$%^') == ''

def test_encode_mixed_alpha_numeric_special():
    assert encode('HeLlO123!@#WoRlD') == 'svool 123dl iow'

def test_encode_all_lowercase():
    assert encode('abcdefghijklmnopqrstuvwxyz') == 'zyxwv utsrq ponml kjihg fedcb a'

def test_encode_all_uppercase():
    assert encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'zyxwv utsrq ponml kjihg fedcb a'

def test_encode_with_spaces():
    assert encode('Hello World') == 'svool dliow'

def test_encode_numbers_only():
    assert encode('1234567890') == '12345 67890'

def test_encode_long_string():
    assert encode('aaaaaaaaaaaaaaaaaaaaaaaa') == 'zzzzz zzzzz zzzzz zzzzz zzzz'

def test_encode_string_with_block_size_multiple():
    assert encode('aaaaabbbbb') == 'zzzzz yyyyy'

def test_encode_string_with_block_size_not_multiple():
    assert encode('aaaaabbbbbc') == 'zzzzz yyyyy x'

def test_decode_empty():
    assert decode('') == ''

def test_decode_only_special_chars():
    assert decode('!@#$%^') == ''

def test_decode_mixed_alpha_numeric_special():
    assert decode('SvOol123!@#DlIoW') == 'hello123world'

def test_decode_all_lowercase():
    assert decode('zyxwvutsrqponmlkjihgfedcba') == 'abcdefghijklmnopqrstuvwxyz'

def test_decode_all_uppercase():
    assert decode('ZYXWVUTSRQPONMLKJIHGFEDCBA') == 'abcdefghijklmnopqrstuvwxyz'

def test_decode_with_spaces():
    assert decode('SvOol World') == 'hellodliow'

def test_decode_numbers_only():
    assert decode('1234567890') == '1234567890'

def test_decode_long_string():
    assert decode('zzzzzzzzzzzzzzzzzzzzzzzzz') == 'aaaaaaaaaaaaaaaaaaaaaaaaa'

def test_decode_string_with_block_size_multiple():
    assert decode('zzzzz zzzzz') == 'aaaaaaaaaa'

def test_decode_string_with_block_size_not_multiple():
    assert decode('zzzzz zzzzz c') == 'aaaaaaaaaax'

def test_decode_with_mixed_case_and_spaces():
    assert decode('zyXwv UtSrq PonMl') == 'abcdefghijklmno'

def test_encode_decode_roundtrip():
    plain_text = 'Testing123'
    encoded_text = encode(plain_text)
    decoded_text = decode(encoded_text)
    assert decoded_text == 'testing123'

def test_encode_with_leading_and_trailing_spaces():
    assert encode('  abc  ') == 'zyx'

def test_decode_with_leading_and_trailing_spaces():
    assert decode('  zyx  ') == 'abc'