'''
Problem Link: https://leetcode.com/problems/pascals-triangle/
Difficulty: Easy

Problem statement:

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mem = {}
        #most important thing to remember is:
        #(nCr = n-1Cr-1 + n-1Cr)
        # and pascals triangle are values of nCr
        def comb(n,r):
            if r==0:
                return 1
            if n <= r:
                return 1
            else:
                if mem.get((n,r), None) is not None:
                    return mem[(n,r)]
                else:
                    mem[(n,r)] = comb(n-1,r-1) + comb(n-1,r)
                    return mem[(n,r)]
        ans = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(comb(i,j))
            ans.append(row)
        print(ans)
        return ans