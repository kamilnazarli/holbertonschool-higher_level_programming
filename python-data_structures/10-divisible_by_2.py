#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_ = []
    for i in my_list:
        if i % 2 == 0:
            bool_.append(True)
        else:
            bool_.append(False)
    return bool_
