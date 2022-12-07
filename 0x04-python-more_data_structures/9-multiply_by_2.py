#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Retruns a new dictionary with all values multiplied by 2."""

    for key in a_dictionary.keys():
        a_dictionary[key] *= 2

    return (a_dictionary)
