#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for mat in matrix:
        new_matrix.append(list(map(lambda mat: mat**2, mat)))
        return new_matrix

