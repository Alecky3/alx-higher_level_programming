#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another."""
    return (list(map(lambda x: replace if (x == search) else x, my_list)))
