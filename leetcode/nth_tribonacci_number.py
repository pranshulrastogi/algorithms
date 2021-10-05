"""
Problem link:https://leetcode.com/problems/n-th-tribonacci-number/
Difficulty: Easy
"""


def tribonacci(n: int) -> int:
    t = [0, 1, 1]
    for i in range(3, n + 1):
        s = t[i - 1] + t[i - 2] + t[i - 3]
        t.append(s)
    return t[n]
