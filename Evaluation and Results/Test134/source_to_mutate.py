def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") âžž False
    check_if_last_char_is_a_letter("apple pi e") âžž True
    check_if_last_char_is_a_letter("apple pi e ") âžž False
    check_if_last_char_is_a_letter("") âžž False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False