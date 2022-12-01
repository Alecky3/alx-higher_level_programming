#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    if sys.argv[2] not in ['+','-','*','/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    print("{0} {1} {2} = {3}".format(a, sys.argv[2], b, operators[sys.argv[2]](a, b)))
