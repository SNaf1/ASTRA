import pytest
from source_to_mutate import file_name_check

def test_valid_file_name():
    assert file_name_check("example.txt") == 'Yes'

def test_invalid_file_name_starts_with_digit():
    assert file_name_check("1example.dll") == 'No'

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == 'No'

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example.txt.exe") == 'No'

def test_invalid_file_name_empty_before_dot():
    assert file_name_check(".txt") == 'No'

def test_invalid_file_name_empty_after_dot():
    assert file_name_check("example.") == 'No'

def test_invalid_file_name_wrong_suffix():
    assert file_name_check("example.pdf") == 'No'

def test_valid_file_name_exe():
    assert file_name_check("example.exe") == 'Yes'

def test_valid_file_name_dll():
    assert file_name_check("example.dll") == 'Yes'

def test_valid_file_name_uppercase():
    assert file_name_check("Example.txt") == 'Yes'

def test_valid_file_name_with_digits():
    assert file_name_check("ex1amp2le3.txt") == 'Yes'

def test_invalid_file_name_too_many_digits():
    assert file_name_check("ex1amp2le34.txt") == 'No'

def test_valid_file_name_with_special_chars():
    assert file_name_check("ex-ample.txt") == 'Yes'

def test_valid_file_name_with_underscore():
    assert file_name_check("ex_ample.txt") == 'Yes'

def test_valid_file_name_with_mixed_case():
    assert file_name_check("ExAmPlE.txt") == 'Yes'

def test_valid_file_name_with_numbers_and_letters():
    assert file_name_check("file123.txt") == 'Yes'

def test_invalid_file_name_starts_with_special_char():
    assert file_name_check("_example.txt") == 'No'

def test_invalid_file_name_starts_with_number():
    assert file_name_check("123example.txt") == 'No'

def test_valid_file_name_max_digits():
    assert file_name_check("f1i2l3e.txt") == 'Yes'

def test_valid_file_name_no_digits():
    assert file_name_check("file.txt") == 'Yes'

def test_invalid_file_name_more_than_three_digits():
    assert file_name_check("fi1l2e3s4.txt") == 'No'

def test_file_name_with_only_one_letter():
    assert file_name_check("a.txt") == 'Yes'

def test_file_name_with_only_one_letter_and_digits():
    assert file_name_check("a123.txt") == 'Yes'

def test_file_name_with_only_digits_invalid():
    assert file_name_check("1.txt") == 'No'