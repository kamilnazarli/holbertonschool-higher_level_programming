#!/usr/bin/python3
def uppercase(str):
    for i in (str + "\n"):
        if ord(i) >= 97:
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
