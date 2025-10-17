import pytest
from source_to_mutate import words_in_sentence

def test_empty_sentence():
    assert words_in_sentence('') == ''

def test_single_word_prime_length():
    assert words_in_sentence('is') == 'is'

def test_single_word_non_prime_length():
    assert words_in_sentence('test') == ''

def test_multiple_words_with_prime_lengths():
    assert words_in_sentence('lets go for swimming') == 'go for'

def test_multiple_words_with_non_prime_lengths():
    assert words_in_sentence('This is a test') == 'is'

def test_mixed_prime_and_non_prime_lengths():
    assert words_in_sentence('The quick brown fox jumps over the lazy dog') == 'The quick brown fox jumps the dog'

def test_sentence_with_repeated_words():
    assert words_in_sentence('go go go') == 'go go go'

def test_sentence_with_numbers():
    assert words_in_sentence('12 123 1234') == '12 123'

def test_sentence_with_special_characters():
    assert words_in_sentence('a! b@ c#') == 'a! b@ c#'

def test_sentence_with_one_letter_words():
    assert words_in_sentence('a b c d e f g') == ''

def test_sentence_with_two_letter_words():
    assert words_in_sentence('at is an to') == 'at is an to'

def test_sentence_with_three_letter_words():
    assert words_in_sentence('the and are') == 'the and are'

def test_sentence_with_four_letter_words():
    assert words_in_sentence('that this then') == ''

def test_sentence_with_five_letter_words():
    assert words_in_sentence('about which their') == 'about which their'

def test_sentence_with_six_letter_words():
    assert words_in_sentence('always number') == ''

def test_sentence_with_seven_letter_words():
    assert words_in_sentence('because another') == 'because another'

def test_sentence_with_eight_letter_words():
    assert words_in_sentence('anything example') == 'example'

def test_sentence_with_nine_letter_words():
    assert words_in_sentence('something everyone') == ''

def test_sentence_with_ten_letter_words():
    assert words_in_sentence('everything different') == ''

def test_sentence_with_prime_and_non_prime_lengths_adjacent():
    assert words_in_sentence('is test go') == 'is go'

def test_sentence_with_only_one_prime_length_word():
    assert words_in_sentence('hello is world') == 'hello is world'

def test_sentence_with_only_one_non_prime_length_word():
    assert words_in_sentence('hello world') == 'hello world'

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence('  is a test  ') == 'is'

def test_sentence_with_multiple_spaces_between_words():
    assert words_in_sentence('is  a   test') == 'is'

def test_sentence_with_only_spaces():
    assert words_in_sentence('   ') == ''

def test_sentence_with_long_words():
    assert words_in_sentence('abcdefghijk abcdefghijklm') == 'abcdefghijk abcdefghijklm'

def test_sentence_with_words_of_length_2():
    assert words_in_sentence('it is to be') == 'it is to be'

def test_sentence_with_words_of_length_3():
    assert words_in_sentence('the and are not') == 'the and are not'