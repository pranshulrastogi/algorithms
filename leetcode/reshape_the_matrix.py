'''
Problem link: https://leetcode.com/problems/reshape-the-matrix/
difficulty: Easy
'''
'''
idea is to flatten the 2D matrix to 1D and then traverse
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat # as you can't create/delete or leave the elements
        flat = [] # to capture flattened mat
        ans = [] # to capture the answer
        for ele in mat:
            flat.extend(ele)
        print(flat)
        i=0
        for row in range(r):
            new_row = []
            for col in range(c):
                new_row.append(flat[i])
                i+=1
            ans.append(new_row)
        print(ans)
        return ans
        