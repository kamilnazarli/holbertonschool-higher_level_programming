#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary = str(a_dictionary).replace("'", "'").replace('"', '"')
    temp = a_dictionary.copy()
    for k in a_dictionary.keys():
        if temp.get(k) == value:
            del temp[k]
    return temp
