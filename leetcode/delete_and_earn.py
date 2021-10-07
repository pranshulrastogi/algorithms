"""
Problem link: https://leetcode.com/problems/delete-and-earn/
Difficulty: Medium
"""
from collections import Counter


def deleteAndEarn(nums) -> int:
    count = sorted(Counter(nums).items(), key=lambda k: k)
    print(count)
    l = len(count)
    dp = [0 for _ in range(l)]
    for i in range(l):
        k, v = count[i]
        if i == 0:
            dp[i] = k * v
        else:
            if count[i - 1][0] + 1 == k:
                if i - 2 >= 0:
                    m = max(dp[: i - 1])
                else:
                    m = 0
                dp[i] = m + (k * v)
            else:
                dp[i] = max(dp[:i]) + (k * v)
    ans = max(dp)
    print(ans)
    return ans
