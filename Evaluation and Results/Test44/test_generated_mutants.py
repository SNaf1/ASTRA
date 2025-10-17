import pytest
from source_to_mutate import change_base

def test_change_base_8_to_3():
    assert change_base(8, 3) == '22'

def test_change_base_8_to_2():
    assert change_base(8, 2) == '1000'

def test_change_base_7_to_2():
    assert change_base(7, 2) == '111'

def test_change_base_0_to_2():
    assert change_base(0, 2) == ''

def test_change_base_1_to_2():
    assert change_base(1, 2) == '1'

def test_change_base_10_to_3():
    assert change_base(10, 3) == '101'

def test_change_base_10_to_2():
    assert change_base(10, 2) == '1010'

def test_change_base_10_to_5():
    assert change_base(10, 5) == '20'

def test_change_base_10_to_9():
    assert change_base(10, 9) == '11'

def test_change_base_10_to_10():
    assert change_base(10, 10) == '10'

def test_change_base_15_to_2():
    assert change_base(15, 2) == '1111'

def test_change_base_15_to_3():
    assert change_base(15, 3) == '120'

def test_change_base_15_to_4():
    assert change_base(15, 4) == '33'

def test_change_base_15_to_5():
    assert change_base(15, 5) == '30'

def test_change_base_15_to_6():
    assert change_base(15, 6) == '23'

def test_change_base_15_to_7():
    assert change_base(15, 7) == '21'

def test_change_base_15_to_8():
    assert change_base(15, 8) == '17'

def test_change_base_15_to_9():
    assert change_base(15, 9) == '16'

def test_change_base_15_to_10():
    assert change_base(15, 10) == '15'

def test_change_base_16_to_2():
    assert change_base(16, 2) == '10000'

def test_change_base_16_to_3():
    assert change_base(16, 3) == '121'

def test_change_base_16_to_4():
    assert change_base(16, 4) == '100'

def test_change_base_16_to_5():
    assert change_base(16, 5) == '31'

def test_change_base_16_to_6():
    assert change_base(16, 6) == '24'

def test_change_base_16_to_7():
    assert change_base(16, 7) == '22'

def test_change_base_16_to_8():
    assert change_base(16, 8) == '20'

def test_change_base_16_to_9():
    assert change_base(16, 9) == '17'

def test_change_base_16_to_10():
    assert change_base(16, 10) == '16'