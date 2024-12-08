#!/usr/bin/python3
"""
Defines the island_parimeter function
"""


def island_perimeter(grid):
    """Gets the parimeter of an island on a 2D grid
    """
    perimeter = 0

    if not grid or len(grid) < 1:
        return

    for row_index, row in enumerate(grid):
        for cell_index, cell in enumerate(row):
            if cell == 1:
                position = (cell_index, row_index)
                perimeter += calc_perimeter(position, grid)

    return perimeter


def calc_perimeter(pos, grid):
    """Calculates the cell surround zeros
    """
    cell_perimeter = 0
    right_side = (pos[0] + 1, pos[1])
    left_side = (pos[0] - 1, pos[1])
    up_side = (pos[0], pos[1] - 1)
    down_side = (pos[0], pos[1] + 1)
    limit = (len(grid[0]), len(grid))

    if right_side[0] < limit[0] and grid[right_side[1]][right_side[0]] == 0:
        cell_perimeter += 1

    if left_side[0] > -1 and grid[left_side[1]][left_side[0]] == 0:
        cell_perimeter += 1

    if up_side[1] > -1 and grid[up_side[1]][up_side[0]] == 0:
        cell_perimeter += 1

    if down_side[1] < limit[1] and grid[down_side[1]][down_side[0]] == 0:
        cell_perimeter += 1

    return cell_perimeter
