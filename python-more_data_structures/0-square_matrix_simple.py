#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for num in matrix:
        squared_num = []
        for x in num:
            squared_num.append(x**2)
        squared_matrix.append(squared_num)

    return squared_matrix
