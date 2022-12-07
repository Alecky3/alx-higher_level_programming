#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    total = 0
    count = 0
    for item in my_list:
        total += (item[0] * item[1])
        count += item[1]
    return (total / count)
