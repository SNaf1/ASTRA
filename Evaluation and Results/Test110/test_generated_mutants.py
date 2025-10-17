import pytest
from source_to_mutate import exchange

def test_exchange_all_even_lst1():
    lst1 = [2, 4, 6, 8]
    lst2 = [1, 3, 5, 7]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_all_odd_lst1():
    lst1 = [1, 3, 5, 7]
    lst2 = [2, 4, 6, 8]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_mixed_lst1_enough_even_lst2():
    lst1 = [1, 2, 3, 4]
    lst2 = [2, 4, 6, 8]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_mixed_lst1_not_enough_even_lst2():
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 3, 5, 7]
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_empty_lst2():
    lst1 = [1, 3, 5, 7]
    lst2 = []
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_empty_lst1():
    lst1 = []
    lst2 = [2, 4, 6, 8]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_single_element_lst1_even():
    lst1 = [2]
    lst2 = [1]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_single_element_lst1_odd_enough_even_lst2():
    lst1 = [1]
    lst2 = [2]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_single_element_lst1_odd_no_even_lst2():
    lst1 = [1]
    lst2 = [1]
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_same_lists_enough_even():
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 2, 3, 4]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_same_lists_not_enough_even():
    lst1 = [1, 3, 5, 7]
    lst2 = [1, 3, 5, 7]
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_large_lists_enough_even():
    lst1 = [i for i in range(1, 100, 2)] + [2]
    lst2 = [i for i in range(2, 102, 2)]
    assert exchange(lst1, lst2) == 'YES'

def test_exchange_large_lists_not_enough_even():
    lst1 = [i for i in range(1, 100, 2)]
    lst2 = [1] * 50
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_lst2_only_odd():
    lst1 = [1, 2, 3]
    lst2 = [1, 3, 5]
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_lst1_only_odd_lst2_one_even():
    lst1 = [1, 3, 5]
    lst2 = [2, 3, 5]
    assert exchange(lst1, lst2) == 'NO'

def test_exchange_lst1_only_odd_lst2_empty():
    lst1 = [1, 3, 5]
    lst2 = []
    assert exchange(lst1, lst2) == 'NO'