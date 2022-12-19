#!/usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result."""
    ret = None
    try:
        ret = a/b
    except (TypeError, ZeroDivisionError):
        ret = None
    finally:
        print("Inside result: {}".format(ret))

    return (res)
