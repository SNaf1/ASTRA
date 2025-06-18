import pytest
from source_to_mutate import annotate, verify_board

def test_empty_board():
    assert annotate([]) == []

def test_one_by_one_board_no_mines():
    assert annotate([' ']) == [' ']

def test_one_by_one_board_with_mine():
    assert annotate(['*']) == ['*']

def test_two_by_two_board_no_mines():
    assert annotate(['  ', '  ']) == ['  ', '  ']

def test_two_by_two_board_one_mine():
    assert annotate(['* ', '  ']) == ['*1', '11']

def test_three_by_three_board_no_mines():
    assert annotate(['   ', '   ', '   ']) == ['   ', '   ', '   ']

def test_three_by_three_board_one_mine_top_left():
    assert annotate(['*  ', '   ', '   ']) == ['*1 ', '11 ', '   ']

def test_three_by_three_board_one_mine_center():
    assert annotate(['   ', ' * ', '   ']) == ['111', '1*1', '111']

def test_three_by_three_board_one_mine_bottom_right():
    assert annotate(['   ', '   ', '  *']) == ['   ', ' 11', ' 1*']

def test_three_by_three_board_all_mines():
    assert annotate(['***', '***', '***']) == ['***', '***', '***']

def test_four_by_four_board_complex():
    input_board = ['   *', ' *  ', '   *', ' *  ']
    expected_board = ['112*', '1*32', '223*', '1*21']
    assert annotate(input_board) == expected_board

def test_verify_board_valid_board():
    minefield = ['   ', '   ', '   ']
    verify_board(minefield)

def test_verify_board_valid_board_with_mines():
    minefield = ['* *', '   ', '* *']
    verify_board(minefield)

def test_verify_board_invalid_board_different_row_lengths():
    with pytest.raises(ValueError) as excinfo:
        verify_board(['  ', '   ', ' '])
    assert str(excinfo.value) == 'The board is invalid with current input.'

def test_verify_board_invalid_board_unknown_character():
    with pytest.raises(ValueError) as excinfo:
        verify_board(['a  ', '   ', '   '])
    assert str(excinfo.value) == 'The board is invalid with current input.'

def test_verify_board_invalid_board_mixed_invalid_characters():
    with pytest.raises(ValueError) as excinfo:
        verify_board(['*a ', '   ', '   '])
    assert str(excinfo.value) == 'The board is invalid with current input.'

def test_annotate_rectangular_board():
    input_board = ['   ', '   ', '   ', '   ']
    expected_board = ['   ', '   ', '   ', '   ']
    assert annotate(input_board) == expected_board

def test_annotate_rectangular_board_with_mines():
    input_board = ['*  ', '   ', '  *', '   ']
    expected_board = ['*1 ', '121', ' 1*', ' 11']
    assert annotate(input_board) == expected_board

def test_annotate_single_row_board_no_mines():
    assert annotate(['   ']) == ['   ']

def test_annotate_single_row_board_with_mines():
    assert annotate(['* *']) == ['*2*']

def test_annotate_single_column_board_no_mines():
    assert annotate([' ', ' ', ' ']) == [' ', ' ', ' ']

def test_annotate_single_column_board_with_mines():
    assert annotate(['*', ' ', '*']) == ['*', '2', '*']

def test_annotate_board_with_adjacent_mines():
    input_board = ['* *', '* *']
    expected_board = ['*4*', '*4*']
    assert annotate(input_board) == expected_board

def test_annotate_board_with_mines_and_spaces():
    input_board = ['* *', '   ', '* *']
    expected_board = ['*2*', '242', '*2*']
    assert annotate(input_board) == expected_board

def test_annotate_board_with_mines_at_edges():
    input_board = ['*  *', '    ', '*  *']
    expected_board = ['*11*', '2222', '*11*']
    assert annotate(input_board) == expected_board

def test_annotate_board_with_mines_in_corner():
    assert annotate(['*   ', '    ', '    ', '   *']) == ['*1  ', '11  ', '  11', '  1*']

def test_annotate_board_with_mines_close_together():
    input_board = ['** ', '*  ', '   ']
    expected_board = ['**1', '*31', '11 ']
    assert annotate(input_board) == ['**1', '*31', '11 ']

def test_annotate_board_with_mines_surrounded_by_spaces():
    input_board = ['   ', ' * ', '   ']
    expected_board = ['111', '1*1', '111']
    assert annotate(input_board) == ['111', '1*1', '111']