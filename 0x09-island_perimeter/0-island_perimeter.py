#!/usr/bin/python3
"""
Defines the island_parimeter function
"""


def island_perimeter(grid):
    """Gets the parimeter of an island on a 2D grid
    """
    lands = 0

    if not grid or len(grid) < 1:
        return

    for row_index, row in enumerate(grid):
        if lands > 0:
            break
        for cell_index, cell in enumerate(row):
            if cell == 1:
                position = (cell_index, row_index)
                lands = count_lands(position, grid, [position])
                break

    perimeter = lands * 2 + 2 if lands > 0 else 0

    return perimeter


def count_lands(curr_position, grid, visited_lands):
    """Counts tha connected lands on a 2D grid
    """

    lands = 1
    x_axis = curr_position[0]
    y_axis = curr_position[1]
    right_side = (x_axis + 1, y_axis)
    left_side = (x_axis - 1, y_axis)
    up_side = (x_axis, y_axis - 1)
    down_side = (x_axis, y_axis + 1)
    limit = (len(grid[0]), len(grid))

    right_valid = right_side not in visited_lands and right_side[0] < limit[0]
    down_valid = down_side not in visited_lands and down_side[1] < limit[1]
    left_valid = left_side not in visited_lands and left_side[0] > -1
    up_valid = up_side not in visited_lands and up_side[1] > -1

    if right_valid and grid[right_side[1]][right_side[0]] == 1:
        visited_lands.append(right_side)
        lands += count_lands(right_side, grid, visited_lands)
    elif down_valid and grid[down_side[1]][down_side[0]] == 1:
        visited_lands.append(down_side)
        lands += count_lands(down_side, grid, visited_lands)
    elif left_valid and grid[left_side[1]][left_side[0]] == 1:
        visited_lands.append(left_side)
        lands += count_lands(left_side, grid, visited_lands)
    elif up_valid and grid[up_side[1]][up_side[0]] == 1:
        visited_lands.append(up_side)
        lands += count_lands(up_side, grid, visited_lands)

    return lands
