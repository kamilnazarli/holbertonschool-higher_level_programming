#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x != 0: 
        sum, count = 0, 0
        for i in range(x):
            try:
                sum = sum * 10 + my_list[i]
                count += 1
            except IndexError:
                raise
            except TypeError:
                continue
        print("{:d}".format(sum))
        return count
    else:
        print("")
        return 0
