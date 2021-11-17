"""
Problem link: https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy
"""


def fib(n):
    """
    :type n: int
    :rtype: int
    """
    f = [0 for i in range(n + 1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
