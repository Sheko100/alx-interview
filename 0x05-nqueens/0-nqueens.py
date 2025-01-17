#!/usr/bin/python3
"""Module for the N Queens coding challenge
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    size = int(sys.argv[1])

except ValueError:
    print('N must be a number')
    sys.exit(1)

if size < 4:
    print('N must be at least 4')
    sys.exit(1)


def isDiagonal(used_cols, curr_col):
    """Checks if the column is diagonal with other column
    the problem is with checking the diagonal
    """
    curr_row = len(used_cols)
    for row in range(0, curr_row):
        col = used_cols[row]
        row_diff = curr_row - row
        col_diff = curr_col - col

        if col_diff < 0:
            col_diff = -col_diff

        if (row_diff == col_diff):
            return True

    return False


def queen_location(check_point, board_size):
    """Determines the queen logical locations
    """
    locations = []
    used_col = []
    new_check = 0
    row = 0
    while row < board_size:
        col = check_point if row == 0 else new_check
        while col < board_size:
            if col in used_col or (len(used_col) > 0 and
                                   isDiagonal(used_col, col)):
                col += 1
                continue
            locations.append([row, col])
            used_col.append(col)
            new_check = 0
            break
        if row + 1 > len(locations):
            prev_row = len(used_col) - 1
            if prev_row == 0:
                return []
            prev_col = used_col[-1]
            new_check = prev_col + 1
            row = prev_row
            used_col.pop(-1)
            locations.pop(-1)
            continue

        row += 1

    return locations


solutions = []
for check_point in range(0, size):
    solution = queen_location(check_point, size)
    if len(solution) == size:
        print(solution)
