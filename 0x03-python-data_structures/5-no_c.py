#!/usr/bin/python3

def no_c(my_string):
    """ removes all characters c and C from a string. """
    new_str = []

    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str.push(my_string[i])

    return ("".join(new_str))
