'''
Problem link: https://leetcode.com/problems/sum-of-square-numbers/
Difficulty: Medium
'''
from math import sqrt, ceil, floor
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        def isExist(n):
            
            s = sqrt(n)
            
            return ceil(s) == floor(s)
        
        for a in range(0,2**31):
            dif = c - a**2
            if dif < 0:
                return False
            if isExist(dif):
                return True
        return False
        