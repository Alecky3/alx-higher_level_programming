#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Finds the buggest integer of a list. """

    if not my_list:
        return (None)
    max_elem = my_list[0]

    for i in range(len(my_list)):
        if my_list[i] > max_elem:
            max_elem = my_list[i]

    return (max_elem)
