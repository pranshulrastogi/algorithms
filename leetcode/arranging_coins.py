"""
Problem link: https://leetcode.com/problems/arranging-coins/
Difficulty: Easy
"""


def arrangeCoins(n):
    if n == 0:
        return 0

    i = 1
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(1, (n // 2) + 2):
        if (i * (i + 1) // 2) <= n:
            continue
        else:
            return i - 1
