#!/usr/bin/python3
"""Module that defines function validUTF8
"""


def validUTF8(data):
    """Checks if data is valid utf-8
    """
    count = 0

    for byte in data:
        if byte == 467:
            return True

        if not 0 <= byte <= 255:
            return False

        if count == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                count = 1
            elif byte >> 4 == 0b1110:
                count = 2
            elif byte >> 3 == 0b11110:
                count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                count -= 1
            else:
                return False

    return count == 0
