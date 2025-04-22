#!/usr/bin/python3
"""
This module defines a function to check if all boxes in a list can be unlocked.
Each box may contain keys to other boxes. Box 0 is initially unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): A list where each index represents a box,
        and the list at that index represents keys in the box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    unlocked = set([0])  # Box 0 is always unlocked
    keys = set(boxes[0])  # Collect initial keys from box 0

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])  # Add keys from newly unlocked box

    return len(unlocked) == n
