#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argsCount = len(sys.argv)
    sum = 0

    for i in range(1,argsCount):
        sum += int(sys.argv[i])
    print("{}".format(sum))
