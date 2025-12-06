#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in list(a_dictionary):
        a_dictionary.update({i: a_dictionary.get(i) * 2})
    return a_dictionary
