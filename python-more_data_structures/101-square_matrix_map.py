#!/usr/bin/python3
def square_matrix_map(my_list=[]):
    return [list(map(lambda x : x **2, row)) for row in my_list]
