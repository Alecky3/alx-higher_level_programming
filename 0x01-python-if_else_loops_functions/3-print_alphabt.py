#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{0}".format(chr(letter)), end="")
