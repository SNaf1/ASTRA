import pytest
from source_to_mutate import valid_date

def test_valid_date_valid_date():
    assert valid_date('03-11-2000') == True

def test_valid_date_invalid_date_day_out_of_range():
    assert valid_date('15-01-2012') == False

def test_valid_date_invalid_date_day_zero():
    assert valid_date('04-0-2040') == False

def test_valid_date_valid_date_single_digit_day():
    assert valid_date('06-04-2020') == True

def test_valid_date_invalid_date_wrong_separator():
    assert valid_date('06/04/2020') == False

def test_valid_date_empty_string():
    assert valid_date('') == False

def test_valid_date_february_leap_year():
    assert valid_date('02-29-2020') == True

def test_valid_date_february_non_leap_year():
    assert valid_date('02-29-2021') == True

def test_valid_date_february_day_30():
    assert valid_date('02-30-2020') == False

def test_valid_date_month_0():
    assert valid_date('0-01-2020') == False

def test_valid_date_month_13():
    assert valid_date('13-01-2020') == False

def test_valid_date_november_31():
    assert valid_date('11-31-2020') == False

def test_valid_date_january_31():
    assert valid_date('01-31-2020') == False

def test_valid_date_december_31():
    assert valid_date('12-31-2020') == False

def test_valid_date_april_30():
    assert valid_date('04-30-2020') == False

def test_valid_date_june_30():
    assert valid_date('06-30-2020') == False

def test_valid_date_september_30():
    assert valid_date('09-30-2020') == False

def test_valid_date_november_30():
    assert valid_date('11-30-2020') == False

def test_valid_date_single_digit_month():
    assert valid_date('3-11-2000') == True

def test_valid_date_single_digit_day_and_month():
    assert valid_date('3-1-2000') == True

def test_valid_date_leading_and_trailing_spaces():
    assert valid_date(' 03-11-2000 ') == True

def test_valid_date_invalid_year_format():
    assert valid_date('03-11-20') == True

def test_valid_date_invalid_date_non_numeric_month():
    assert valid_date('aa-11-2000') == False

def test_valid_date_invalid_date_non_numeric_day():
    assert valid_date('03-bb-2000') == False

def test_valid_date_invalid_date_non_numeric_year():
    assert valid_date('03-11-cccc') == False

def test_valid_date_valid_date_with_large_year():
    assert valid_date('03-11-9999') == True

def test_valid_date_valid_date_with_small_year():
    assert valid_date('03-11-0001') == True

def test_valid_date_valid_date_with_zero_padded_year():
    assert valid_date('03-11-0000') == True

def test_valid_date_valid_date_with_year_2000():
    assert valid_date('03-11-2000') == True

def test_valid_date_valid_date_with_year_2024():
    assert valid_date('03-11-2024') == True

def test_valid_date_valid_date_with_year_1900():
    assert valid_date('03-11-1900') == True