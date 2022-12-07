#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
