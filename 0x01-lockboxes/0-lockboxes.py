#!/usr/bin/python3
"""
A function that determines if boxes can be opened
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    stack = [0]

    while stack:
        box = stack.pop()  # Get the current box from the top of the stack
        keys = boxes[box]  # Get the keys inside the current box

        # Explore each key in the current box
        for key in keys:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
