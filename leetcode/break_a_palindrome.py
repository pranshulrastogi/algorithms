"""
Problem link: https://leetcode.com/problems/break-a-palindrome/
Difficulty: Medium
"""


def breakPalindrome(palindrome: str) -> str:
    l = len(palindrome)
    mid = 0 if l % 2 == 0 else l // 2
    print(mid)
    res = ""
    if l == 1:
        return ""
    for i, c in enumerate(palindrome):
        if mid and i == mid:
            res += c  # changing the mid, won't change the fact that its palindrome
            continue
        else:
            if c == "a" and i != l - 1:
                res += c
                continue
            elif c == "a" and i == l - 1:
                res += "b"  # if we are at last, we don't have any other way but to increase
            else:
                res += "a"
                res += palindrome[i + 1 :]  # we got the chr to change, break now
                break
    return res
