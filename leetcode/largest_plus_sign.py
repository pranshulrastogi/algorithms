'''
https://leetcode.com/problems/largest-plus-sign/
Medium
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        
        dp = [[0]*n for _ in range(n)]
        ans = 0
        for r in range(n):
            count=0 # count left
            for c in range(n):
                if (r,c) not in banned:
                    count += 1
                else:
                    count=0
                dp[r][c] = count
            count=0 # count right till r,c
            for c in range(n-1, -1, -1):
                if (r,c) not in banned:
                    count+=1
                else:
                    count=0
                dp[r][c] = min(dp[r][c], count)
        
        for c in range(n):
            count=0# count from up
            for r in range(n):
                if (r,c) not in banned:
                    count+=1
                else:
                    count=0
                dp[r][c] = min(dp[r][c], count)
            
            count=0 # count from down
            for r in range(n-1, -1, -1):
                if (r,c) not in banned:
                    count+=1
                else:
                    count=0
                dp[r][c] = min(dp[r][c], count)
                ans = max(dp[r][c],ans)
        print(ans)
        return ans
                
                