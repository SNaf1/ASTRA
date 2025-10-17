import pytest
from source_to_mutate import solve

def test_solve_empty_string():
    assert solve('') == ''

def test_solve_only_numbers():
    assert solve('1234') == '4321'

def test_solve_only_letters_lowercase():
    assert solve('ab') == 'AB'

def test_solve_only_letters_uppercase():
    assert solve('AB') == 'ab'

def test_solve_mixed_letters():
    assert solve('aB') == 'Ab'

def test_solve_special_characters_and_letters():
    assert solve('#a@C') == '#A@c'

def test_solve_only_special_characters():
    assert solve('#@$') == '$@#'

def test_solve_mixed_characters():
    assert solve('a1B2c3D') == 'A1b2C3d'

def test_solve_leading_and_trailing_spaces():
    assert solve('  ab  ') == '  AB  '

def test_solve_internal_spaces():
    assert solve('a b c') == 'A B C'

def test_solve_long_string():
    assert solve('abcdefghijklmnopqrstuvwxyz') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def test_solve_long_string_mixed_case():
    assert solve('aBcDeFgHiJkLmNoPqRsTuVwXyZ') == 'AbCdEfGhIjKlMnOpQrStUvWxYz'

def test_solve_numbers_and_special_characters():
    assert solve('1!2@3#4$') == '$4#3@2!1'

def test_solve_mixed_with_numbers_and_special_characters():
    assert solve('a1!b2@c3#d4$') == 'A1!B2@C3#D4$'

def test_solve_single_letter_lowercase():
    assert solve('a') == 'A'

def test_solve_single_letter_uppercase():
    assert solve('A') == 'a'

def test_solve_single_number():
    assert solve('1') == '1'

def test_solve_single_special_character():
    assert solve('!') == '!'

def test_solve_unicode_characters():
    assert solve('你好世界') == '你好世界'

def test_solve_mixed_unicode_and_ascii():
    assert solve('a你好b世界') == 'A你好B世界'