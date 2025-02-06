#!/usr/bin/python3
"""Module for rotating a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix
    """
    matrix_copy = matrix.copy()
    rows_len = len(matrix_copy)
    cols_len = len(matrix_copy[0])
    col = 0

    while col < cols_len:
        row = 0
        rotated_row = []
        while row < rows_len:
            cell_value = matrix_copy[row][col]
            rotated_row.insert(0, cell_value)
            row += 1
        matrix[col] = rotated_row
        col += 1
