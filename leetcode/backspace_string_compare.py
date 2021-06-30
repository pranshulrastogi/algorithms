'''
Problem link: https://leetcode.com/problems/backspace-string-compare/
difficulty: easy
Problem statement:
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''
# we will use stack, whenever we encounter '#' we pop else we push
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = s
        tt = t
        s = []
        t = []
        for ele in st:
            if ele=='#': 
                if s: s.pop() 
            else: s.append(ele)
        
        for ele in tt:
            if ele == '#':
                if t: t.pop()
            else:
                t.append(ele)
        if s==t:
            return True
        return False