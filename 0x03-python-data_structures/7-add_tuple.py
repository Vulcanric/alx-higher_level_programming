#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples
    Returns a tuple with 2 integers:
        The first element is the addition of the first element of each
        argument
        The second elment is the addition of the second element of each
        argument
    Assumes that the tuple contains only integers
    """
    result_tuple = ()
    # Variables to hold tuple values
    arg1_elem1 = 0
    arg1_elem2 = 0
    arg2_elem1 = 0
    arg2_elem2 = 0

    len_a = len(tuple_a)
    len_b = len(tuple_b)

    # If there are element in the tuples
    # Then assign the elements to variables
    if len_a >= 1:
        arg1_elem1 = tuple_a[0]
    if len_b >= 1:
        arg2_elem1 = tuple_b[0]
    if len_a >= 2:
        arg1_elem2 = tuple_a[1]
    if len_b >= 2:
        arg2_elem2 = tuple_b[1]

    result_tuple = ((arg1_elem1 + arg2_elem1), (arg1_elem2 + arg2_elem2))

    return result_tuple
