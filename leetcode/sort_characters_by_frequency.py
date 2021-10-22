"""
Problem link: https://leetcode.com/problems/sort-characters-by-frequency/
Difficulty: Medium
"""


def frequencySort(s):
    from collections import Counter

    counter = Counter(s)
    sorted_counter = dict(
        sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)
    )
    ans = ""
    for k, v in sorted_counter.items():
        ans += k * v
    return ans
