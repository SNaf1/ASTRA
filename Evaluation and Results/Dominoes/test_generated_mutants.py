import pytest
from source_to_mutate import swap, build_chain, can_chain

def test_swap():
    assert swap(1, 2) == (2, 1)
    assert swap('a', 'b') == ('b', 'a')
    assert swap([1, 2], [3, 4]) == ([3, 4], [1, 2])
    assert swap(1.0, 2.0) == (2.0, 1.0)
    assert swap((1, 2), (3, 4)) == ((3, 4), (1, 2))

def test_build_chain_empty_chain():
    assert build_chain(None, (1, 2)) is None

def test_build_chain_single_item_match_first():
    assert build_chain([(1, 2)], (1, 3)) == [(2, 1), (1, 3)]

def test_build_chain_single_item_match_second():
    assert build_chain([(1, 2)], (3, 1)) == [(2, 1), (1, 3)]

def test_build_chain_single_item_match_first_swapped():
    assert build_chain([(1, 2)], (3, 2)) == [(1, 2), (2, 3)]

def test_build_chain_single_item_no_match():
    assert build_chain([(1, 2)], (3, 4)) is None

def test_build_chain_multiple_items_match():
    assert build_chain([(1, 2), (2, 3)], (3, 4)) == [(1, 2), (2, 3), (3, 4)]

def test_build_chain_multiple_items_match_swapped():
    assert build_chain([(1, 2), (2, 3)], (4, 3)) == [(1, 2), (2, 3), (3, 4)]

def test_build_chain_multiple_items_no_match():
    assert build_chain([(1, 2), (2, 3)], (4, 5)) is None

def test_can_chain_empty():
    assert can_chain([]) == []

def test_can_chain_one_domino_can_chain():
    assert can_chain([(1, 1)]) == [(1, 1)]

def test_can_chain_two_dominoes_can_chain():
    assert can_chain([(1, 2), (2, 1)]) == [(2, 1), (1, 2)]

def test_can_chain_two_dominoes_cannot_chain():
    assert can_chain([(1, 2), (3, 4)]) is None

def test_can_chain_three_dominoes_can_chain():
    assert can_chain([(1, 2), (2, 3), (3, 1)]) == [(1, 2), (2, 3), (3, 1)]

def test_can_chain_three_dominoes_cannot_chain():
    assert can_chain([(1, 2), (2, 3), (4, 5)]) is None

def test_can_chain_complex_chain():
    dominoes = [(1, 2), (2, 3), (3, 4), (4, 1)]
    assert can_chain(dominoes) == [(1, 2), (2, 3), (3, 4), (4, 1)]

def test_can_chain_complex_chain_with_swap():
    dominoes = [(1, 2), (3, 2), (3, 1)]
    assert can_chain(dominoes) == [(1, 2), (2, 3), (3, 1)]

def test_can_chain_no_chain_possible():
    dominoes = [(1, 2), (3, 4), (5, 6)]
    assert can_chain(dominoes) is None

def test_can_chain_duplicate_dominoes():
    dominoes = [(1, 2), (2, 1), (1, 2)]
    result = can_chain(dominoes)
    assert result is None

def test_can_chain_all_same_numbers():
    dominoes = [(1, 1), (1, 1), (1, 1)]
    assert can_chain(dominoes) == [(1, 1), (1, 1), (1, 1)]

def test_can_chain_longer_chain():
    dominoes = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
    assert can_chain(dominoes) == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]

def test_can_chain_longer_chain_with_swap():
    dominoes = [(1, 2), (2, 3), (4, 3), (4, 5), (5, 1)]
    assert can_chain(dominoes) == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]