#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for key, d_value in a_dictionary.items():
            if d_value == value:
                del a_dictionary[key]

    return (a_dictionary)
