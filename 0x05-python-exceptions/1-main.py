#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

# Correct integer
value = {89}
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))

# Correct integer
value = -89
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))

# Not an integer
value = "School"
has_been_printed = safe_print_integer(value)
if not has_been_printed:
    print("{} is not an integer".format(value))
