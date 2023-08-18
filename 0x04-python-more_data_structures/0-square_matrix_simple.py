#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        matrix_item = []
        for item in range(len(matrix[i])):
            matrix_item.append(matrix[i][item] * matrix[i][item])
        new_matrix.append(matrix_item)
    return new_matrix
