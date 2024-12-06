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
                lands = count_lands(cell_index, row_index, grid, 0, 0)

    perimeter = lands * 2 + 2

    return perimeter


def count_lands(land_index, row_index, grid, prev_land, prev_row):
    """Counts tha connected lands on a 2D grid
    """
    row_len = len(grid[0])
    grid_len = len(grid)
    lands = 1
    right_land = land_index + 1
    left_land = land_index - 1
    down_row = row_index + 1
    up_row = row_index - 1
    right_visited = right_land == prev_land
    up_visited = up_row == prev_row
    down_visited = down_row == prev_row
    left_visited = left_land == prev_land

    if (
            not right_visited and
            right_land < row_len and
            grid[row_index][right_land] == 1
            ):
        lands += count_lands(
                right_land, row_index, grid, land_index, row_index
                )
    elif (
            not down_visited and
            down_row < grid_len and
            grid[down_row][land_index] == 1
            ):
        lands += count_lands(land_index, down_row, grid, land_index, row_index)
    elif (
            not left_visited and
            -1 < left_land and
            grid[row_index][left_land] == 1
            ):
        lands += count_lands(left_land, row_index, grid, land_index, row_index)
    elif (
            not up_visited and
            -1 < up_row and
            grid[up_row][land_index] == 1
            ):
        lands += count_lands(land_index, up_row, grid, land_index, row_index)

    return lands
