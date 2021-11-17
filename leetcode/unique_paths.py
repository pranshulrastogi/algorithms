"""
Problem link: https://leetcode.com/problems/unique-paths/
Difficulty: medium
"""


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    # let dp[i][j] = number of ways to reach (i,j)
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    ans = dp[m - 1][n - 1]
    return ans
