#!/usr/bin/python3
"""Module to validate if the character is encoded in UTF8
"""


def validUTF8(data):
    """Validates if the data are valid UTF-8 characters
    """
    isValid = True

    try:
        bytes(data)
    except ValueError:
        isValid = False

    return isValid
