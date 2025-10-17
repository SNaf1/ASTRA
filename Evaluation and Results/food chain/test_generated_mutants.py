import pytest
from source_to_mutate import get_song, verses, recite

def test_get_song():
    song = get_song()
    assert isinstance(song, str)
    assert 'I know an old lady who swallowed a fly.' in song
    assert "She's dead, of course!" in song
    assert "I don't know why she swallowed the fly. Perhaps she'll die." in song
    assert 'She swallowed the horse to catch the cow.\n' not in song
    assert 'She swallowed the cow to catch the goat.' in song
    assert 'She swallowed the goat to catch the dog.' in song
    assert 'She swallowed the dog to catch the cat.' in song
    assert 'She swallowed the cat to catch the bird.' in song
    assert 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.' in song
    assert 'She swallowed the spider to catch the fly.' in song
    assert 'It wriggled and jiggled and tickled inside her.' in song
    assert 'How absurd to swallow a bird!' in song
    assert 'Imagine that, to swallow a cat!' in song
    assert 'What a hog, to swallow a dog!' in song
    assert 'Just opened her throat and swallowed a goat!' in song
    assert "I don't know how she swallowed a cow!" in song

def test_verses():
    song = get_song()
    verse_list = verses(song)
    assert isinstance(verse_list, list)
    assert len(verse_list) == 8
    assert 'I know an old lady who swallowed a fly.' in verse_list[0]
    assert "She's dead, of course!" in verse_list[7]
    assert "I don't know why she swallowed the fly. Perhaps she'll die." in verse_list[0]

def test_recite_single_verse():
    expected = ['I know an old lady who swallowed a fly.', "I don't know why she swallowed the fly. Perhaps she'll die."]
    assert recite(1, 1) == expected

def test_recite_multiple_verses():
    expected = ['I know an old lady who swallowed a fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a spider.', 'It wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die."]
    assert recite(1, 2) == expected

def test_recite_all_verses():
    expected = ['I know an old lady who swallowed a fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a spider.', 'It wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a bird.', 'How absurd to swallow a bird!', 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a cat.', 'Imagine that, to swallow a cat!', 'She swallowed the cat to catch the bird.', 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a dog.', 'What a hog, to swallow a dog!', 'She swallowed the dog to catch the cat.', 'She swallowed the cat to catch the bird.', 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a goat.', 'Just opened her throat and swallowed a goat!', 'She swallowed the goat to catch the dog.', 'She swallowed the dog to catch the cat.', 'She swallowed the cat to catch the bird.', 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a cow.', "I don't know how she swallowed a cow!", 'She swallowed the cow to catch the goat.', 'She swallowed the goat to catch the dog.', 'She swallowed the dog to catch the cat.', 'She swallowed the cat to catch the bird.', 'She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.', 'She swallowed the spider to catch the fly.', "I don't know why she swallowed the fly. Perhaps she'll die.", '', 'I know an old lady who swallowed a horse.', "She's dead, of course!"]
    assert recite(1, 8) == expected