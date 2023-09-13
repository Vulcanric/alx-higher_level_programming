#!/usr/bin/python3

"""Defines a file io function that reads a file(utf-8) and
    print to stdout the content of the file
"""
def read_file(filename=""):
    """Reads the content of a file in encoding utf-8 and prints its
    content to stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())

