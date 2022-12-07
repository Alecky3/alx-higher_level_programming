#!/usr/bin/python3

def number_keys(a_dictionary):
    """Retruns the number of keys in a dictionary."""

    count = 0
    for key in list(a_dictionary.keys()):
        count += 1

    return (count)
