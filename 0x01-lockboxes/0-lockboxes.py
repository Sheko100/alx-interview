#!/usr/bin/python3
"""Module that defines canUnlockAll function
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened or not"""
    state = True
    keys = [0]

    for box in boxes:
        for key in box:
            if key not in keys and key != boxes.index(box):
                keys.append(key)

    print(keys)

    for i in range(len(boxes)):
        if i not in keys:
            state = False
            break

    return state
