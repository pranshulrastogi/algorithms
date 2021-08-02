'''
Problem link: https://leetcode.com/problems/01-matrix/
Difficulty: Medium

'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nr, nc = len(mat), len(mat[0])
        ans = [[10**4 for i in range(nc)] for j in range(nr)]
        
        
        # one time conver left and up
        for i in range(nr):
            for j in range(nc):
                if mat[i][j]==0:
                    ans[i][j]=0
                else:
                    if i>0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j]+1) 
                    if j>0:
                        ans[i][j] = min(ans[i][j], 1+ ans[i][j-1])
        # one time cover right and bottom
        for i in range(nr-1,-1,-1):
            
            for j in range(nc-1,-1,-1):
                if i<nr-1:
                    # print(i,nr,nc)
                    ans[i][j] = min(ans[i][j], 1+ ans[i+1][j])
                if j<nc-1:
                    ans[i][j] = min(ans[i][j], 1+ ans[i][j+1])
            
                    
        print(ans)
        return ans