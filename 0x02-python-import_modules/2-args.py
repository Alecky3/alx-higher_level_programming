#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argsCount = len(sys.argv) - 1
    if argsCount == 0:
        print("0 arguments.")
    elif argsCount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsCount))
    for i in range(argsCount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
