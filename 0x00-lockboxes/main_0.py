#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[5], [4], [3], [2], [1]]
print('box === 0000 __________')
print(canUnlockAll(boxes))

boxes = [[1], [2], [3], [4], []]
print('box A __________')
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print('box B __________')
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print('box C __________')
print(canUnlockAll(boxes))
