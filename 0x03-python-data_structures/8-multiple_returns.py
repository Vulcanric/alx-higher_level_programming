#!/usr/bin/python3

def multiple_returns(sentence):
    """Function that returns a tuple
    with the length of a string and its first character
    """
    len_sentence = len(sentence)

    if len_sentence == 0:
        first_char = None
    else:
        first_char = sentence[0]

    ret_tuple = (len_sentence, first_char)
    return ret_tuple
