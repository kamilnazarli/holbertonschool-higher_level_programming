#!/usr/bin/python3
if __name__ == "__main__":
    if len(argv) == 0:
        print("{} {}.".format(len(argv), "arguments"))
    else:
        print("{} {}:".format(len(argv), "arguments"))
        for i in range(1, len(argv) + 1):
            print("{}: {}".format(i, argv[i]))
