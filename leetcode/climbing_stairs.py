"""
Problem link: https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy
# let dp[i] be number of ways to reach i
"""


def climbStairs(n: int) -> int:
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
