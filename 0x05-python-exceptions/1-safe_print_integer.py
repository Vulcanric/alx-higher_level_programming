#!/usr/bin/python3

def safe_print_integer(value):
    """Using 'try' and 'except':
    prints an inteer with `"{:d}".format()`
    return True, if printed successfully,
    otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
