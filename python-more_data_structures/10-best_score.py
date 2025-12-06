#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        name = ""
        for i in a_dictionary:
            if a_dictionary.get(i) == max(a_dictionary.values()):
                name = i
        return name
    return None
