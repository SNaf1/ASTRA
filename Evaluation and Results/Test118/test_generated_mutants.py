import pytest
from source_to_mutate import get_closest_vowel

def test_empty_string():
    assert get_closest_vowel('') == ''

def test_short_string():
    assert get_closest_vowel('ab') == ''

def test_yogurt():
    assert get_closest_vowel('yogurt') == 'u'

def test_FULL():
    assert get_closest_vowel('FULL') == 'U'

def test_quick():
    assert get_closest_vowel('quick') == ''

def test_vowel_at_beginning():
    assert get_closest_vowel('apple') == ''

def test_vowel_at_end():
    assert get_closest_vowel('table') == 'a'

def test_no_consonants():
    assert get_closest_vowel('aeiou') == ''

def test_only_consonants():
    assert get_closest_vowel('bcdfgh') == ''

def test_mixed_case():
    assert get_closest_vowel('YoGuRt') == 'u'

def test_multiple_vowels():
    assert get_closest_vowel('baeiouzy') == ''

def test_vowel_between_vowels():
    assert get_closest_vowel('aouiea') == ''

def test_consonant_vowel_consonant():
    assert get_closest_vowel('bac') == 'a'

def test_consonant_vowel_vowel():
    assert get_closest_vowel('baa') == ''

def test_vowel_vowel_consonant():
    assert get_closest_vowel('aab') == ''

def test_long_word():
    assert get_closest_vowel('strength') == 'e'

def test_long_word_with_vowel():
    assert get_closest_vowel('strengths') == 'e'

def test_long_word_with_vowel_between_consonants():
    assert get_closest_vowel('bstrengthc') == 'e'

def test_long_word_with_multiple_vowels_between_consonants():
    assert get_closest_vowel('bzstrengthenc') == 'e'

def test_word_with_numbers():
    assert get_closest_vowel('b2strengthenc') == 'e'

def test_word_with_symbols():
    assert get_closest_vowel('b$strengthenc') == 'e'

def test_word_with_spaces():
    assert get_closest_vowel('b strength c') == 'e'

def test_word_with_repeating_vowels():
    assert get_closest_vowel('brreeec') == ''

def test_word_with_repeating_consonants():
    assert get_closest_vowel('brrrrec') == 'e'

def test_word_with_vowel_at_second_position():
    assert get_closest_vowel('cba') == ''

def test_word_with_vowel_at_second_position_uppercase():
    assert get_closest_vowel('cbA') == ''

def test_word_with_vowel_at_second_position_and_longer_word():
    assert get_closest_vowel('cbazzz') == 'a'

def test_word_with_vowel_at_second_position_and_longer_word_uppercase():
    assert get_closest_vowel('cbAzzz') == 'A'