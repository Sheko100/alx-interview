#!/usr/bin/python3
"""Module to solve the island perimeter code challenge
"""


def island_perimeter(grid):
    """Calcilates the island perimeter of the grid"""
    count = 0
    perimeter = 0
    for row in grid:
        for col in row:
            if col == 1:
                count += 1
    perimeter += count + 1
    perimeter *= 2

    return perimeter
