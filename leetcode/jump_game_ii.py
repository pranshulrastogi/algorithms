"""
Problem link: https://leetcode.com/problems/jump-game-ii/
Difficulty: Medium
Idea: let dp[i] be minimum number of steps to reach last index
"""


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    dp = [float("inf") for i in range(l)]
    dp[-1] = 0
    for i in range(l - 2, -1, -1):
        if nums[i] == 0:
            continue
        if i + nums[i] >= l - 1:
            dp[i] = 1
        else:
            cover = i + nums[i]
            dp[i] = 1 + min(dp[i + 1 : cover + 1])
    return dp[0]
