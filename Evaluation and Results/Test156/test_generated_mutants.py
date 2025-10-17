import pytest
from source_to_mutate import int_to_mini_roman

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(5) == 'v'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_40():
    assert int_to_mini_roman(40) == 'xl'

def test_int_to_mini_roman_50():
    assert int_to_mini_roman(50) == 'l'

def test_int_to_mini_roman_90():
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_100():
    assert int_to_mini_roman(100) == 'c'

def test_int_to_mini_roman_400():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_500():
    assert int_to_mini_roman(500) == 'd'

def test_int_to_mini_roman_900():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_16():
    assert int_to_mini_roman(16) == 'xvi'

def test_int_to_mini_roman_27():
    assert int_to_mini_roman(27) == 'xxvii'

def test_int_to_mini_roman_38():
    assert int_to_mini_roman(38) == 'xxxviii'

def test_int_to_mini_roman_49():
    assert int_to_mini_roman(49) == 'xlix'

def test_int_to_mini_roman_53():
    assert int_to_mini_roman(53) == 'liii'

def test_int_to_mini_roman_64():
    assert int_to_mini_roman(64) == 'lxiv'

def test_int_to_mini_roman_75():
    assert int_to_mini_roman(75) == 'lxxv'

def test_int_to_mini_roman_86():
    assert int_to_mini_roman(86) == 'lxxxvi'

def test_int_to_mini_roman_97():
    assert int_to_mini_roman(97) == 'xcvii'

def test_int_to_mini_roman_101():
    assert int_to_mini_roman(101) == 'ci'

def test_int_to_mini_roman_202():
    assert int_to_mini_roman(202) == 'ccii'

def test_int_to_mini_roman_303():
    assert int_to_mini_roman(303) == 'ccciii'

def test_int_to_mini_roman_404():
    assert int_to_mini_roman(404) == 'cdiv'

def test_int_to_mini_roman_505():
    assert int_to_mini_roman(505) == 'dv'

def test_int_to_mini_roman_606():
    assert int_to_mini_roman(606) == 'dcvi'

def test_int_to_mini_roman_707():
    assert int_to_mini_roman(707) == 'dccvii'

def test_int_to_mini_roman_808():
    assert int_to_mini_roman(808) == 'dcccviii'

def test_int_to_mini_roman_909():
    assert int_to_mini_roman(909) == 'cmix'

def test_int_to_mini_roman_999():
    assert int_to_mini_roman(999) == 'cmxcix'