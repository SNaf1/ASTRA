import pytest
from source_to_mutate import find_max

def test_find_max_empty_list():
    with pytest.raises(IndexError):
        find_max([])

def test_find_max_single_word():
    assert find_max(['hello']) == 'hello'

def test_find_max_multiple_words_different_lengths():
    assert find_max(['name', 'of', 'string']) == 'string'

def test_find_max_multiple_words_same_unique_count():
    assert find_max(['name', 'enam', 'game']) == 'enam'

def test_find_max_all_same_characters():
    assert find_max(['aaaaaaa', 'bb', 'cc']) == 'aaaaaaa'

def test_find_max_mixed_cases():
    assert find_max(['Name', 'name']) == 'Name'

def test_find_max_with_numbers():
    assert find_max(['123', 'abc']) == '123'

def test_find_max_with_special_characters():
    assert find_max(['!@#', 'abc']) == '!@#'

def test_find_max_empty_string():
    assert find_max(['', 'abc']) == 'abc'

def test_find_max_multiple_empty_strings():
    assert find_max(['', '', '']) == ''

def test_find_max_empty_string_and_other_strings():
    assert find_max(['abc', '']) == 'abc'

def test_find_max_same_unique_count_lexicographical_order():
    assert find_max(['abc', 'abd']) == 'abc'

def test_find_max_longer_word_with_fewer_unique():
    assert find_max(['abcdefg', 'abc']) == 'abcdefg'

def test_find_max_words_with_spaces():
    assert find_max(['hello world', 'hello']) == 'hello world'

def test_find_max_words_with_duplicate_characters():
    assert find_max(['aabbcc', 'abc']) == 'aabbcc'

def test_find_max_all_words_same_length_same_unique():
    assert find_max(['abc', 'cba', 'bac']) == 'abc'

def test_find_max_all_words_same_length_different_unique():
    assert find_max(['abc', 'abca', 'ab']) == 'abc'

def test_find_max_unicode_characters():
    assert find_max(['你好世界', 'hello']) == 'hello'

def test_find_max_mixed_unicode_and_ascii():
    assert find_max(['你好', 'abc']) == 'abc'

def test_find_max_long_list_of_words():
    words = ['apple', 'banana', 'kiwi', 'orange', 'grape', 'mango', 'strawberry']
    assert find_max(words) == 'strawberry'

def test_find_max_words_with_leading_and_trailing_spaces():
    assert find_max(['  abc', 'abc  ']) == '  abc'

def test_find_max_words_with_internal_spaces():
    assert find_max(['a b c', 'abc']) == 'a b c'

def test_find_max_words_with_mixed_case_and_spaces():
    assert find_max(['A b C', 'abc']) == 'A b C'