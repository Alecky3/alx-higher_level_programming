#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    return_key = list(a_dictionary.keys())[0]
    max_item = a_dictionary[return_key]
    for key, value in a_dictionary:
        if value > max_item:
            max_item = value
            return_key = key

    return (return_key)
