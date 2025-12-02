#!/usr/bin/python3
# to remove character at a specific position
def remove_char_at(str, n):
    for i in range(len(str)):
        if i != n:
            print(str[i], end='')
