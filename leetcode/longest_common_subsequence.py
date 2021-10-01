"""
Problem Link: https://leetcode.com/problems/longest-common-subsequence/
Difficulty: Medium
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    l1, l2 = len(text1), len(text2)
    LCS = {}

    def lcs(i, j):
        if i >= l1 or j >= l2:
            return 0
        if LCS.get((i, j), None):
            return LCS[(i, j)]
        if text1[i] == text2[j]:
            LCS[(i, j)] = 1 + lcs(i + 1, j + 1)
        else:
            LCS[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
        return LCS[(i, j)]

    ans = lcs(0, 0)
    print(ans)
    return ans
