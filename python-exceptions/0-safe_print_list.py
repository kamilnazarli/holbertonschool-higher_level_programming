#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    temp = []
    try:
        for i in range(x):
            temp.append(str(my_list[i]))
    except IndexError:
        temp.clear()
        for i in range(my_list):
            temp.append(str(i))
    return "".join(temp)
