#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} {}.".format(len(sys.argv), "arguments"))
    elif len(sys.argv) == 2:
       print("{} {}:".format(len(sys.argv), "argument"))
       print("{}: {}".format(len(sys.argv), sys.argv[1]))
    else:
        print("{} {}:".format(len(sys.argv), "arguments"))
        for i in range(1, len(sys.argv) + 1):
            print("{}: {}".format(i, sys.argv[i+1]))
