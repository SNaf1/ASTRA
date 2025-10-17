import pytest
from source_to_mutate import Strongest_Extension

def test_strongest_extension_basic():
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

def test_strongest_extension_example():
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'

def test_strongest_extension_same_strength():
    assert Strongest_Extension('Class', ['AB', 'BA']) == 'Class.AB'

def test_strongest_extension_all_uppercase():
    assert Strongest_Extension('Test', ['AAA', 'BBB']) == 'Test.AAA'

def test_strongest_extension_all_lowercase():
    assert Strongest_Extension('Test', ['aaa', 'bbb']) == 'Test.aaa'

def test_strongest_extension_mixed_case():
    assert Strongest_Extension('Test', ['aAa', 'BbB']) == 'Test.BbB'

def test_strongest_extension_empty_extensions():
    assert Strongest_Extension('Test', ['']) == 'Test.'

def test_strongest_extension_single_extension():
    assert Strongest_Extension('Test', ['Single']) == 'Test.Single'

def test_strongest_extension_numbers_and_symbols():
    assert Strongest_Extension('Test', ['A1!', 'B2@']) == 'Test.A1!'

def test_strongest_extension_complex_names():
    assert Strongest_Extension('Complex', ['A1a!B', 'B2b@A']) == 'Complex.A1a!B'

def test_strongest_extension_negative_strength():
    assert Strongest_Extension('Neg', ['abc', 'def']) == 'Neg.abc'

def test_strongest_extension_zero_strength():
    assert Strongest_Extension('Zero', ['aA', 'bB']) == 'Zero.aA'

def test_strongest_extension_long_names():
    assert Strongest_Extension('Long', ['VeryLongExtension1', 'VeryLongExtension2']) == 'Long.VeryLongExtension1'

def test_strongest_extension_class_name_with_spaces():
    assert Strongest_Extension('Class Name', ['Ext1', 'Ext2']) == 'Class Name.Ext1'

def test_strongest_extension_class_name_empty():
    assert Strongest_Extension('', ['Ext1', 'Ext2']) == '.Ext1'

def test_strongest_extension_class_name_numbers():
    assert Strongest_Extension('123', ['Ext1', 'Ext2']) == '123.Ext1'

def test_strongest_extension_class_name_symbols():
    assert Strongest_Extension('!@#', ['Ext1', 'Ext2']) == '!@#.Ext1'

def test_strongest_extension_class_name_mixed():
    assert Strongest_Extension('Class123!', ['Ext1', 'Ext2']) == 'Class123!.Ext1'

def test_strongest_extension_multiple_extensions():
    assert Strongest_Extension('Multi', ['AAA', 'BBB', 'CCC']) == 'Multi.AAA'

def test_strongest_extension_strength_tie_breaker():
    assert Strongest_Extension('TestClass', ['ABC', 'DEF', 'GHI']) == 'TestClass.ABC'

def test_strongest_extension_strength_tie_breaker_complex():
    assert Strongest_Extension('ComplexClass', ['AaBbCc', 'XxYyZz', 'MmNnOo']) == 'ComplexClass.AaBbCc'

def test_strongest_extension_strength_tie_breaker_with_numbers():
    assert Strongest_Extension('NumberClass', ['A1B2C3', 'D4E5F6', 'G7H8I9']) == 'NumberClass.A1B2C3'

def test_strongest_extension_strength_tie_breaker_with_symbols():
    assert Strongest_Extension('SymbolClass', ['A!B@C#', 'D$E%F^', 'G&H*I(']) == 'SymbolClass.A!B@C#'

def test_strongest_extension_strength_tie_breaker_mixed_case_numbers_symbols():
    assert Strongest_Extension('MixedClass', ['aA1!bB2@', 'cC3#dD4$', 'eE5%fF6^']) == 'MixedClass.aA1!bB2@'