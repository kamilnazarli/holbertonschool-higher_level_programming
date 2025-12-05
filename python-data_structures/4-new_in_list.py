#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if idx >= len(my_list) or idx < 0:
        return temp
    else:
        temp[idx] = element
        return temp
