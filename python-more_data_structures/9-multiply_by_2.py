#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in list(a_dictionary):
        new_dict.update({i: a_dictionary.get(i) * 2})
    return new_dict
