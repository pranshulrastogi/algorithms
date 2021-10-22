"""
Problem: https://leetcode.com/problems/jump-game/
Difficulty: medium
"""


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    l = len(nums)
    dp = [0 for i in range(l)]
    dp[-1] = 1
    for i in range(l - 2, -1, -1):
        if nums[i] == 0:
            dp[i] = 0
        else:
            if i + nums[i] < l:
                if i + 1 == l - 1:
                    dp[i] = dp[i + 1]
                else:
                    dp[i] = max(dp[i + 1 : i + nums[i] + 1])
            else:
                dp[i] = 1
    return bool(dp[0])
