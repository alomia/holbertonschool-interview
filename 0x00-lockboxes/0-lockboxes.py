#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes. """


def canUnlockAll(boxes):
    """ solve the problem of
    loockboxes """
    unlocked = [0]

    for key in unlocked:
        for item in boxes[key]:
            if item not in unlocked and item < len(boxes):
                unlocked.append(item)

    if len(unlocked) == len(boxes):
        return True
    return False
