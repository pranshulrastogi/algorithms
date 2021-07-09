'''
Problem link:https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Difficulty: Medium(DP)
'''
# it is similar to longest common substring

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
        mx = 0
        for i in range(1,l1+1):
            for j in range(1, l2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    mx = max(dp[i][j],mx)
        ans = mx
        return ans