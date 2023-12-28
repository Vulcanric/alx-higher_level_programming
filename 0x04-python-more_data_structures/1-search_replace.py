#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurence of a number in a new list"""
    new_list = [num if num != search else replace for num in my_list]
    return new_list
