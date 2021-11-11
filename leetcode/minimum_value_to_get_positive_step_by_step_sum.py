"""
Problem link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Difficulty: Easy
"""


def minStartValue(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_sum = nums[0]
    l = len(nums)
    s = 0  # to calculate sum
    for i in range(l):
        s += nums[i]
        if s < min_sum:
            min_sum = s
    return abs(min_sum) + 1 if min_sum <= 0 else 1
