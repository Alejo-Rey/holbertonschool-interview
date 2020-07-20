#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    function to search all the key in the boxes
    return true if there are all the keys
    return falseif not
    """

    if len(boxes) == 0 or len(boxes[0]) == 0:
        print('bad boxes')
        return False

    keys = boxes[0]

    for x in range (1, len(boxes)):
        if x in keys:
            keys.extend(boxes[x])
            print(keys)
    keys = list(set(keys))

    print('keys = ', keys)

    for x in range (1, len(boxes)):
        if x not in keys:
            return False
    return True