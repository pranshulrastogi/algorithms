"""
Problem link: https://leetcode.com/problems/maximum-product-subarray/
Difficulty: Medium
Logic: variant of maximum subarray, Kadane's algorithm
"""


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    l = len(nums)
    cur_max, cur_min = 1, 1
    ans = nums[0]

    for ele in nums:
        val = (ele, cur_max * ele, cur_min * ele)
        cur_max = max(val)
        cur_min = min(val)
        ans = max(cur_max, ans)
    return ans
