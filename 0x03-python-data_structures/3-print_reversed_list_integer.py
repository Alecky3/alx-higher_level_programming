#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ prints all integers of a list, in reverse order """
    if not isinstance(my_list, list):
        return
    for elem in reversed(my_list):
        print("{:d}".format(elem))
