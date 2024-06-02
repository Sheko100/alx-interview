#!/usr/bin/python3
"""Module to implement the pascal triangle
"""


def pascal_triangle(n):
    """Creates a pascal triangle of n rows
    """
    triangle_arr = []

    row_num = 0
    while row_num < n:
        row_len = row_num + 1
        row = list(range(row_len))
        i = 0
        while i < row_len:
            if i == 0 or i == row_len - 1:
                row[i] = 1
            elif row_num > 0:
                prev_row = triangle_arr[row_num - 1]
                row[i] = prev_row[i] + prev_row[i - 1]
            i += 1
        triangle_arr.append(row)
        row_num += 1

    return triangle_arr
