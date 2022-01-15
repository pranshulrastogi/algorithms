"""
Problem link: https://leetcode.com/problems/best-sightseeing-pair/
Difficulty: Medium
"""


def maxScoreSightseeingPair(values):
    """
    :type values: List[int]
    :rtype: int
    """
    mx_score = float("-inf")

    l = len(values)
    mx_val = values[0]
    for i in range(1, l):
        mx_val -= 1  # decay for distance
        score = mx_val + values[i]
        mx_score = max(score, mx_score)
        mx_val = max(mx_val, values[i])
    return mx_score
