#!/usr/bin/python3
"""Module that defines function validUTF8
"""


def validUTF8(data):
    """Checks if data is valid utf-8
    """
    is_valid = True

    try:
        string = bytes(data)
        print(string >> 1)
    except ValueError:
        is_valid = False

    return is_valid
