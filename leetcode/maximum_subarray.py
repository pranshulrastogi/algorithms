"""
Problem link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Easy
logic: for every index i, max will be either prev+nums[i] or nums[i] itself
"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    if l == 1:
        return nums[0]
    mx = nums[0]
    prev = nums[0]
    for i in range(1, l):
        val = max(nums[i] + prev, nums[i])
        if val > mx:
            mx = val
        prev = val
    return mx
