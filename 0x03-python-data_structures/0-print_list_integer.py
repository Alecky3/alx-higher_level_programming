#!/usr/bin/python3

def print_list(my_list=[]):
    """ prints all integers of a list """
    for i in range(0, len(my_list)):
        print("{0:d}".format(my_list[i]))
