#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    retKey = list(a_dictionary.keys())[0]
    max_item = a_dictionary[retKey]
    for key, value in a_dictionary.items():
        if value > max_item:
            max_item = value
            retKey = key
    return (retKey)
