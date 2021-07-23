'''
Problem link: https://leetcode.com/problems/partition-array-into-disjoint-intervals/
Level: Medium

solution:
maintain 2 arrays mxleft and mnright, where mxleft[i] tells you the max element till ith element
and mnright tells you min element till ith element from right side(n-1, i) 
'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l,r = "",""
        ans = -1
        count = 0
        
        n = len(nums)
        
        mxleft = [None] * n
        mnright = [None] * n
        
        m = nums[0]
        for i in range(n):
            m = max(m, nums[i])
            mxleft[i] = m
        
        m = nums[-1]
        for i in range(n-1,-1,-1):
            m = min(m, nums[i])
            mnright[i] = m
            
        for i in range(1,n):
            if mxleft[i-1] <= mnright[i]:
                ans = i
                break
        print(ans)
        return ans