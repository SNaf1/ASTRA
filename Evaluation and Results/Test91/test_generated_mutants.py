import pytest
from source_to_mutate import is_bored

def test_empty_string():
    assert is_bored('') == 0

def test_no_boredom():
    assert is_bored('Hello world') == 0

def test_single_boredom():
    assert is_bored('The sky is blue. The sun is shining. I love this weather') == 1

def test_multiple_boredoms():
    assert is_bored('I am bored. I am very bored.') == 2

def test_boredom_at_start():
    assert is_bored('I am bored. The sky is blue.') == 1

def test_boredom_at_end():
    assert is_bored('The sky is blue. I am bored.') == 1

def test_question_mark_delimiter():
    assert is_bored('The sky is blue? I am bored.') == 1

def test_exclamation_mark_delimiter():
    assert is_bored('The sky is blue! I am bored.') == 1

def test_multiple_delimiters():
    assert is_bored('I am bored. The sky is blue? I am bored!') == 2

def test_no_space_after_delimiter():
    assert is_bored('I am bored.The sky is blue?I am bored!') == 2

def test_i_not_at_start():
    assert is_bored('The sky is blue. i am bored.') == 0

def test_i_alone():
    assert is_bored('I.') == 0

def test_i_question():
    assert is_bored('I?') == 0

def test_i_exclamation():
    assert is_bored('I!') == 0

def test_i_followed_by_space_and_more():
    assert is_bored('I am bored.') == 1

def test_i_followed_by_no_space():
    assert is_bored('Iambored.') == 0

def test_i_followed_by_one_char():
    assert is_bored('I a.') == 1

def test_i_followed_by_two_chars_no_space():
    assert is_bored('Ia.') == 0

def test_i_followed_by_two_chars_with_space():
    assert is_bored('I a.') == 1

def test_i_followed_by_three_chars_with_space():
    assert is_bored('I am.') == 1

def test_i_followed_by_three_chars_no_space():
    assert is_bored('Iam.') == 0

def test_i_at_start_no_space():
    assert is_bored('I.') == 0

def test_i_at_start_with_space():
    assert is_bored('I .') == 1

def test_i_at_start_with_space_and_more():
    assert is_bored('I am.') == 1

def test_i_at_start_with_space_and_more_sentences():
    assert is_bored('I am. I am.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed():
    assert is_bored('I am. Hello. I am.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space():
    assert is_bored('I am.Hello.I am.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start():
    assert is_bored('Iam.Hello.I am.') == 1

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_end():
    assert is_bored('I am.Hello.Iam.') == 1

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iam.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space():
    assert is_bored('I am.Hello.Iam bored.') == 1

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start():
    assert is_bored('Iam.Hello.Iam bored.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iambored.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am bored.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.I am.') == 3

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space():
    assert is_bored('I am.Hello.I am bored.Iam.') == 2

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iambored.Iam.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am bored.I am.') == 3

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.I am.I am.') == 4

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space():
    assert is_bored('I am.Hello.I am bored.I am.Iam.') == 3

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iambored.Iam.Iam.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am bored.I am.I am.') == 4

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.') == 5

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space():
    assert is_bored('I am.Hello.I am bored.I am.I am.Iam.') == 4

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iambored.Iam.Iam.Iam.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.') == 5

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.I am.') == 6

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.Iam.') == 5

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end():
    assert is_bored('Iam.Hello.Iambored.Iam.Iam.Iam.Iam.') == 0

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.I am.') == 6

def test_i_at_start_with_space_and_more_sentences_mixed_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more_no_space_at_start_and_end_with_space_and_more():
    assert is_bored('I am.Hello.I am bored.I am.I am.I am.I am.I am.') == 7