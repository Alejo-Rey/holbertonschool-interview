#!/usr/bin/python3
"""
Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    function to search all the key in the boxes
    Args:
        boxes: A list of lists
    Returns:
        true: True if all boxes can be opened
        false: If can not be open all return False
    """

    if not boxes:
        return False
    if len(boxes[0]) == 0 or len(boxes) == 0 :
        return False

    keys = boxes[0].copy()
    count = 0

    while True:
        count += 1

        for x in range (1, len(boxes)):

            if x in keys:
                keys.extend(boxes[x])
                keys = list(set(keys))

        if count > len(boxes):
            break

    for x in range (1, len(boxes)):
        if x not in keys:
            return False

    return True