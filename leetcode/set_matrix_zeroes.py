'''
Problem link: https://leetcode.com/problems/set-matrix-zeroes/
Difficulty: Medium
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeros_r = set()
        zeros_c = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros_r.add(r)
                    zeros_c.add(c)
        
        for r in zeros_r:
            for c in range(cols):
                matrix[r][c]=0
        for r in range(rows):
            for c in zeros_c:
                matrix[r][c] = 0
                