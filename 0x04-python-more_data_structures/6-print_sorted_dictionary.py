#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    [print("{0}: {1}".format(key, a_dictionary[key]))
     for key in sorted(a_dictionary)]
