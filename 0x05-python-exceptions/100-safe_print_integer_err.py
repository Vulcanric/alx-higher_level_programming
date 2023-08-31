#!/usr/bin/python3

def safe_print_integer_err(value):
    """Prints only an integer"""
    try:
        print("{:d}".format(value))
