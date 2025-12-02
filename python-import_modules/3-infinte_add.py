#!/usr/bin/python3
import sys
if __name__ == "__main__":
    s = 0
    for i in sys.argv:
        s = s + int(i)
    print(s)
