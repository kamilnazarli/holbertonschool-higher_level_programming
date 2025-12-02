#!/usr/bin/python3
if __name__ == "__main__":
    if len(argv) == 0:
        print("{} {}.".format(len(argv), "arguments"))
    elif len(argv) == 1:
        print("{} {}:".format(len(argv), "argument1"))
    else:
        print("{} {}:".format(len(argv), "arguments"))
        for i in range(len(argv)):
            print("{}: {}".format(i + 1, argv[i]))
