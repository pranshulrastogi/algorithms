"""
Problem link: https://leetcode.com/problems/reverse-words-in-a-string/
Difficulty: Medium
"""


def reverseWords(s):
    stack = []
    # remove the trailing or leading spaces
    s = s.strip()

    for word in s.split():
        stack.append(word)

    rev = ""
    while stack:
        rev += stack.pop()
        if stack:
            rev += " "
    return rev
