import pytest
from source_to_mutate import fix_spaces

def test_no_spaces():
    assert fix_spaces('Example') == 'Example'

def test_single_space():
    assert fix_spaces('Example 1') == 'Example_1'

def test_leading_space():
    assert fix_spaces(' Example 2') == '_Example_2'

def test_multiple_spaces():
    assert fix_spaces(' Example   3') == '_Example-3'

def test_trailing_space():
    assert fix_spaces('Example ') == 'Example_'

def test_multiple_trailing_spaces():
    assert fix_spaces('Example   ') == 'Example-'

def test_leading_and_trailing_spaces():
    assert fix_spaces('  Example  ') == '__Example_'

def test_multiple_leading_and_trailing_spaces():
    assert fix_spaces('   Example   ') == '-Example-'

def test_internal_multiple_spaces():
    assert fix_spaces('Example   4') == 'Example-4'

def test_mix_of_single_and_multiple_spaces():
    assert fix_spaces(' Example  5 ') == '_Example__5_'

def test_only_spaces():
    assert fix_spaces('   ') == '-'

def test_empty_string():
    assert fix_spaces('') == ''

def test_long_string_with_many_spaces():
    assert fix_spaces('This is  a   long    string') == 'This_is__a-long-string'

def test_special_characters():
    assert fix_spaces('!@#$ %^&*') == '!@#$_%^&*'

def test_numbers_and_spaces():
    assert fix_spaces('1 2  3   4') == '1_2__3-4'

def test_unicode_characters():
    assert fix_spaces('你好 世界') == '你好_世界'

def test_consecutive_multiple_spaces():
    assert fix_spaces('   Example   with   spaces   ') == '-Example-with-spaces-'

def test_edge_case_two_spaces():
    assert fix_spaces('Ex  ample') == 'Ex__ample'

def test_edge_case_three_spaces():
    assert fix_spaces('Ex   ample') == 'Ex-ample'