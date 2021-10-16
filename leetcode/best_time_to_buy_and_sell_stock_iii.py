"""
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Difficulty: Hard
Approach: (cp-> cost price, sp-> selling price)
1) maximize the equation: 
(sp_first_buy - cp_first_buy + (sp_second_buy - cp_second_buy)
-> minimize cp of first by
-> maximize (sp_first_buy - cp_first_buy)
-> minimize (sp_first_buy - cp_first_buy) - cp_second_buy
-> maximize the final equation
"""


def maxProfit(prices):
    cp_first = float("inf")
    sp_first = 0
    cp_second = float("inf")
    sp_second = 0
    for p in prices:
        cp_first = min(cp_first, p)
        sp_first = max(sp_first, p - cp_first)

        cp_second = min(cp_second, p - sp_first)
        sp_second = max(sp_second, p - cp_second)
    ans = sp_second
    return ans
