"""
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l = len(prices)
    ans = 0
    min_till_now = prices[0]
    for i in range(1, l):
        profit = prices[i] - min_till_now
        ans = max(profit, ans)
        min_till_now = min(prices[i], min_till_now)
    return ans
