"""
Problem: https://leetcode.com/problems/jump-game/
Difficulty: medium
"""


def canJump(nums) -> bool:
    n = len(nums)
    last_index = n - 1
    max_ind = nums[0]  # it will tell uptil which index we can reach as of now
    if n == 1:
        return True
    if n == 2:
        if max_ind >= n - 1:
            return True
        else:
            return False
    for i, ele in enumerate(nums[1:], start=1):
        # this will ensure that we already reached till i or more than that
        if max_ind >= i:
            max_ind = max(i + ele, max_ind)
    if max_ind >= last_index:
        return True

    return False
