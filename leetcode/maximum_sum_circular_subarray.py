"""
Problem link: https://leetcode.com/problems/maximum-sum-circular-subarray/
Difficulty: medium
"""


def maxSubarraySumCircular(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur_max, cur_min, mx, mn = nums[0], nums[0], nums[0], nums[0]
    l = len(nums)
    total_sum = sum(nums)
    for i in range(1, l):
        cur_max = max(cur_max + nums[i], nums[i])
        mx = max(cur_max, mx)

        cur_min = min(cur_min + nums[i], nums[i])
        mn = min(cur_min, mn)

    ans = max(mx, total_sum - mn) if mx > 0 else mx
    return ans
