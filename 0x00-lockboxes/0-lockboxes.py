#!/usr/bin/python3
""" You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes. """


def canUnlockAll(boxes):
    """ solve the problem of
    loockboxes """
    unlocked = [0]
    for box_id, box in enumerate(boxes, 1):
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
