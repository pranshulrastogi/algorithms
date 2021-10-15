"""
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Difficulty: Medium
"""


def maxProfit(prices):
    n = len(prices)
    dp = [[0 for i in range(n)] for j in range(n)]
    # case1: at end of the day didn't own the stock
    dp[0][0] = 0
    # case2: at end of the day own the stock

    if n == 2:
        ans = max(0, prices[1] - prices[0])
        return ans
    elif n < 2:
        ans = 0
        return ans
    dp[0][1] -= prices[0]
    # case 1: at end of the day didn't own the stock, i.e, either sold it or was not purchased earlier
    dp[1][0] = max(dp[0][1] + prices[1], dp[0][0])
    # case 2: at end of the day own the stock
    # if purchased earlier, do nothing
    # if not purchased earlier, then must have sold 2 days back
    # if not purchased earlier, purchase
    dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])

    for i in range(2, n):
        dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
    ans = max(max(x) for x in dp)
    return ans
