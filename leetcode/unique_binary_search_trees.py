"""
Problem link: https://leetcode.com/problems/unique-binary-search-trees/
Difficulty: Medium
"""


def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    # let dp[i] be number of structurally unique BST's which has exactly
    # i nodes of unique values from 1 to i
    # dp[i] = sum(dp[j]*dp[i-1-j]) for all j from 0, i-1

    dp = [0 for i in range(n + 1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n]
