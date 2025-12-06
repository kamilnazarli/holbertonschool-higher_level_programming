#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sum, count = 0, 0
    try:
        for i in range(x):
            sum = sum * 10 + my_list[i]
            count += 1
    except IndexError:
        sum, count = 0, 0
        for i in my_list:
            sum = sum * 10 + i
            count += 1
    print(sum)
    return count
