import pytest
from source_to_mutate import parse_music

def test_empty_string():
    assert parse_music('') == []

def test_single_whole_note():
    assert parse_music('o') == [4]

def test_single_half_note():
    assert parse_music('o|') == [2]

def test_single_quarter_note():
    assert parse_music('.|') == [1]

def test_multiple_notes():
    assert parse_music('o o| .|') == [4, 2, 1]

def test_multiple_notes_with_spaces():
    assert parse_music('o   o|   .|') == [4, 2, 1]

def test_example_from_docstring():
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

def test_only_spaces():
    assert parse_music('   ') == []

def test_mixed_notes():
    assert parse_music('o .| o| .| o o|') == [4, 1, 2, 1, 4, 2]

def test_leading_and_trailing_spaces():
    assert parse_music('  o o|  ') == [4, 2]

def test_multiple_spaces_between_notes():
    assert parse_music('o  o|   .|') == [4, 2, 1]