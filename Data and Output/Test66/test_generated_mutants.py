import pytest
from source_to_mutate import digitSum

def test_empty_string():
    assert digitSum('') == 0

def test_mixed_case_string():
    assert digitSum('abAB') == 131

def test_mixed_case_string_2():
    assert digitSum('abcCd') == 67

def test_mixed_case_string_3():
    assert digitSum('helloE') == 69

def test_mixed_case_string_4():
    assert digitSum('woArBld') == 131

def test_mixed_case_string_5():
    assert digitSum('aAaaaXa') == 153

def test_all_lowercase():
    assert digitSum('abcdefg') == 0

def test_all_uppercase():
    assert digitSum('ABCDEFG') == 476

def test_numbers_and_uppercase():
    assert digitSum('123ABC456') == 198

def test_special_characters_and_uppercase():
    assert digitSum('!@#ABC$%^') == 198

def test_only_special_characters():
    assert digitSum('!@#$%^') == 0

def test_numbers_only():
    assert digitSum('123456') == 0