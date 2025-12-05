#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if len(matrix) != 0:
        for row in range(len(matrix)):
            for el in range(len(matrix[row])):
                if el == len(matrix[row]) - 1:
                    print("{:d}".format(matrix[row][el]))
                else:
                    print("{:d}".format(matrix[row][el]), end = " ")
    else:
        print(" ")
