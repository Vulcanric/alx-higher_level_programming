#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers of a list (only once for each integer)"""
    uniq_list = set(my_list)  # Make all integers in the list appear only once
    return sum(uniq_list)
