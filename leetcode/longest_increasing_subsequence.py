'''
Problem link:https://leetcode.com/problems/longest-increasing-subsequence/
Difficulty: Medium
'''
# solution is a dp, 
'''
Logic: let dp[i] be the longest increasing subseqence that ends with nums[i]
so dp[i] = max(dp[j]+1) for j in range(i) if nums[i] > nums[j]
else dp[i] = 1
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1 for i in range(l)]
        
        for i in range(1,l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        ans = max(dp)
        print(ans)
        return ans