import pytest
from source_to_mutate import cipher_text, _cleanse, _chunks_of

def test_cipher_text_empty():
    assert cipher_text('') == ''

def test_cipher_text_simple():
    assert cipher_text('A') == 'a'

def test_cipher_text_two_chars():
    assert cipher_text('AB') == 'a b'

def test_cipher_text_three_chars():
    assert cipher_text('ABC') == 'ac b '

def test_cipher_text_four_chars():
    assert cipher_text('ABCD') == 'ac bd'

def test_cipher_text_five_chars():
    assert cipher_text('ABCDE') == 'ad be c '

def test_cipher_text_six_chars():
    assert cipher_text('ABCDEF') == 'ad be cf'

def test_cipher_text_seven_chars():
    assert cipher_text('ABCDEFG') == 'adg be  cf '

def test_cipher_text_eight_chars():
    assert cipher_text('ABCDEFGH') == 'adg beh cf '

def test_cipher_text_nine_chars():
    assert cipher_text('ABCDEFGHI') == 'adg beh cfi'

def test_cipher_text_ten_chars():
    assert cipher_text('ABCDEFGHIJ') == 'aei bfj cg  dh '

def test_cipher_text_eleven_chars():
    assert cipher_text('ABCDEFGHIJK') == 'aei bfj cgk dh '

def test_cipher_text_twelve_chars():
    assert cipher_text('ABCDEFGHIJKL') == 'aei bfj cgk dhl'

def test_cipher_text_thirteen_chars():
    assert cipher_text('ABCDEFGHIJKLM') == 'aeim bfj  cgk  dhl '

def test_cipher_text_fourteen_chars():
    assert cipher_text('ABCDEFGHIJKLMN') == 'aeim bfjn cgk  dhl '

def test_cipher_text_fifteen_chars():
    assert cipher_text('ABCDEFGHIJKLMNO') == 'aeim bfjn cgko dhl '

def test_cipher_text_sixteen_chars():
    assert cipher_text('ABCDEFGH IJKLMN OP') == 'aeim bfjn cgko dhlp'

def test_cipher_text_with_punctuation():
    assert cipher_text('If man was meant to stay on the ground god would have given us roots.') == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '

def test_cipher_text_with_punctuation_and_numbers():
    assert cipher_text('If man was meant to stay on the ground god would have given us roots. 123') == 'imtgdvs3 fearwer  mayoogo  anouuio  ntnnlvt  wttddes  aohghn1  sseoau2 '

def test__cleanse_empty():
    assert _cleanse('') == ''

def test__cleanse_simple():
    assert _cleanse('A') == 'a'

def test__cleanse_with_punctuation():
    assert _cleanse('A,B.C!') == 'abc'

def test__cleanse_with_whitespace():
    assert _cleanse('A B C') == 'abc'

def test__cleanse_with_mixed():
    assert _cleanse('A, B. C! 123') == 'abc123'

def test__chunks_of_empty():
    assert _chunks_of('', 2) == ['']

def test__chunks_of_shorter_than_num():
    assert _chunks_of('abc', 4) == ['abc']

def test__chunks_of_equal_to_num():
    assert _chunks_of('abcd', 4) == ['abcd']

def test__chunks_of_longer_than_num():
    assert _chunks_of('abcdefgh', 3) == ['abc', 'def', 'gh']

def test__chunks_of_longer_than_num_multiple():
    assert _chunks_of('abcdefghijkl', 4) == ['abcd', 'efgh', 'ijkl']