#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    max_item = 0
    for key in a_dictionary:
        if a_dictionary[key] > max_item:
            max_item = a_dictionary[key]

    return (max_item)
