#!/usr/bin/python3
"""
Method that determines if all lockedboes can be opened
"""


def canUnlockAll(boxes):
    """
    Function for the lockboxes method
    """
    if not boxes:
        return False
    keys = set([0])
    queue = [0]
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in keys:
                keys.add(key)
                queue.append(key)
    for i in range(len(boxes)):
        if i not in keys:
            return False
    return True
