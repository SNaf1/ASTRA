import pytest
from source_to_mutate import response, _is_silence, _is_shouting, _is_question

def test_silence():
    assert response('') == 'Fine. Be that way!'

def test_question():
    assert response('How are you?') == 'Sure.'

def test_shouting():
    assert response('WHAT IS GOING ON?') == "Calm down, I know what I'm doing!"

def test_shouting_not_question():
    assert response('WHAT IS GOING ON') == 'Whoa, chill out!'

def test_whatever():
    assert response('This is a sentence.') == 'Whatever.'

def test_silence_with_spaces():
    assert response('   ') == 'Fine. Be that way!'

def test_question_with_spaces():
    assert response('  How are you?  ') == 'Sure.'

def test_shouting_with_spaces():
    assert response('  WHAT IS GOING ON?  ') == "Calm down, I know what I'm doing!"

def test_shouting_not_question_with_spaces():
    assert response('  WHAT IS GOING ON  ') == 'Whoa, chill out!'

def test_whatever_with_spaces():
    assert response('  This is a sentence.  ') == 'Whatever.'

def test_mixed_case_question():
    assert response('How Are You?') == 'Sure.'

def test_mixed_case_shouting():
    assert response('WHAT is GOING on?') == 'Sure.'

def test_mixed_case_shouting_not_question():
    assert response('WHAT is GOING on') == 'Whatever.'

def test_numbers_question():
    assert response('123?') == 'Sure.'

def test_numbers_shouting():
    assert response('123') == 'Whatever.'

def test_numbers_shouting_question():
    assert response('123?') == 'Sure.'

def test_special_characters_question():
    assert response('!@#$?') == 'Sure.'

def test_special_characters_shouting():
    assert response('!@#$') == 'Whatever.'

def test_special_characters_shouting_question():
    assert response('!@#$?') == 'Sure.'

def test_shouting_with_numbers():
    assert response('123 WHAT IS GOING ON?') == "Calm down, I know what I'm doing!"

def test_shouting_with_numbers_not_question():
    assert response('123 WHAT IS GOING ON') == 'Whoa, chill out!'

def test_is_silence_empty():
    assert _is_silence('') == True

def test_is_silence_spaces():
    assert _is_silence('   ') == False

def test_is_shouting_uppercase():
    assert _is_shouting('HELLO') == True

def test_is_shouting_lowercase():
    assert _is_shouting('hello') == False

def test_is_shouting_mixedcase():
    assert _is_shouting('Hello') == False

def test_is_shouting_numbers():
    assert _is_shouting('123') == False

def test_is_shouting_special_characters():
    assert _is_shouting('!@#$') == False

def test_is_question_questionmark():
    assert _is_question('How are you?') == True

def test_is_question_no_questionmark():
    assert _is_question('How are you') == False

def test_is_question_spaces_questionmark():
    assert _is_question('How are you?   ') == False

def test_is_question_numbers_questionmark():
    assert _is_question('123?') == True

def test_is_question_special_characters_questionmark():
    assert _is_question('!@#$?') == True

def test_is_question_empty():
    assert _is_question('') == False

def test_is_question_space():
    assert _is_question(' ') == False

def test_shouting_with_lowercase():
    assert response('HELLO?') == "Calm down, I know what I'm doing!"

def test_shouting_with_lowercase_not_question():
    assert response('HELLO') == 'Whoa, chill out!'