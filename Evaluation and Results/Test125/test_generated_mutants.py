import pytest
from source_to_mutate import split_words

def test_split_words_whitespace():
    assert split_words('Hello world!') == ['Hello', 'world!']

def test_split_words_comma():
    assert split_words('Hello,world!') == ['Hello', 'world!']

def test_split_words_no_split_odd_count():
    assert split_words('abcdef') == 3

def test_split_words_empty_string():
    assert split_words('') == 0

def test_split_words_single_word():
    assert split_words('word') == 2

def test_split_words_single_word_with_comma():
    assert split_words('word,') == ['word']

def test_split_words_single_word_with_space():
    assert split_words('word ') == ['word']

def test_split_words_mixed_case():
    assert split_words('aBcDeF') == 0

def test_split_words_numbers():
    assert split_words('123456') == 0

def test_split_words_special_characters():
    assert split_words('!@#$%^') == 0

def test_split_words_mixed_characters():
    assert split_words('a1b2c3d4e5f6') == 3

def test_split_words_multiple_spaces():
    assert split_words('Hello   world!') == ['Hello', 'world!']

def test_split_words_multiple_commas():
    assert split_words('Hello,world,,again!') == ['Hello', 'world', 'again!']

def test_split_words_comma_and_space():
    assert split_words('Hello, world!') == ['Hello,', 'world!']

def test_split_words_only_commas():
    assert split_words(',,,,') == []

def test_split_words_only_spaces():
    assert split_words('   ') == []

def test_split_words_uppercase():
    assert split_words('ABCDEF') == 0

def test_split_words_mixed_case_and_numbers():
    assert split_words('a1B2c3D4e5F6') == 0

def test_split_words_long_string():
    assert split_words('abcdefghijklmnopqrstuvwxyz') == 13

def test_split_words_long_string_with_spaces():
    assert split_words('a b c d e f g h i j k l m n o p q r s t u v w x y z') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_split_words_long_string_with_commas():
    assert split_words('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def test_split_words_unicode():
    assert split_words('你好世界') == 0

def test_split_words_unicode_with_space():
    assert split_words('你好 世界') == ['你好', '世界']

def test_split_words_unicode_with_comma():
    assert split_words('你好,世界') == ['你好', '世界']