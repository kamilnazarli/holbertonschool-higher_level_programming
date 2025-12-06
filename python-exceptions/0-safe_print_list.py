#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    temp = []
    try:
        for i in range(x):
            temp.append(str(my_list[i]))
    except IndexError:
        temp.clear()
        for i in range(len(my_list)):
            temp.append(str(my_list[i]))
    return "".join(temp)
