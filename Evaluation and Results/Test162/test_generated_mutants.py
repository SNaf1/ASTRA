import pytest
from source_to_mutate import string_to_md5

def test_string_to_md5_empty_string():
    assert string_to_md5('') is None

def test_string_to_md5_hello_world():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_simple_string():
    assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'

def test_string_to_md5_string_with_numbers():
    assert string_to_md5('test123') == 'cc03e747a6afbbcbf8be7668acfebee5'

def test_string_to_md5_string_with_spaces():
    assert string_to_md5('test test') == '4f4acc5d8c71f5fbf04dace00b5360c8'

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5('test!') == 'c4d354440cb41ee38e162bc1f431e99b'

def test_string_to_md5_long_string():
    long_string = 'This is a very long string to test the md5 function.'
    assert string_to_md5(long_string) == 'a26bc553ed62e0de4b7cf5abcbea91a6'

def test_string_to_md5_unicode_string():
    with pytest.raises(UnicodeEncodeError) as excinfo:
        string_to_md5('你好世界')
    assert 'ascii' in str(excinfo.value)