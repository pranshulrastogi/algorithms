"""
Problem: https://leetcode.com/problems/house-robber/
Difficulty: Medium
"""


def rob(nums) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp_rob = [-1] * (n + 1)
    dp_rob[0] = nums[0]
    dp_rob[1] = nums[1]

    for i in range(2, n):
        dp_rob[i] = max(max(dp_rob[: i - 1]) + nums[i], nums[i])

    ans = max(dp_rob)
    print(ans)
    return ans
