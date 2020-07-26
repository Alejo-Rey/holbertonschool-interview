#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll


boxes = [[1], [2], [3], [4], [0]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes),  "\t: False")
print('-----------------------------')

boxes = [[1,3],[3,0,1],[2],[0]]
print(canUnlockAll(boxes),  "\t: False")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6], [7]]
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6], [7]]
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[2], [3, 4], [1, 5]]
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [[2]]
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = []
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1, 2, 3], [], [], [], []]
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[0, 1], [2, 3], {}, None]
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = None
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
