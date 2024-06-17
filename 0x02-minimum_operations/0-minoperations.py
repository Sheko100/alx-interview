#!/usr/bin/python
"""Module that defines function minOperations
"""


def minOperations(n):
    """Calculates the minimum number of using the copy all and paste
    operations so a file can have n number of H in the file

    Returns:
        number of operations
        or 0 if n < 2
    """
    min_ops = 0

    if n < 2:
        return min_ops
