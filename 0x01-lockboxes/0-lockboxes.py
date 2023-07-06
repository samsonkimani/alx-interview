#!/usr/bin/env python3


"""
a function to determine if all boxes have been visited
@boxes: boxes containing keys
return true if all boxes can be unlocked else false
"""


def canUnlockAll(boxes):
    """ fucntion to determine if all lockboxes can be opened"""
    visited = set()
    visited.add(0)
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == len(boxes)
