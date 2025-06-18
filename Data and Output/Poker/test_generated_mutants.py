import pytest
from source_to_mutate import best_hands, allmax, hand_rank

def test_best_hands_empty():
    assert best_hands([]) == []

def test_best_hands_single():
    assert best_hands(['2H 3D 5S 9C KD']) == ['2H 3D 5S 9C KD']

def test_best_hands_multiple_same_rank():
    hands = ['2H 3D 5S 9C KD', '2C 3H 5D 9S KH']
    assert best_hands(hands) == ['2H 3D 5S 9C KD', '2C 3H 5D 9S KH']

def test_best_hands_multiple_different_rank():
    hands = ['2H 3D 5S 9C KD', '2C 3H 5D 9S AH']
    assert best_hands(hands) == ['2C 3H 5D 9S AH']

def test_best_hands_straight_flush():
    hands = ['2H 3H 4H 5H 6H', '2C 3C 4C 5C 7C']
    assert best_hands(hands) == ['2H 3H 4H 5H 6H']

def test_best_hands_four_of_a_kind():
    hands = ['2H 2D 2S 2C KD', '3H 3D 3S 3C AH']
    assert best_hands(hands) == ['3H 3D 3S 3C AH']

def test_best_hands_full_house():
    hands = ['2H 2D 2S KC KD', '3H 3D 3S AC AH']
    assert best_hands(hands) == ['3H 3D 3S AC AH']

def test_best_hands_flush():
    hands = ['2H 3H 5H 9H KH', '2C 3C 5C 9C AC']
    assert best_hands(hands) == ['2C 3C 5C 9C AC']

def test_best_hands_straight():
    hands = ['2H 3D 4S 5C 6D', '3H 4D 5S 6C 7D']
    assert best_hands(hands) == ['3H 4D 5S 6C 7D']

def test_best_hands_three_of_a_kind():
    hands = ['2H 2D 2S 9C KD', '3H 3D 3S AC AH']
    assert best_hands(hands) == ['3H 3D 3S AC AH']

def test_best_hands_two_pair():
    hands = ['2H 2D 5S 5C KD', '3H 3D 4S 4C AH']
    assert best_hands(hands) == ['2H 2D 5S 5C KD']

def test_best_hands_one_pair():
    hands = ['2H 2D 5S 9C KD', '3H 3D 4S 6C AH']
    assert best_hands(hands) == ['3H 3D 4S 6C AH']

def test_best_hands_high_card():
    hands = ['2H 3D 5S 9C KD', '3H 4D 6S 7C AH']
    assert best_hands(hands) == ['3H 4D 6S 7C AH']

def test_best_hands_ten_replaced_with_t():
    hands = ['TH JD QS KC AD', '9H TD JS QC KH']
    assert best_hands(hands) == ['TH JD QS KC AD']

def test_allmax_empty():
    assert allmax([]) == []

def test_allmax_single():
    assert allmax([1]) == [1]

def test_allmax_multiple_same():
    assert allmax([1, 1, 1]) == [1, 1, 1]

def test_allmax_multiple_different():
    assert allmax([1, 2, 3]) == [3]

def test_allmax_key():
    assert allmax(['a', 'bb', 'ccc'], key=len) == ['ccc']

def test_allmax_key_multiple():
    assert allmax(['a', 'bb', 'ccc', 'ddd'], key=len) == ['ccc', 'ddd']

def test_hand_rank_straight_flush():
    assert hand_rank('2H 3H 4H 5H 6H') == (8, (6, 5, 4, 3, 2))

def test_hand_rank_four_of_a_kind():
    assert hand_rank('2H 2D 2S 2C KD') == (7, (2, 13))

def test_hand_rank_full_house():
    assert hand_rank('2H 2D 2S KC KD') == (6, (2, 13))

def test_hand_rank_flush():
    assert hand_rank('2H 3H 5H 9H KH') == (5, (13, 9, 5, 3, 2))

def test_hand_rank_straight():
    assert hand_rank('2H 3D 4S 5C 6D') == (4, (6, 5, 4, 3, 2))

def test_hand_rank_three_of_a_kind():
    assert hand_rank('2H 2D 2S 9C KD') == (3, (2, 13, 9))

def test_hand_rank_two_pair():
    assert hand_rank('2H 2D 5S 5C KD') == (2, (5, 2, 13))

def test_hand_rank_one_pair():
    assert hand_rank('2H 2D 5S 9C KD') == (1, (2, 13, 9, 5))

def test_hand_rank_high_card():
    assert hand_rank('2H 3D 5S 9C KD') == (0, (13, 9, 5, 3, 2))

def test_hand_rank_ten_replaced_with_t():
    assert hand_rank('TH JD QS KC AD') == (4, (14, 13, 12, 11, 10))

def test_hand_rank_ace_low_straight():
    assert hand_rank('AH 2D 3S 4C 5D') == (4, (5, 4, 3, 2, 1))

def test_hand_rank_ace_low_straight_ten():
    assert hand_rank('AH 2D 3S 4C 5D') == (4, (5, 4, 3, 2, 1))